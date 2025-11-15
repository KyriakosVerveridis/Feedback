🏛️ Feedback Django App

A simple Django web application with two main apps: Reviews and Profiles.

The app allows users to:

Submit reviews with a name, text, and rating

Mark one review as their favorite; selecting a new favorite updates the previous choice

Upload profile images

View lists of reviews and detailed single review pages

🚀 Features

Reviews app demonstrates DetailView, ListView, TemplateView, and session management

Profiles app demonstrates CreateView, FormView, and file upload handling

Image uploads stored in uploads/images/

Clean integration of forms, models, views, CBVs, sessions, and file uploads

🛠️ Tech Stack

Backend: Django 5.2.8 (Python 3.12)

Frontend: HTML, CSS

Database: SQLite (default Django DB)

Environment Management: Virtual Environment + requirements.txt

Dependencies: asgiref==3.10.0, sqlparse==0.5.3, tzdata==2025.2, pillow==12.0.0

⚙️ Installation & Setup

Clone the repository
```
git clone https://github.com/yourusername/feedback.git
cd feedback
```


Create and activate a virtual environment
Windows PowerShell
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux
```
python -m venv venv
source venv/bin/activate
```


Install dependencies
```
pip install -r requirements.txt
```


Run database migrations
```
python manage.py migrate
```


Start the development server
```
python manage.py runserver
```


Access the app:

Main app: http://127.0.0.1:8000

Admin panel: http://127.0.0.1:8000/admin
