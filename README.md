# Backend API - Subscription Management Dashboard

Django REST Framework API for the Subscription Management Dashboard.

## Key Features

*   Manages subscriptions (CRUD operations).
*   Calculates next renewal dates and monthly/annual costs.
*   Validates future renewal dates.

## API Endpoints

*   `GET    /api/subscriptions/`: List all subscriptions with calculated costs.
*   `POST   /api/subscriptions/`: Create a new subscription.
*   `DELETE /api/subscriptions/{id}/`: Delete a specific subscription.
*   `GET    /api/dashboard-summary/`: Get dashboard summary (e.g., total monthly spend).
*   `POST   /api/subscriptions/{id}/update-price/`: Update a subscription's price/cycle and record history.
*   `GET    /api/subscriptions/{id}/history/`: List price change history for a subscription.

**Live API:** `https://subsdashboardbe.onrender.com/api`

## Tech Stack

*   Python / Django / Django REST Framework (DRF)
*   PostgreSQL (Supabase)
*   Key Libraries: `dj-database-url`, `python-dotenv`, `python-dateutil`, `psycopg2-binary`, `django-cors-headers`

## Project Structure

*   `subscriptions/`: Django app containing models, views, serializers, and URLs for subscription management.
*   `mysite/`: Django project settings and main URL configuration.
*   `manage.py`: Django's command-line utility.
*   `requirements.txt`: Project dependencies.
*   `.env`: Environment variables (database URL, secret key, etc.).

## Local Development Setup

1.  **Prerequisites:** Python 3, pip.
2.  **Clone & Navigate:** Clone the repo and `cd Backend`.
3.  **Environment & Dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
4.  **Environment Variables:** Create `.env` (see example below).
5.  **Database Migrations:** `python3 manage.py migrate`
6.  **Run Server:** `python3 manage.py runserver` (API at `http://127.0.0.1:8000/api/subscriptions/`)

**Example `.env` Configuration:**

```dotenv
SECRET_KEY='your_django_secret_key'
DEBUG=True
# Use Supabase DIRECT connection string for local dev/migrations
DATABASE_URL='postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-SUPABASE-REF].supabase.co:5432/postgres'
# Keep DIRECT_URL same as DATABASE_URL for local dev
DIRECT_URL='postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-SUPABASE-REF].supabase.co:5432/postgres'
ALLOWED_HOSTS='localhost,127.0.0.1'
CORS_ALLOWED_ORIGINS='http://localhost:5173,http://127.0.0.1:5173' # Frontend URL
```
*(Replace placeholders. Use pooled Supabase URL for `DATABASE_URL` in production).*

## Deployment

*   Currently hosted on Render.