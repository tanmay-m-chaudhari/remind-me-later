# Remind-Me-Later API

This is a straightforward **RESTful API** built with **Django** and **Django REST Framework**. It enables users to create and manage reminders for future dates and times, delivered via **Email** or **SMS**. The API includes standard **CRUD** (Create, Read, Update, Delete) endpoints.

---

## 📖 Description

This project allows user to:

* **Schedule reminders** with personalized messages.
* Select their preferred delivery method: **Email** or **SMS**.

---


## ⚙️ Setup and Installation

Follow these steps to get the Remind-me-later backend up and running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/tanmay-m-chaudhari/remind-me-later.git
cd assignment
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 2. Import postman json
* Import the provided Postman JSON file as a raw collection to easily interact with the API endpoints.

