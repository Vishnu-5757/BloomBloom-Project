# Todo Manager Django Project

This Django application allows you to create and manage todo projects, including adding, editing, updating, and marking tasks as completed. It also enables exporting project summaries as secret Gists on GitHub.

## Features

* Project creation and management
* Task management within projects (CRUD operations)
* Marking tasks as completed
* Exporting project summaries as secret Gists on GitHub (Markdown format)

## Installation

**Prerequisites:**

* Python (version 3.X) - https://www.python.org/downloads/
* pip (package installer for Python) - Usually bundled with Python

**Steps:**

1. **Clone the repository (if applicable):**

   ```bash
   git clone git@github.com:Vishnu-5757/todo_manager.git

2. **Create Virtual Environment:**

   

     ```bash
    # If you haven't installed virtualenv, install it first
    pip install virtualenv

    # Create a virtual environment
    virtualenv venv

    # Activate the virtual environment
    source venv/bin/activate   # for Unix/Linux
    # or
    .\venv\Scripts\activate    # for Windows
2. **Install Dependencies:**

   
    ```bash 
    pip install -r requirements.txt


3. **Run Migrations:**

   
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    
6. **Start the development server:**
   ```bash
   python manage.py runserver
7. **Access the application:**
   * By default, the server runs at http://127.0.0.1:8000/
   * You need to create an account and log in for full functionality.


8. **Export project summary :**
   * The application will generate the Markdown-formatted project summary and export it as a secret Gist on GitHub.

9. **Create a .env File**:
    * In the root directory of your Django project, create a file named .env.
    * GITHUB_ACCESS_TOKEN=<secret_key>
   




