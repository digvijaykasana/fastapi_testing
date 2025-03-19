# FastAPI Testing Project

A comprehensive FastAPI application with SQLAlchemy integration, unit testing, and a beautiful frontend interface. This project demonstrates best practices for building and testing modern web APIs with Python.

![FastAPI Logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Frontend Interface](#frontend-interface)
- [Database](#database)
- [Development Process](#development-process)
- [Best Practices](#best-practices)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project was created to demonstrate best practices for unit testing and behavior-driven testing in a FastAPI application. It includes a complete API for managing inventory items, with full CRUD operations, SQLAlchemy ORM integration, comprehensive test coverage, and a modern web interface.

## Features

- **RESTful API**: Implements standard REST principles with proper HTTP methods
- **Database Integration**: SQLAlchemy ORM with SQLite backend
- **Comprehensive Testing**: Unit tests for all endpoints with pytest
- **Interactive Documentation**: Auto-generated Swagger and ReDoc documentation
- **Modern Web Interface**: Responsive UI for managing items
- **Data Visualization**: Charts and statistics on the dashboard
- **Dark/Light Mode**: Theme switching for user preference
- **Search & Filtering**: Dynamic item filtering and sorting
- **Form Validation**: Client-side validation for data entry

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM)
- **Pydantic**: Data validation and settings management
- **pytest**: Testing framework for Python
- **Jinja2**: Template engine for Python
- **HTML/CSS/JavaScript**: Frontend technologies
- **ApexCharts**: Interactive charts for data visualization
- **Font Awesome**: Icon library
- **SQLite**: Lightweight disk-based database

## Project Structure
fastapi-testing/
├── app/
│   ├── init.py
│   ├── main.py             # FastAPI application initialization and routes
│   ├── database.py         # Database configuration and models
│   ├── models.py           # Pydantic models for request/response
│   ├── static/             # Static files for frontend
│   │   ├── css/
│   │   │   └── styles.css  # CSS styles for UI
│   │   └── js/
│   │       └── script.js   # JavaScript for UI functionality
│   └── templates/
│       └── index.html      # HTML template for UI
├── tests/
│   ├── init.py
│   ├── conftest.py         # pytest fixtures and configuration
│   └── test_main.py        # Tests for API endpoints
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/fastapi-testing.git
   cd fastapi-testing

2. Create a virtual environment:
    python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

## Running the Application
    Start the FastAPI server:

    uvicorn app.main:app --reload

The application will be available at:

API: http://127.0.0.1:8000/
API Documentation: http://127.0.0.1:8000/docs
Alternative Documentation: http://127.0.0.1:8000/redoc
Web Interface: http://127.0.0.1:8000/ui

API Documentation
The API provides the following endpoints:

GET /: Welcome message
GET /ui: Web interface
POST /items/: Create a new item
GET /items/{item_id}: Get a specific item
GET /items/: Get all items (with pagination)
PUT /items/{item_id}: Update an item
DELETE /items/{item_id}: Delete an item

Each endpoint is fully documented in the Swagger UI available at /docs.
## Testing
Run the tests with pytest:
pytest

The tests cover all API endpoints and ensure that:

Items can be created
Items can be retrieved
Items can be updated
Items can be deleted
Error cases are handled correctly

## Frontend Interface
The web interface is accessible at /ui and provides:
Dashboard

Overview of item statistics
Number of items in inventory
Average price of items
Total value of inventory
Price distribution chart

Items Management

List of all items with details
Add new items
Edit existing items
Delete items
Search functionality
Sorting options

About Page

Information about the application
Technology stack details

## Database
The application uses SQLAlchemy with a SQLite database. The database schema includes:
Items Table

id: Integer (Primary Key)
name: String
description: String (Optional)
price: Float

## Development Process
The development process followed these steps:

Project Setup: Created basic folder structure and installed dependencies
Database Design: Defined SQLAlchemy models and database connection
API Development: Implemented CRUD endpoints with FastAPI
Testing: Added unit tests for all endpoints
Frontend Development: Created responsive UI with HTML/CSS/JavaScript
Integration: Connected frontend to backend API
Documentation: Added comprehensive documentation

## Best Practices
This project demonstrates several best practices:
FastAPI Best Practices

Dependency injection for database sessions
Pydantic models for request/response validation
Proper status codes and error handling
Path and query parameter typing
API documentation with examples

Testing Best Practices

Isolated tests with fixtures
Test database separation
Coverage of success and error cases
Dependency overriding for testing
Clear test naming and organization

General Best Practices

Clean code organization
Type hints
Comprehensive documentation
Separation of concerns
Proper error handling

Future Improvements

User authentication and authorization
More advanced filtering and sorting options
Data export functionality
More detailed analytics
Image upload for items
Pagination controls
Deployment instructions for production