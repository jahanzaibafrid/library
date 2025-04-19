import streamlit as st
import json
import os

# 📚 Library Class
class Library:
    def __init__(self, storage_file="library.json"):
        self.storage_file = storage_file
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def save_books(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, title, author):
        book = {"title": title, "author": author}
        self.books.append(book)
        self.save_books()

    def delete_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                return True
        return False

    def search_books(self, query):
        return [book for book in self.books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]


# 🚀 Streamlit App Start
st.title("📚 My Library Manager")

library = Library()

# Navigation
option = st.sidebar.selectbox("Choose an option", ["Add Book", "View Books", "Delete Book",
