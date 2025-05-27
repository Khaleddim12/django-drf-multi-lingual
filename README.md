# Django DRF Application with Internationalization

## Features

- REST API built with Django REST Framework
- Multi-language support (English & Arabic)
- PostgreSQL database (configurable to SQLite for development)
- Translation workflow with gettext

## Prerequisites

- Python 3.8+
- PostgreSQL 12+ (or SQLite for development)
- gettext installed on your system

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Khaleddim12/django-drf-multi-lingual.git
   cd django-drf-multi-lingual
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or 
   venv\Scripts\activate  # Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Database setup (PostgreSQL recommended):
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. the translation.py file is used to add multiple languages for each field
6. gettext_lazy is used to translate the required words using these commands:
   ```bash
   django-admin makemessages -l ar
   python manage.py compilemessages
7. Testing Translations(Run the server):
   ```bash
   python manage.py runserver
