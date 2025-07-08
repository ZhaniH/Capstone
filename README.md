# Django Capstone Project

This is a Django-based web application that consolidates all the skills learned in the course, including relational databases, application frameworks, version control, and containerization.

## Prerequisites
- Python 3.8+
- Docker (optional, for containerized deployment)
- Git (for version control)

## Installation & Setup

### Using Virtual Environment (Recommended)
1. Clone the repository:
   ```bash
   git clone [https://github.com/ZhaniH/Capstone]
   cd your-Capstone

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Access the application at: http://127.0.0.1:8000

Using Docker
docker build -t django-app .
docker run -p 8000:8000 django-app

project-root/
├── docs/            # Sphinx-generated documentation
├── your_app/        # Main Django application
├── project_name/    # Project settings
├── requirements.txt # Project dependencies
├── Dockerfile       # Docker configuration
└── .gitignore       # Specifies ignored files


cd docs/
make html
Configuration
Create a .env file in the project root with your environment variables (not committed to version control)

Required variables will typically include:

SECRET_KEY

DEBUG

DATABASE_URL

Contributing
Fork the repository

Create a new branch (git checkout -b feature-branch)

Commit your changes (git commit -am 'Add new feature')

Push to the branch (git push origin feature-branch)

Create a new Pull Request

   
