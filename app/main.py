from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List, Optional
from sqlalchemy.orm import Session
from app.database import get_db, ItemModel, SessionLocal
from pydantic import BaseModel
import uuid
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Item API",
    description="A robust API for managing items with SQLAlchemy database integration",
    version="0.2.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="app/templates")

# Pydantic models
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    
    class Config:
        orm_mode = True

@app.middleware("http")
async def log_requests(request, call_next):
    request_id = str(uuid.uuid4())
    start_time = datetime.now()
    
    logger.info(f"Request started | ID: {request_id} | Path: {request.url.path}")
    
    response = await call_next(request)
    
    process_time = (datetime.now() - start_time).total_seconds() * 1000
    logger.info(f"Request completed | ID: {request_id} | Time: {process_time:.2f}ms")
    
    return response

@app.get("/ui", response_class=HTMLResponse)
async def get_ui(request: Request):
    """
    Renders the UI for the Item Manager application.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/", summary="Welcome endpoint", description="Returns a welcome message for the API")
def read_root():
    """
    Returns a welcome message for the Item API.
    
    This is the root endpoint that can be used to verify the API is running.
    """
    return {"message": "Welcome to the Item API"}

@app.post("/items/", response_model=ItemResponse, 
          summary="Create a new item", 
          description="Creates a new item in the database with the provided details")
def create_item(item: Item, db: Session = Depends(get_db)):
    """
    Create a new item with the following properties:
    
    - **name**: Name of the item (required)
    - **description**: Optional description of the item
    - **price**: Price of the item (required)
    
    Returns the created item with its assigned ID.
    """
    db_item = ItemModel(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}", response_model=ItemResponse,
         summary="Get item by ID",
         description="Retrieves a specific item by its ID")
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific item by its ID.
    
    Parameters:
    - **item_id**: The unique identifier of the item to retrieve
    
    Returns the item if found, otherwise raises a 404 error.
    """
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/items/", response_model=List[ItemResponse],
         summary="Get all items",
         description="Retrieves a list of all items, with pagination support")
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all items.
    
    Parameters:
    - **skip**: Number of items to skip (for pagination)
    - **limit**: Maximum number of items to return (for pagination)
    
    Returns a list of items.
    """
    items = db.query(ItemModel).offset(skip).limit(limit).all()
    return items

@app.put("/items/{item_id}", response_model=ItemResponse,
         summary="Update an item",
         description="Updates an existing item with new details")
def update_item(item_id: int, item: Item, db: Session = Depends(get_db)):
    """
    Update an existing item by its ID.
    
    Parameters:
    - **item_id**: The unique identifier of the item to update
    - **item**: The new item details
    
    Returns the updated item if found, otherwise raises a 404 error.
    """
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db_item.name = item.name
    db_item.description = item.description
    db_item.price = item.price
    
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}",
            summary="Delete an item",
            description="Deletes an item by its ID")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item by its ID.
    
    Parameters:
    - **item_id**: The unique identifier of the item to delete
    
    Returns a success message if the item was deleted, otherwise raises a 404 error.
    """
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}

# Add some default items for demonstration
def add_default_items():
    db = SessionLocal()
    try:
        # Check if we already have items
        items_count = db.query(ItemModel).count()
        if items_count == 0:
            # Add some default items
            default_items = [
                ItemModel(name="Laptop", description="High-performance laptop with 16GB RAM", price=999.99),
                ItemModel(name="Smartphone", description="Latest model with 128GB storage", price=699.99),
                ItemModel(name="Headphones", description="Wireless noise-cancelling headphones", price=149.99)
            ]
            db.add_all(default_items)
            db.commit()
            logger.info("Added default items to the database")
    finally:
        db.close()

# Add default items when the app starts
add_default_items()