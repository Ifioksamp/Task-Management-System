# Task Management System

A Django-based task management system that allows users to create, manage, join, and comment on tasks. The system includes user authentication and profile management features.

## Features

- User registration and authentication
- Profile management with profile picture upload
- Task creation, update, and deletion
- Joining and leaving tasks
- Commenting on tasks (only for users who have joined the task)
- Task search functionality
- User profile viewing with a list of tasks created by the user
- Responsive design using Bootstrap

## Installation

## Prerequisites

- Python 3.8+
- Django 3.2+
- pip (Python package installer)

## Clone the Repository


## git clone https://github.com/Ifioksamp/Task-Management-System.git
 - cd todolist


## Create a Virtual Environment
 - python -m venv venv
 - source venv/bin/activate   # On Windows use `venv\Scripts\activate`

## Install Dependencies
 - pip install -r requirements.txt

## Set Up the Database
 - Run the following commands to create and set up the database:

	- python manage.py makemigrations
	- python manage.py migrate

## Create a Superuser
	- python manage.py createsuperuser

## Run the Development Server
 - Start the Django development server:
	- python manage.py runserver


## Usage

 ### User Registration and Authentication
 - Register a new user by clicking on the "Sign Up" link.
 - Log in using the registered email and password.

## Profile Management
 - After logging in, click on your username at the top right to view your profile.

 - Edit your profile by clicking the "Edit Profile" button, which opens a modal for editing profile details.

## Task Management
 - Create a new task by clicking the "Add Task" button on the homepage.
 - View task details by clicking on the task title.
 - Edit or delete tasks that you have created.
 - Join a task by clicking the user-plus icon next to the task.
 - Leave a task by clicking the sign-out icon next to the task.
 - Comment on tasks that you have joined.
 - Search Tasks
 - Use the search bar on the homepage to search for tasks by title.


### Project Structure
task-management-system/
│
├── todo/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   ├── signup.html
│   │   ├── task_detail.html
│   │   └── update_task.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── todolist/
	 ── static/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt

## Acknowledgements
 - Django - The web framework used
 - Bootstrap - For responsive design
 - MDBootstrap - Material Design for Bootstrap
 - Font Awesome - Icons


### Steps to follow:
1. **Replace the placeholder URL in the "Clone the Repository" section with the actual URL of your GitHub repository.**
2. **Update any additional dependencies in the `requirements.txt` file.**
3. **Adjust the project structure section if there are additional folders or significant changes.**
4. **Ensure the instructions reflect the actual steps required to run your project.**

With this `README.md`, users should have a clear understanding of how to set up and use your project.
