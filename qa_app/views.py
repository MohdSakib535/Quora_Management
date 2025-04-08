from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.views.decorators.csrf import ensure_csrf_cookie
from markdown import markdown
from django.utils.safestring import mark_safe
from django.contrib import messages

@login_required
def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'qa_app/home.html', {'questions': questions})

@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.content = mark_safe(markdown(question.content, extensions=['fenced_code']))

    answers = question.answers.all().order_by('-created_at')

    for answer in answers:
        answer.content = mark_safe(markdown(answer.content, extensions=['fenced_code']))

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question_detail', pk=pk)
    else:
        form = AnswerForm()
    
    return render(request, 'qa_app/question_details.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    
    return render(request, 'qa_app/ask_question.html', {'form': form})

@login_required
@ensure_csrf_cookie
def like_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
        liked = False
    else:
        answer.likes.add(request.user)
        liked = True
    
    return JsonResponse({
        'liked': liked,
        'likes_count': answer.total_likes()
    })


@login_required
def My_questions(request):
    question_data= Question.objects.filter(author=request.user).order_by('-created_at')
    return render(request,'qa_app/my_question.html',{'questions': question_data})


@login_required
def update_question(request, pk):
    """Allow users to update their own questions"""
    question = get_object_or_404(Question, pk=pk)
    
    if question.author != request.user:
        messages.error(request, "You don't have permission to edit this question.")
        return redirect('question_detail', pk=pk)
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, "Your question has been updated successfully!")
            return redirect('question_detail', pk=pk)
    else:
        form = QuestionForm(instance=question)
    
    return render(request, 'qa_app/update_question.html', {'form': form, 'question': question})
