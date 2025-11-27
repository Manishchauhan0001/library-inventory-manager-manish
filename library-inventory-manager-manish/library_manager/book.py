# Book class – stores details of a single book

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status   # "available" or "issued"

    def issue(self):
        """Mark book as issued."""
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        """Return book (make available again)."""
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"

    def to_dict(self):
        """Convert book into dictionary for saving in JSON."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def __str__(self):
        return f'"{self.title}" by {self.author} (ISBN: {self.isbn}) - {self.status}'
