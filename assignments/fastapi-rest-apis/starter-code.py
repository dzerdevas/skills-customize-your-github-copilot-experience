from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books: List[Book] = []
next_id = 1


@app.get("/")
def root() -> dict:
    return {"message": "Welcome to the FastAPI Books API"}


@app.get("/books", response_model=List[Book])
def get_books() -> List[Book]:
    # Task: Return the full list of books.
    return books


@app.post("/books", response_model=Book)
def create_book(book: BookCreate) -> Book:
    global next_id
    # Task: Create a new book with a unique ID, store it, and return it.
    new_book = Book(id=next_id, title=book.title, author=book.author)
    books.append(new_book)
    next_id += 1
    return new_book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: BookCreate) -> Book:
    # Task: Find the book by ID and update it. Raise 404 if not found.
    for index, existing in enumerate(books):
        if existing.id == book_id:
            books[index] = Book(id=book_id, title=updated_book.title, author=updated_book.author)
            return books[index]
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict:
    # Task: Remove the book by ID. Raise 404 if not found.
    for index, existing in enumerate(books):
        if existing.id == book_id:
            books.pop(index)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
