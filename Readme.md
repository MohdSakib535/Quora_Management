# QuoraClone - Django Q&A Platform

QuoraClone is a Quora-inspired web application built with Django that allows users to ask questions, provide answers, and engage with content through likes.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Question Management**: Create, read, update, and view questions
- **Answer System**: Post answers to questions
- **Interaction**: Like answers posted by other users
- **User Dashboard**: View and manage your own questions
- **Markdown Support**: Format questions and answers with Markdown syntax

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/quora-clone.git
cd quora-clone
```

2. **Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up the database**

```bash
python manage.py makemigrations accounts qa_app
python manage.py migrate
```

5. **Create a superuser (admin)**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

7. **Access the application**

Open your web browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

```
quora_management/
│
├── Quora_management/          # Main project directory
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL configuration
│   └── ...
│
├── accounts/             # User authentication app
│   ├── forms.py          # User registration forms
│   ├── urls.py           # Authentication URLs
│   ├── views.py          # Authentication views
│   └── ...
│
├── qa_app/               # Q&A functionality app
│   ├── forms.py          # Question and answer forms
│   ├── models.py         # Question and Answer models
│   ├── urls.py           # Q&A URLs
│   ├── views.py          # Q&A views
│   └── ...
│
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── accounts/         # Authentication templates
│   └── qa_app/           # Q&A templates
│
└── requirements.txt      # Project dependencies
```

## Core Functionality

### User Authentication

- Register a new account
- Login with username and password
- Logout functionality

### Questions

- View all questions on the homepage
- View a specific question with its answers
- Ask a new question
- Edit your own questions
- View all your questions in one place

### Answers

- Post answers to questions
- View answers to specific questions

### Interaction

- Like/unlike answers
- See the number of likes on each answer

## Markdown Support

This application supports Markdown formatting for questions and answers, allowing rich text formatting.

### Examples of Markdown Syntax

- **Bold text**: `**bold**`
- *Italic text*: `*italic*`
- Headers: `# Header 1`, `## Header 2`, etc.

- Links: `[link text](URL)`
- Code: `` `code` `` or code blocks with triple backticks


## Technology Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (default) - can be configured for PostgreSQL, MySQL, etc.
- **Text Formatting**: Markdown
- **Authentication**: Django built-in authentication system

## Future Enhancements

- Comment system for answers
- User profiles
- Search functionality

## License

Mohd Sakib