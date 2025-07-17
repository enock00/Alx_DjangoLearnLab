```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```
Expected output (verify with `Book.objects.get(id=1).title`):
`'Nineteen Eighty-Four'`