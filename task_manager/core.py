import json
import os
from task_manager.logger import setup_logger
from task_manager.config import TASKS_FILE

logger = setup_logger()

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description, priority):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "priority": priority
    }
    tasks.append(task)
    save_tasks(tasks)
    logger.info(f"Added task: {description} (Priority: {priority})")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"[{task['id']}] {task['description']} (Priority: {task['priority']})")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    
    if len(tasks) == len(updated_tasks):
        print("Task ID not found.")
    else:
        # Reassign IDs
        for index, task in enumerate(updated_tasks, start=1):
            task['id'] = index
        save_tasks(updated_tasks)
        logger.info(f"Deleted task ID: {task_id}")