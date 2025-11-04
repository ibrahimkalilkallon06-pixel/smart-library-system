# demo.py
from operations import *

# Add books
print(register_book("B001", "The Alchemist", "Paulo Coelho", "Fiction", 4))
print(register_book("B002", "Deep Learning", "Ian Goodfellow", "Education", 3))
print(register_book("B003", "Rich dad poor dad", "Robert Kiyosaki", "Fiction", 2))
print(register_book("B004", "Cosmos", "Carl Sagan", "Non-Fiction", 3))
print(register_book("B005", "Dune", "Frank Herbert", "Sci-Fi", 5))

# Add members
print(register_member("M001", "Kallon Ibrahim", "kallon@example.com"))
print(register_member("M002", "Mr. Lavalie", "lavalie@example.com"))
print(register_member("M003", "Kalmata", "kalmata@example.com"))

# Search for a book
print("\nSearching books by author 'George':")
print(find_book("George", search_by="author"))

# Update member info
print(update_member("M002", email="mr.Lavalie025@example.com"))

# Borrowing books
print(borrow_book("M001", "B001"))
print(borrow_book("M001", "B003"))
print(borrow_book("M001", "B005"))

# Trying to borrow unavailable book
print(borrow_book("M002", "B003"))  # may fail if no copies left

# Return a book
print(return_book("M001", "B001"))

# Delete a book and member
print(remove_book("B002"))
print(remove_member("M003"))

# Display current records
print("\n📚 Books in Library:")
print(library_books)

print("\n👥 Registered Members:")
print(registered_members)

