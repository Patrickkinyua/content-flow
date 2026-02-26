# Content Flow - Blog API

A RESTful API for managing blog articles and tags, built with Django REST Framework. Users can create, read, update, and delete articles and tags with role-based access control.

## Overview

Content Flow is a lightweight blog content management system that supports:
- **Article Management**: Create drafts, publish articles, and manage content
- **Tag System**: Organize articles with tags
- **User Roles**: Writer and Editor roles for content management
- **User Authentication**: Custom user model with role-based permissions

## Tech Stack

- **Framework**: Django 6.0.2
- **API**: Django REST Framework (DRF)
- **Database**: SQLite (default)
- **Python**: 3.13.7
- **Environment**: Virtual environment (pipenv)

## Project Structure

```
content-flow/
├── config/              # Project configuration
│   ├── settings.py     # Django settings
│   ├── urls.py         # Main URL router
│   ├── wsgi.py         # WSGI application
│   └── asgi.py         # ASGI application
├── content/            # Blog content app
│   ├── models.py       # Article and Tag models
│   ├── serializers.py  # DRF serializers
│   ├── views.py        # ViewSets for API
│   ├── urls.py         # Content app URLs
│   └── migrations/     # Database migrations
├── users/              # User management app
│   ├── models.py       # CustomUser model
│   ├── middleware.py   # Custom middleware
│   └── migrations/     # Database migrations
├── manage.py           # Django management script
├── db.sqlite3          # SQLite database
└── Pipfile             # Pipenv dependencies
```

## Installation

### Prerequisites
- Python 3.13+
- pipenv (or pip + virtualenv)

### Setup

1. **Clone and navigate to the project**:
   ```bash
   cd content-flow
   ```

 2. **Install dependencies** (new step):
   ```bash
   pipenv install
   ```

 3. **Activate the virtual environment**:
   ```bash
   pipenv shell
   ```

 4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

 5. **Create a superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

 6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Base URL
```
http://127.0.0.1:8000/api/
```

### Articles (Content)

#### List all articles
```
GET /api/content/
```

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "status": "published",
    "title": "Getting Started with Django",
    "body": "Django is a powerful web framework...",
    "author": 1,
    "tags": [1, 2],
    "created_at": "2026-02-26T10:00:00Z",
    "updated_at": "2026-02-26T10:30:00Z"
  }
]
```

#### Create a new article
```
POST /api/content/
```

**Request body**:
```json
{
  "status": "draft",
  "title": "My New Article",
  "body": "Article content here...",
  "author": 1,
  "tags": [1, 2]
}
```

**Response** (201 Created):
```json
{
  "id": 2,
  "status": "draft",
  "title": "My New Article",
  "body": "Article content here...",
  "author": 1,
  "tags": [1, 2],
  "created_at": "2026-02-26T11:00:00Z",
  "updated_at": "2026-02-26T11:00:00Z"
}
```

#### Retrieve a specific article
```
GET /api/content/{id}/
```

**Response** (200 OK):
```json
{
  "id": 1,
  "status": "published",
  "title": "Getting Started with Django",
  "body": "Django is a powerful web framework...",
  "author": 1,
  "tags": [1, 2],
  "created_at": "2026-02-26T10:00:00Z",
  "updated_at": "2026-02-26T10:30:00Z"
}
```

#### Update an article (PUT)
```
PUT /api/content/{id}/
```

**Request body**:
```json
{
  "status": "published",
  "title": "Updated Title",
  "body": "Updated content...",
  "author": 1,
  "tags": [1]
}
```

**Response** (200 OK): Updated article object

#### Partial update an article (PATCH)
```
PATCH /api/content/{id}/
```

**Request body** (optional fields):
```json
{
  "status": "published",
  "title": "New Title"
}
```

**Response** (200 OK): Updated article object

#### Delete an article
```
DELETE /api/content/{id}/
```

**Response** (204 No Content)

---

### Tags

#### List all tags
```
GET /api/tag/
```

**Response** (200 OK):
```json
[
  {
    "name": "Django"
  },
  {
    "id": 2,
  }
]
```

#### Create a new tag
```
POST /api/tag/
```
**Request body**:
```json
{
  "name": "REST API"
}
```

**Response** (201 Created):
```json
{
  "id": 3,
  "name": "REST API"
}
```

#### Retrieve a specific tag
```
GET /api/tag/{id}/
```

**Response** (200 OK):
```json
{
  "id": 1,
  "name": "Django"
}
```

#### Update a tag (PUT)
```
PUT /api/tag/{id}/
```

```json
{
  "name": "Django Framework"
}
```

**Response** (200 OK): Updated tag object

#### Partial update a tag (PATCH)
```
PATCH /api/tag/{id}/
```

**Request body**:
```json
{
  "name": "Advanced Django"
}
```

**Response** (200 OK): Updated tag object

#### Delete a tag
```
DELETE /api/tag/{id}/
```

**Response** (204 No Content)

---

### Admin Panel
```
GET /admin/
```

Access the Django admin interface. Requires superuser credentials.

---

## Data Models

### Article Model
```python
class article(models.Model):
    status            # CharField: "draft" or "published"
    title             # CharField (max 200)
    body              # TextField
    author            # ForeignKey to CustomUser (CASCADE)
    tags              # ManyToManyField to tag
    created_at        # DateTimeField (auto-generated)
    updated_at        # DateTimeField (auto-updated)
```

### Tag Model
```python
class tag(models.Model):
    name              # CharField (max 50)
```

### CustomUser Model
```python
    role              # CharField: "writer" or "editor" (default: "writer")
```

## Usage Examples

### Using cURL

**List all articles**:
```bash
curl http://127.0.0.1:8000/api/content/
```

**Create an article**:
```bash
curl -X POST http://127.0.0.1:8000/api/content/ \
  -H "Content-Type: application/json" \
  -d '{
    "status": "draft",
    "title": "My First Post",
    "body": "This is my first blog post",
    "author": 1,
    "tags": []
```

**Update an article**:
```bash
curl -X PATCH http://127.0.0.1:8000/api/content/1/ \
  -H "Content-Type: application/json" \
  -d '{"status": "published"}'
```

**Delete an article**:
```bash
curl -X DELETE http://127.0.0.1:8000/api/content/1/
```

### Using Python (requests)

```python
import requests

BASE_URL = "http://127.0.0.1:8000/api"

response = requests.get(f"{BASE_URL}/content/")
articles = response.json()

# Create article
new_article = {
    "status": "draft",
    "title": "My Article",
    "body": "Content here",
    "author": 1,
    "tags": [1, 2]
}
response = requests.post(f"{BASE_URL}/content/", json=new_article)
created = response.json()

# Update article
update_data = {"status": "published"}
response = requests.patch(f"{BASE_URL}/content/1/", json=update_data)

# Delete article
```

## Configuration

Key settings in `config/settings.py`:

- **DEBUG**: `True` (set to `False` in production)
- **ALLOWED_HOSTS**: `[]` (configure for production)
- **DATABASES**: SQLite (can be switched to PostgreSQL, MySQL, etc.)
- **AUTH_USER_MODEL**: `users.CustomUser`
- **INSTALLED_APPS**: Includes Django admin, auth, DRF, users, and content apps

## Development

### Create a superuser
python manage.py createsuperuser
```

### Run migrations
```bash
python manage.py migrate
```

### Create new migrations
```bash
python manage.py makemigrations
```

### Access Django shell
```bash
python manage.py shell
```

### Run tests
```bash
python manage.py test
```

## Troubleshooting

### `TemplateDoesNotExist: rest_framework/api.html`
Ensure `rest_framework` is in `INSTALLED_APPS` in `config/settings.py`.

### Database locked error
Clear or recreate `db.sqlite3`:
```bash
rm db.sqlite3
python manage.py migrate
```

### Port already in use (8000)
Use a different port:
```bash
python manage.py runserver 8001
```

## Future Enhancements

- Authentication and permissions (JWT, token-based)
- Search and filtering for articles
- Pagination for large datasets
- Rate limiting
- Comments system
- Article versioning
- Advanced user permissions

## License

Proprietary. All rights reserved.

## Support

For issues or questions, please contact the development team.
