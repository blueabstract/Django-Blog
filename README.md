# 📝 Django Blog

A full-featured blog web application built with Django — supports user authentication, post creation, profile management, and a clean editorial UI.

---

## ✨ Features

- **User Authentication** — Register, login, logout
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
pip install django django-crispy-forms crispy-bootstrap4 Pillow
```

Or if a `requirements.txt` is present:

```bash
pip install -r ../requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. (Optional) Load sample posts

```bash
python manage.py loaddata posts.json
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

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
│   ├── templates/users/    # Login, register, profile templates
│   ├── models.py           # Profile model
│   ├── forms.py            # User & profile forms
│   └── views.py            # Auth views
├── django_project/         # Project settings
│   ├── settings.py
│   └── urls.py
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
| `/profile/` | Update profile info & picture |

---

## ⚙️ Configuration

Key settings in `django_project/settings.py`:

```python
# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Media files (profile pictures)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
