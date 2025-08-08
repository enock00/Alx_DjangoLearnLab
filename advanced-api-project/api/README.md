# Advanced API Project

## Overview
This project demonstrates a Django REST Framework API with custom serializers and generic views for CRUD operations.

## Endpoints
| Method | Endpoint                  | Description              | Permissions       |
|--------|---------------------------|--------------------------|-------------------|
| GET    | /api/books/               | List all books           | Public            |
| GET    | /api/books/<id>/          | Retrieve a single book   | Public            |
| POST   | /api/books/create/        | Create a new book        | Authenticated     |
| PUT    | /api/books/<id>/update/   | Update an existing book  | Authenticated     |
| DELETE | /api/books/<id>/delete/   | Delete a book            | Authenticated     |

## Notes
- Nested serializers handle `Author → Book` relationships.
- Custom validation ensures `publication_year` is not in the future.
- `IsAuthenticated` is applied for create, update, and delete operations.
