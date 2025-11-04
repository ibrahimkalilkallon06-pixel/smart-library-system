# test_operations.py
from operations import *

def run_tests():
    print("Running system tests...\n")

    # Add books
    assert "successfully" in register_book("101", "Python Crash Course", "Eric Matthes", "Education", 3)
    assert "successfully" in register_book("102", "Brave New World", "Aldous Huxley", "Fiction", 2)

    # Add members
    assert "added successfully" in register_member("T001", "Kallon", "kallon@example.com")

    # Borrow book
    assert "borrowed" in borrow_book("T001", "101")

    # Return book
    assert "returned" in return_book("T001", "101")

    # Search
    results = find_book("Python", search_by="title")
    assert len(results) > 0

    # Remove member
    assert "deleted" in remove_member("T001")

    print("✅ All tests passed successfully!")

if __name__ == "__main__":
    run_tests()
