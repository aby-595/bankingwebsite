# 🏦 Banking Website (Django)

A Django-based web application simulating a basic banking system. This project allows users to register, log in, and fill out application forms. After submission, users receive a confirmation message.

---

## 🔧 Features

- User registration and login
- Application form submission
- Post-submission confirmation message
- Django admin panel support
- Modular backend architecture using Django

---

## 🚀 Technologies Used

- Python 3.x
- Django
- HTML, CSS, JavaScript
- SQLite (default Django DB)

---

## 📁 Folder Overview

- `bankingproject/` – Django project config (`settings.py`, `urls.py`, etc.)
- `banking_app/` – Your Django app logic (views, models, forms)
- `static/` – Static files (CSS, JS, etc.)
- `assets/` – Project assets (images, etc.)

---

## ▶️ How to Run This Project

> Make sure you have Python and Django installed.

```bash
# 1. Clone the repository
git clone https://github.com/aby-595/bankingwebsite.git
cd bankingwebsite

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt  # if available

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver



