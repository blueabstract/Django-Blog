# 📝 Django Blog

A full-featured blog web application built with Django — supports user authentication, post creation, profile management, password reset via email, and a clean editorial UI.

---

## ✨ Features

- **User Authentication** — Register, login, logout
- **Password Reset** — Reset password via Gmail email link
- **Profile Management** — Update username, email, and profile picture
- **Blog Posts** — Create, read, update, and delete posts
- **Author Pages** — View all posts by a specific user
- **Pagination** — Posts paginated across multiple pages
- **Responsive UI** — Built with Bootstrap 5, styled with a bold editorial design

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap 5 |
| Database | SQLite (default) |
| Forms | django-crispy-forms + crispy-bootstrap4 |
| Images | Pillow |
| Environment | python-dotenv |
| Fonts | Playfair Display, Space Grotesk (Google Fonts) |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/blueabstract/Django-Blog.git
cd Django-Blog/django_project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django django-crispy-forms crispy-bootstrap4 Pillow python-dotenv
```

Or if a `requirements.txt` is present:

```bash
pip install -r ../requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file in the `django_project` folder (same level as `manage.py`):

```
EMAIL_USER=yourgmail@gmail.com
EMAIL_PASS=your16digitapppassword
```

> **Note:** `EMAIL_PASS` must be a Gmail **App Password**, not your regular Gmail password.
> Generate one at: Google Account → Security → 2-Step Verification → App Passwords

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. (Optional) Load sample posts

```bash
python manage.py loaddata posts.json
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit: **http://127.0.0.1:8000**

---

## 📁 Project Structure

```
django_project/
├── blog/                   # Main blog app
│   ├── templates/blog/     # HTML templates
│   ├── static/blog/        # CSS & static files
│   ├── models.py           # Post model
│   ├── views.py            # Blog views (CBV)
│   └── urls.py             # Blog URL routes
├── users/                  # User auth app
│   ├── templates/users/    # Login, register, profile, password reset templates
│   ├── models.py           # Profile model
│   ├── forms.py            # User & profile forms
│   └── views.py            # Auth views
├── django_project/         # Project settings
│   ├── settings.py
│   └── urls.py
├── .env                    # Environment variables (not committed to git)
└── manage.py
```

---

## 🖼️ Pages

| URL | Description |
|---|---|
| `/` | Home — all posts |
| `/post/<id>/` | Post detail |
| `/post/new/` | Create new post |
| `/post/<id>/update/` | Edit a post |
| `/post/<id>/delete/` | Delete a post |
| `/user/<username>/` | Posts by a specific user |
| `/register/` | Register a new account |
| `/login/` | Login |
| `/logout/` | Logout |
| `/profile/` | Update profile info & picture |
| `/password-reset/` | Request a password reset email |
| `/password-reset/done/` | Confirmation that email was sent |
| `/password-reset-confirm/<uidb64>/<token>/` | Set a new password |
| `/password-reset-complete/` | Password reset success page |

---

## ⚙️ Configuration

Key settings in `django_project/settings.py`:

```python
from dotenv import load_dotenv
load_dotenv()

# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Media files (profile pictures)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Email (Gmail SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_USER')
```

---

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `EMAIL_USER` | Your Gmail address |
| `EMAIL_PASS` | Your Gmail App Password (16 characters, no spaces) |

> Never commit your `.env` file to GitHub. Make sure it's listed in `.gitignore`.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
