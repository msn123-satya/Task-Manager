# 🗂️ Task Manager API – FastAPI Backend

A simple yet powerful **Task Manager API** built with **FastAPI**, following RESTful principles.  
This backend-only project allows users to **create**, **read**, **update**, and **delete** tasks, and is tested directly via the **Swagger UI (OpenAPI)** provided by FastAPI.

---

## 🚀 Features

- 🧩 Built with **FastAPI** – lightweight, modern, and async-ready  
- 📌 RESTful API design using standard HTTP methods  
- 💾 Stores tasks using **SQLite** (file-based database)  
- ✅ Validated input data using **Pydantic models**  
- 🔄 Full **CRUD functionality** (Create, Read, Update, Delete)  
- 🌐 Tested directly on **Swagger UI (OpenAPI docs)** at `/docs`

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI  
- **Database:** SQLite (via `sqlite3`)  
- **Validation:** Pydantic  
- **Documentation:** Swagger UI / ReDoc (auto-generated)

---

## 📂 Project Structure

```
task-manager/
├── main.py              # FastAPI app and API routes
├── models.py            # Pydantic models for validation
├── database.py          # SQLite connection and table setup
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

### 2. Create a virtual environment and activate it

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI app

```bash
uvicorn main:app --reload
```

---

## 🔍 Test the API

Open your browser and go to:

- ✅ Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- 📘 ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

From here, you can test all endpoints like:

- `POST /tasks` → Create a new task  
- `GET /tasks` → Get all tasks  
- `PUT /tasks/{id}` → Update a task  
- `DELETE /tasks/{id}` → Delete a task  

---

## 📎 Example Task JSON

```json
{
  "title": "Write GitHub README",
  "description": "Document the project for public use",
  "completed": false
}
```

---

## 📃 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Developed by **Satyanarayana Makka**  
📬 [LinkedIn](https://www.linkedin.com/in/satya-python-dev) • [GitHub](https://github.com/msn123-satya)
