# Little Lemon Django Project Setup

This guide will walk you through setting up and running the **Little Lemon** Django project on your local machine after cloning it from GitHub. Since the project is already built, you only need to clone the repository, set up your environment, and run the server.

## Prerequisites

Make sure you have the following installed:

- Python (3.8 or higher recommended)
- Django (version 3.2 or higher)

## Steps

### 1. Clone the Repository

Open your terminal and clone the GitHub repository.

```bash
git clone https://github.com/aniketraut16/littlelemon.git
```

Navigate to the project directory:

```bash
cd littlelemon
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
```

### 3. Set Up the Database

The project’s database is already configured, but you need to apply migrations to set up the database schema.

```bash
python manage.py migrate
```

### 4. Create a Superuser for Admin Access

To manage menu items and other data through the Django admin panel, create a superuser account.

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the username, email, and password for the admin account.

### 5. Run the Django Server

Now, you can start the Django development server to run the application.

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the site.

### 6. Access the Admin Interface

To add or manage menu items, log into the admin interface at `http://127.0.0.1:8000/admin` using the superuser credentials you created earlier.

### 7. Adding Menu Items

Once logged in, navigate to the **Menu Items** section in the Django admin to add menu items. You can add the following details for each item:

- **Name**
- **Price**
- **Description**
- **Image** (optional, but recommended)

### Project Structure

Here’s a quick overview of the project structure and key files:

- `littlelemon/` - Main project folder
- `menu/` - Django app for menu items
- `templates/menu/` - HTML templates for the views
- `urls.py` - URL routing for the app
- `models.py` - Database model for MenuItem

### Project URLs

- **Homepage**: `http://127.0.0.1:8000/`
- **About Page**: `http://127.0.0.1:8000/about/`
- **Menu**: `http://127.0.0.1:8000/menu/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

---
