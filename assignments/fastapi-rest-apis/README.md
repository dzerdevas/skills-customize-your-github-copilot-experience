# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a REST API using the FastAPI framework. You will learn how to create endpoints, handle request and response data, and implement basic CRUD operations.

## 📝 Tasks

### 🛠️	Set Up a FastAPI App

#### Description
Create a new FastAPI application with one basic endpoint to confirm the API is running.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app object.
- Create a `GET /` endpoint that returns a welcome message in JSON format.
- Run successfully with Uvicorn.
- Return a valid JSON response when tested in a browser or with `curl`.


### 🛠️	Create Read and Create Endpoints

#### Description
Build endpoints for managing a simple in-memory list of books. Add one endpoint to list all books and one endpoint to add a new book.

#### Requirements
Completed program should:

- Store books in an in-memory Python list.
- Create a `GET /books` endpoint that returns all books.
- Create a `POST /books` endpoint that accepts a JSON body with `title` and `author`.
- Return a clear success response after adding a book.
- Reject invalid request data using FastAPI validation.


### 🛠️	Add Update and Delete Endpoints

#### Description
Expand the API by adding endpoints to update and delete books by ID.

#### Requirements
Completed program should:

- Assign each new book a unique integer `id`.
- Create a `PUT /books/{book_id}` endpoint to update a book's data.
- Create a `DELETE /books/{book_id}` endpoint to remove a book.
- Return an appropriate error response when a book ID does not exist.
- Support testing all endpoints in the FastAPI interactive docs at `/docs`.
