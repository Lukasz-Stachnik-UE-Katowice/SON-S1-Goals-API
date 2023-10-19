# Goals API Group 1 Stationary

## Description

This repository is a place for facilitating knowledge of Git and GitHub. It aims to show students various techniques that are used in a typical production setup. 

It's a pretty simple REST API for saving and sticking to goals, but not only goals like: “Learn python” or “Lose 5 kg”, additionally it can track habits etc. 

### Data Models

```python
Goal { 
    id: int
    due_date: str  # You can use a date format
    frequency: str  # You can use an enum for 'daily', 'weekly', 'monthly'
    progress: float
    reminders: List[dict]  # List of reminders with 'date_time' and 'message' - optional
    notes: List[dict]  # List of notes with 'date_time' and 'text' - optional
    privacy: str  # You can use an enum for 'private', 'shared', 'public' - optional
    shared_with: List[str]  # List of user_ids  - optional
    tags: List[str] - optional
    linked_resources: List[dict]  # List of linked resources with 'title' and 'url'  - optional
    comments: List[dict]  # List of comments with 'user_id', 'date_time', and 'text' - optional
    badges: List[str] - optional
}

GoalType { 
    case habit
    case milestone
}

User {
    id: UUID
    name: String
}
```

## Create python venv:

```bash
python -m venv ./.venv
```

### Windows activation

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux activation

```bash
source ./.venv/bin/activate
```

## How to download requirements

```bash
pip install -r requirements.txt
```

## Dependecies

```bash 
pip3 install "uvicorn[standard]" fastapi
```

## How to run: 

```bash
uvicorn app.main:app --reload
```
