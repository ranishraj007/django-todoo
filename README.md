# Django Todo App

A simple todo application built with Django.

## Features

- Create, read, update, and delete todos
- Mark todos as complete
- Simple and clean UI

## Installation

1. Clone the repository
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run migrations:
    ```bash
    python manage.py migrate
    ```
4. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

Navigate to `http://localhost:8000` and start managing your todos.

## Project Structure

```
todo/
├── manage.py
├── requirements.txt
├── todos/
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── README.md
```

## License

MIT