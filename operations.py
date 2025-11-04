
library_books = {}   # Stores book info by ISBN
registered_members = []  # Stores library users and their borrowed books
BOOK_GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Education")

# ---------------- Core Functions ---------------- #

def register_book(isbn, title, author, genre, copies):
    """Add a new book record to the library."""
    if isbn in library_books:
        return f"Book with ISBN {isbn} already exists."
    if genre not in BOOK_GENRES:
        return "Invalid genre type."

    library_books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total": copies,
        "available": copies
    }
    return f"Book '{title}' successfully registered."


def find_book(keyword, search_by="title"):
    """Search for books based on title or author name."""
    result = []
    for isbn, info in library_books.items():
        if search_by == "title" and keyword.lower() in info["title"].lower():
            result.append((isbn, info))
        elif search_by == "author" and keyword.lower() in info["author"].lower():
            result.append((isbn, info))
    return result


def register_member(member_id, name, email):
    """Register a new member into the system."""
    for member in registered_members:
        if member["id"] == member_id:
            return "Member ID already exists."
    registered_members.append({"id": member_id, "name": name, "email": email, "borrowed": []})
    return f"Member '{name}' added successfully."


def update_member(member_id, **kwargs):
    """Update member details (like email or name)."""
    for member in registered_members:
        if member["id"] == member_id:
            member.update(kwargs)
            return f"Member '{member_id}' updated."
    return "Member not found."


def borrow_book(member_id, isbn):
    """Allow a member to borrow a book if available."""
    if isbn not in library_books:
        return "Book not found."

    if library_books[isbn]["available"] <= 0:
        return "No copies available for borrowing."

    for member in registered_members:
        if member["id"] == member_id:
            member["borrowed"].append(isbn)
            library_books[isbn]["available"] -= 1
            return f"{member['name']} borrowed '{library_books[isbn]['title']}'."
    return "Member not found."


def return_book(member_id, isbn):
    """Return a borrowed book."""
    for member in registered_members:
        if member["id"] == member_id:
            if isbn in member["borrowed"]:
                member["borrowed"].remove(isbn)
                library_books[isbn]["available"] += 1
                return f"{member['name']} returned '{library_books[isbn]['title']}'."
            return "Book not borrowed by this member."
    return "Member not found."


def remove_book(isbn):
    """Delete a book from the system."""
    if isbn not in library_books:
        return "Book not found."

    if library_books[isbn]["available"] != library_books[isbn]["total"]:
        return "Cannot delete book while copies are borrowed."

    del library_books[isbn]
    return f"Book with ISBN {isbn} removed."


def remove_member(member_id):
    """Remove a member from the system if no books are borrowed."""
    for member in registered_members:
        if member["id"] == member_id:
            if member["borrowed"]:
                return "Cannot delete. Member still has borrowed books."
            registered_members.remove(member)
            return f"Member {member_id} deleted."
    return "Member not found."
