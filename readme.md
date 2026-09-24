# Google ADK Shopping Agent

A beginner-friendly AI agent built using Google ADK and Gemini.

## Features

- Basic AI Agent
- Gemini integration
- Tool Calling
- Product Search Tool
- SQL Tool
- SQLite Database

## Technologies Used

- Python
- Google ADK
- Gemini 2.5 Flash
- SQLite
- SQL

## Project Structure

```text
AGENT/
│
├── shopping_agent/
│   ├── __init__.py
│   ├── agent.py
│   ├── tools.py
│   ├── database.py
│   └── students.db
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd agent
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Google API Key Setup

Create a `.env` file in the project root.

Add:

```text
GOOGLE_API_KEY=your_google_api_key_here
```

Replace the placeholder with your own Google API key.

**Do not share or upload your API key.**

## Run the Agent

From the project root, run:

```bash
adk run shopping_agent
```

## Example

You can ask:

```text
Show me students with attendance below 75%.
```

The agent uses the SQL tool to retrieve the required data from the SQLite database.

You can also ask:

```text
Show me laptops under ₹60,000.
```

The agent uses the product search tool to find matching products.

## How Tool Calling Works

```text
User
  ↓
AI Agent
  ↓
Selects the required tool
  ↓
Tool performs the task
  ↓
Result returned to Agent
  ↓
Final response
```

## SQL Agent Flow

```text
User
  ↓
Agent
  ↓
SQL Tool
  ↓
SQLite Database
  ↓
SQL Query
  ↓
Result
  ↓
Agent Response
```

## Database

The project uses SQLite.

The database contains a `students` table with:

- id
- name
- attendance

The sample database is included for demonstration.

## Recreate the Database

If required, run:

```bash
cd shopping_agent
python database.py
```

Then return to the project root:

```bash
cd ..
```

## Important Notes

- Each student should use their own Google API key.
- Keep the API key private.
- Do not upload `.env` to GitHub.
- Make sure the virtual environment is activated.
- Run the ADK command from the project root.

## Learning Flow

```text
Basic Agent
     ↓
Tool Calling
     ↓
External Data
     ↓
SQL
     ↓
Database-powered Agent
```