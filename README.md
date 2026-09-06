# DataPilot – AI-Powered SQL Analytics Assistant

DataPilot is an AI-powered SQL analytics assistant that lets users interact with a database using natural language.

Instead of manually writing SQL queries, users can ask questions such as **"Which products have the highest sales?"** and DataPilot uses Gemini to generate and execute the appropriate SQL query.

## Features

* Natural language to SQL generation using Gemini
* Automatic SQL validation
* Automatic SQL correction when a query fails
* SQLite database integration
* FastAPI backend
* React frontend
* Database exploration
* Query results displayed in a table
* Example analytics questions

## Tech Stack

**Frontend**

* React
* Vite
* JavaScript
* CSS

**Backend**

* Python
* FastAPI
* SQLAlchemy
* SQLGlot
* SQLite
* Gemini API

## How It Works

```text
User Question
      ↓
React Frontend
      ↓
FastAPI Backend
      ↓
Gemini API
      ↓
SQL Generation
      ↓
SQL Validation
      ↓
SQL Execution
      ↓
SQLite Database
      ↓
Results
      ↓
React Dashboard
```

## Project Structure

```text
DataPilot/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   └── services/
│   ├── database/
│   ├── requirements.txt
│   └── test_gemini.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

## Getting Started

### Backend

```bash
cd backend
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside `backend`:

```text
GEMINI_API_KEY=your_api_key_here
```

Initialize and seed the database:

```bash
python database/init_db.py
python database/seed.py
```

Start the backend:

```bash
python -m uvicorn app.main:app --reload
```

### Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Then open the local frontend URL shown by Vite.

## Example Questions

Try asking:

* Which products cost more than 20,000?
* Show all customers from the South region.
* What are the top-selling products?
* Which customer generated the highest sales?
* Show total sales by region.

## Future Improvements

* Interactive data visualizations
* Persistent query history
* Support for additional databases
* AI-generated analytical insights
* User authentication
* Cloud deployment

## Author

**Prabhas Reddy**

GitHub: [@prabhasreddy0210](https://github.com/prabhasreddy0210)
