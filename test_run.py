import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi_mcp import FastApiMCP


# Book model for validation
class Book(BaseModel):
    title: str
    author: str
    genre: str


app = FastAPI()

# Predefined list of books
books = [
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
]


@app.post("/add_book")
async def add_book(book: Book):
    books.append(book.dict())
    return {"message": "Book added", "books": books}


@app.delete("/delete_book")
async def delete_book(key: str, value: str):
    global books
    books = [b for b in books if b.get(key) != value]
    return {"message": "Book(s) deleted", "books": books}


@app.get("/list_books")
async def list_books():
    return {"books": books}


# --- MCP agent setup ---
from fastapi import APIRouter

mcp_router = APIRouter()
mcp = FastApiMCP(app)
mcp.mount(router=mcp_router)
app.include_router(mcp_router, prefix="/mcp")
