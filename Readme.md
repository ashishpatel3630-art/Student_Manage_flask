````markdown
# 🎓 Flask Student Management System

A simple **Flask CRUD (Create, Read, Update, Delete)** application to manage student records. This project stores student information in a JSON file instead of a database, making it perfect for beginners learning Flask.

---

## 🚀 Features

- ➕ Add new students
- 📋 View all students
- ✏️ Edit student details
- 🗑️ Delete students
- 💾 Data stored in a JSON file
- 🌐 Simple and clean web interface

---

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML
- CSS
- JSON

---

## 📁 Project Structure

```
Student-Management-System/
│
├── app.py
├── students.json
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
│
├── static/
│   └── style.css
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-management-system.git
```

### 2. Navigate to the project folder

```bash
cd student-management-system
```

### 3. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install flask
```

or

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

The application will start at:

```
http://127.0.0.1:5000/
```

Open the URL in your browser.

---

## 📌 CRUD Operations

### ➕ Add Student

- Enter student name
- Enter student age
- Click **Add Student**

---

### 📋 View Students

The homepage displays all students stored in the JSON file.

---

### ✏️ Edit Student

- Click **Edit**
- Update the information
- Save changes

---

### 🗑️ Delete Student

- Click **Delete**
- The student record is removed instantly.

---

## 💾 Data Storage

All student records are stored inside:

```
students.json
```

Example:

```json
[
    {
        "name": "Ashish",
        "age": "21"
    },
    {
        "name": "Rahul",
        "age": "22"
    }
]
```

---

## 📦 Requirements

```
Flask
```

Generate a requirements file:

```bash
pip freeze > requirements.txt
```

Example:

```
Flask==3.1.0
```

---

## 🎯 Learning Concepts

This project demonstrates:

- Flask Routing
- GET & POST Requests
- HTML Forms
- CRUD Operations
- JSON File Handling
- Templates using Jinja2
- Redirects
- Basic Web Development with Flask

---

## 🚀 Future Improvements

- SQLite/MySQL database integration
- Search students
- Student ID generation
- Validation
- Bootstrap UI
- Login Authentication
- Pagination
- REST API version

---

## 👨‍💻 Author

**Ashish Patel**

GitHub: https://github.com/your-username

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
````
