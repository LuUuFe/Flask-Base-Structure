# Flask School System

Basic structure of a Flask project divided into folders, similar to the MVC pattern, but I prefer to call it MVFC (Models, Views, Forms and Controllers).

---

## Technologies Used

- Python 3.10+
- Bootstrap 5
- DataTables
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- SQLite (as the default database)

---

## Installation and Setup

### 1. Clone the Repository

```bash
$ git clone git@github.com:LuUuFe/Flask-Base-Structure.git
$ cd Flask-Base-Structure
```

### 2. Create a Virtual Environment

It is highly recommended to create a virtual environment to avoid dependency conflicts.

```bash
# On Linux or macOS
$ python3 -m venv venv
$ source venv/bin/activate

# On Windows
$ python -m venv venv
$ venv\Scripts\activate
```

### 3. Install Dependencies

With the virtual environment activated, install the dependencies listed in the `requirements.txt` file.

```bash
$ pip install -r requirements.txt
```

### 4. Run the Application

Start the local server:

```bash
$ python run.py
```

The application will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## Project Structure

```
Flask-School-System/
|
|-- app/
|   |-- __init__.py       # Flask application configuration
|   |-- Controllers/      # Controller templates and models
|   |-- Forms/            # Flask-WTF forms
|   |-- Models/           # Database models definition
|   |-- routes.py         # Application routes
|   |-- templates/        # HTML files
|   |-- static/           # Static files (CSS, JS, images)
|   |-- config.py         # Application configuration
|
|-- instance/
|   |-- data.db           # Database (SQLite)
|-- requirements.txt      # Project dependencies
|-- run.py                # Application entry point
```

---

## Contribution

If you want to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit your changes with a Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE).

