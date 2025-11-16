# Django Authentication System

## Overview

This Django application provides user authentication features, including login, signup, forgot password, change password, profile page, and dashboard. It uses Django's built-in authentication system and restricts access to pages based on authentication status.

## Features

- **Login**: Login with username/email and password.
- **Signup**: Create a new account with username, email, and password.
- **Forgot Password**: Request a password reset via email.
- **Change Password**: Authenticated users can change their password.
- **Dashboard**: Private page with a greeting message, accessible only to logged-in users.
- **Profile Page**: Displays user details such as username, email, and account creation date.

## Directory Structure

```
django_auth_system/
├── manage.py
├── db.sqlite3
├── users/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
└── templates/
    └── user/
        ├── login.html
        ├── signup.html
        ├── forgot_password.html
        ├── change_password.html
        ├── dashboard.html
        └── profile.html
```

## Key Files

- **`forms.py`**: Contains the forms for signup, login, forgot password, change password, etc.
- **`models.py`**: Extends Django’s `User` model for additional user-related information.
- **`views.py`**: Handles the logic for user registration, login, password reset, etc.
- **`urls.py`**: Maps URLs to views.
- **Email OTP**: Sends password reset emails using Django’s `send_mail` function and generates a reset link with a token.

## Configuration

- **Timezone**: Set to `Asia/Kolkata` in `settings.py`.
- **Email**: Configured with SMTP settings for sending OTP emails (Gmail is used in this example).

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'Null'
EMAIL_HOST_PASSWORD = 'Null'
```

## Running the Project

1. Clone the repository:
   ```bash
   git clone <https://github.com/sanskratipatel/Django_Auth_Assignment.git>
   cd django_auth_system
   ```

2. Migrate the database:
   ```bash
   python manage.py migrate
   ```

3. Run the server:
   ```bash
   python manage.py runserver
   ```

4. Access the app at `http://127.0.0.1:8000/signup/`.

## Video Demonstration

Watch the video demonstrating the features of the application [here](https://www.loom.com/share/6d4b50681f5a4bfbb35a70cf7f6c2067?sid=84e6853d-ead1-4ed9-ab2e-7b8ef4ff668e).

## License

This project is open-source and available under the MIT License.
```


