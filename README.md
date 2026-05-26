# 📝 Task Tracker CLI

A command-line interface (CLI) app to track and manage your tasks. Built with Python as part of the [Roadmap.sh](https://roadmap.sh) beginner projects.

## Features

- Add, update, and delete tasks
- Mark tasks as `todo`, `in-progress`, or `done`
- List all tasks or filter by status
- Data stored in a local JSON file

## Requirements

- Python 3.x

## Usage

```bash
# Add a task
python task_cli_sg.py add "Buy groceries"

# Update a task
python task_cli_sg.py update 1 "Buy groceries and cook dinner"

# Delete a task
python task_cli_sg.py delete 1

# Mark a task as in progress
python task_cli_sg.py mark-in-progress 1

# Mark a task as done
python task_cli_sg.py mark-done 1

# List all tasks
python task_cli_sg.py list

# List by status
python task_cli_sg.py list todo
python task_cli_sg.py list in-progress
python task_cli_sg.py list done

# Delete all tasks
python task_cli_sg.py clear
```

## Task Properties

Each task has the following properties:

- `ID` - Unique identifier
- `description` - Task description
- `status` - `todo`, `in-progress`, or `done`
- `createdAt` - Date and time of creation
- `updatedAt` - Date and time of last update