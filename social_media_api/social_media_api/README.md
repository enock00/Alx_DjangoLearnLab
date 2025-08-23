# Social Media API

## Setup
1. Clone repo & install requirements:
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt

## Posts
- **List**: `GET /api/posts/`  
  Query params: `search=<term>`, `ordering=created_at|updated_at|title`, `page=<n>`
- **Create**: `POST /api/posts/` (Token)  
  Body: `{ "title": "str", "content": "str" }`
- **Retrieve**: `GET /api/posts/{id}/`
- **Update**: `PATCH /api/posts/{id}/` (Author only)
- **Delete**: `DELETE /api/posts/{id}/` (Author only)

## Comments
- **List**: `GET /api/comments/`
- **Create**: `POST /api/comments/` (Token)  
  Body: `{ "post": <post_id>, "content": "str" }`
- **Retrieve**: `GET /api/comments/{id}/`
- **Update**: `PATCH /api/comments/{id}/` (Author only)
- **Delete**: `DELETE /api/comments/{id}/` (Author only)

Endpoint: POST /api/accounts/users/<id>/follow/
Headers: Authorization: Bearer <token>

POST /api/posts/{post_id}/like/
