from django.urls import path
from . import views


urlpatterns = [
    
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('ask/', views.ask_question, name='ask_question'),
    path('like/<int:pk>/', views.like_answer, name='like_answer'),
    path('my-questions/', views.My_questions, name='my_questions'),
    path('question/<int:pk>/update/', views.update_question, name='update_question'),
]