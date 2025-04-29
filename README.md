# 🖋️ Advanced Task Manager (CLI)

This project is a simple command-line task manager built with Python.  
It leverages `argparse` for subcommands, manages tasks in a `JSON` file, uses environment variables for configuration, and logs all actions. Unit tests are included.

---

## 📅 Main Features

- Add new tasks with descriptions and priority levels.
- Display all current tasks.
- Remove tasks by specifying their ID.
- Store tasks persistently in a JSON file.
- Keep a log of all operations.
- Configure the path of the task file via an environment variable.
- Includes automated unit tests for core functionalities.

---

## 📦 Project Layout

```plaintext
advanced_cli_task_manager/
├── README.md
├── requirements.txt
├── task_manager/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── core.py
│   └── logger.py
├── tasks.json
└── tests/
    └── test_core.py
```

---

## 🛠️ Setup

1. Clone the project repository:

```bash
git clone https://github.com/Senbonzakura95/Day4_exo2
cd Day4_exo2
```

2. Install necessary packages:

```bash
pip3 install -r requirements.txt
```

(Use `pip3` to match your Python version on macOS.)

---

## 🚀 How to Use

**To add a new task:**
```bash
python3 -m task_manager.cli add "Complete assignment" 1
```

**To view all tasks:**
```bash
python3 -m task_manager.cli list
```

**To delete a task by ID:**
```bash
python3 -m task_manager.cli delete 1
```

---

## 📢 Configuration Options

By default, tasks are saved to `tasks.json` in the project directory.  
You can override this by setting the `TASKS_FILE_PATH` environment variable:

```bash
export TASKS_FILE_PATH="/custom/path/tasks.json"
```

---

## 📊 Testing

Run the unit tests using:

```bash
pytest
```

Be sure to run tests from the project root.

---