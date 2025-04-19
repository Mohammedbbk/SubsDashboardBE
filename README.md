# Backend API - Subscription Management Dashboard

This directory contains the Django REST Framework API backend for the Subscription Management Dashboard.

## Features

* Provides API endpoints for managing subscriptions (CRUD).
* Calculates next renewal dates upon creation.
* Validates renewal dates (must be in the future).
* Calculates and includes monthly/annual costs in API responses.

## API Endpoints

* `GET /api/subscriptions/`: Lists all subscriptions with calculated costs.
* `POST /api/subscriptions/`: Creates a new subscription.
* `DELETE /api/subscriptions/{id}/`: Deletes a specific subscription.

## Tech Stack

* Django & Django REST Framework (DRF)
* Python
* PostgreSQL (on Supabase)
* dj-database-url, python-dotenv, python-dateutil, psycopg2-binary, django-cors-headers

## Setup & Running

1.  **Prerequisites:** Python 3 and pip.
2.  **Navigate:** `cd Backend` (from project root).
3.  **Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4.  **Install Dependencies:** `pip install -r requirements.txt`
5.  **Environment Variables:** Create a `.env` file in this (`Backend`) directory:
    ```dotenv
    SECRET_KEY='your_strong_django_secret_key_here'
    DEBUG=True
    # Use Supabase DIRECT connection string for local dev/migrations
    DATABASE_URL='postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-SUPABASE-REF].supabase.co:5432/postgres'
    # Keep DIRECT_URL same as DATABASE_URL for local dev
    DIRECT_URL='postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-SUPABASE-REF].supabase.co:5432/postgres'
    ALLOWED_HOSTS='localhost,127.0.0.1'
    # Add your frontend local URL
    CORS_ALLOWED_ORIGINS='http://localhost:5173,[http://127.0.0.1:5173](http://127.0.0.1:5173)'
    ```
    *(Replace placeholders with actual values. Use pooled URL for `DATABASE_URL` when deploying).*
6.  **Database Migrations:** `python3 manage.py migrate`
7.  **Run Server:**
    ```bash
    python3 manage.py runserver
    ```
    * API is available at `http://127.0.0.1:8000/api/`

## Planned Hosting

* Render