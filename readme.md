# FastAPI Student Management System

## Overview

A robust Student Management API built with FastAPI and MongoDB, providing full CRUD (Create, Read, Update, Delete) functionality for student records with modern web development best practices.

## Important Note
Application is deployed on render , it has cold start problem , time will be required for the API to respond

## 🚀 Features

- **FastAPI Backend**: High-performance, easy-to-use API framework
- **MongoDB Integration**: Flexible NoSQL database for storing student records
- **Async Database Operations**: Efficient, non-blocking database interactions
- **Data Validation**: Comprehensive input validation using Pydantic
- **Automatic API Documentation**: Swagger UI and ReDoc support
- **Environment Configuration**: Secure, flexible environment variable management

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- MongoDB 4.0+
- pip (Python package manager)

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-management-api.git
cd student-management-api
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
# OR
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
# MongoDB Connection
DATABASE_URL=mongodb://localhost:27017/student_management
# Or use MongoDB Atlas connection string
```

## 🚦 Running the Application

### Development Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

- Swagger UI: `http://localhost:8000/docs`


## 🛢 Project Structure

```
student-management-api/
│
├── app/
│   ├── main.py          # FastAPI routes and application logic
│   ├── models.py        # Pydantic models for data validation
│   └── database.py      # MongoDB connection setup
│
├── .env                 # Environment variables (git-ignored)
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## 📡 API Endpoints

### Students Resource

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/students` | Create a new student record |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PATCH | `/students/{student_id}` | Update an existing student record |
| DELETE | `/students/{student_id}` | Delete a student record |

### Example Student Object in MongoDB

```json
{
  "_id": "unique_mongodb_id",
  "name": "John Doe",
  "age": 22,
  "address": {
    "city": "New York",
    "country": "USA"
  }
}
```



### Environment Variables for Production

- `DATABASE_URL`: MongoDB connection string


