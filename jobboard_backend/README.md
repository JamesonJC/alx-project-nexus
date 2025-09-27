# Job Board Backend API

A Django-based backend API for a Job Board platform with role-based access control, optimized job search, and Swagger documentation.

## Features

- JWT authentication with Admin/User roles
- CRUD for Jobs and Categories
- Job filtering by location, category, and type
- Users can apply to jobs
- Admin can manage everything
- Swagger API docs at `/api/docs`

## Tech Stack Used

- Django + Django REST Framework
- PostgreSQL
- Simple JWT
- Swagger (`drf-yasg`)

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/token/` | POST | Get access & refresh tokens |
| `/api/jobs/` | GET | List/filter jobs |
| `/api/jobs/` | POST | Create a job (admin only) |
| `/api/categories/` | POST | Add new category (admin only) |
| `/api/applications/` | POST | Apply to a job (user) |

## Roles

- **Admin**: Full access to jobs, categories, and applications
- **User**: Can apply to jobs and view listings

## Run Locally

```bash
git clone https://github.com/JamesonJC/jobboard-backend.git
cd jobboard-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

