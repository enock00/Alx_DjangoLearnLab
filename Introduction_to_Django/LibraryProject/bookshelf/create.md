```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
```
Expected output (no errors, book instance created):
`<Book: 1984>`