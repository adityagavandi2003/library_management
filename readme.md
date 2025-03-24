# Django Project Setup Guide

Follow these steps to set up and run the Django project on your local machine.

## Prerequisites

Ensure you have the following installed:

- Python (>= 3.8)
- pip (Python package manager)
- virtualenv (optional but recommended)
- Git (if cloning from a repository)

## Installation Steps

### 1. Clone the Repository (if applicable)

```sh
git clone https://github.com/adityagavandi2003/library_management.git
cd your-django-project
```

### 2. Create a Virtual Environment (Optional but Recommended)

```sh
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```sh
  source venv/bin/activate
  ```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Apply Migrations

```sh
python manage.py migrate
```

### 5. Create a Superuser (Optional, for Admin Access)

```sh
python manage.py createsuperuser
```

Follow the prompts to set up an admin user.

### 6. Run the Development Server

```sh
python manage.py runserver
```

The project should now be accessible at `http://127.0.0.1:8000/`


### Deactivating Virtual Environment

```sh
deactivate
```

## Troubleshooting

- If you face issues with dependencies, try running:
  ```sh
  pip install --upgrade pip
  pip install -r requirements.txt
  ```
- Ensure the `.env` file has the correct settings.
- If migrations fail, try:
  ```sh
  python manage.py makemigrations
  python manage.py migrate
  ```


