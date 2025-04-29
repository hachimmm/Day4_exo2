import sys
import os
import unittest
import json

# ➔ Modifier le chemin pour trouver task_manager
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from task_manager.core import add_task, load_tasks, delete_task, save_tasks
from task_manager.config import TASKS_FILE

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Préparer un fichier vide pour les tests avant chaque test
        save_tasks([])

    def tearDown(self):
        # Nettoyer après chaque test
        if os.path.exists(TASKS_FILE):
            os.remove(TASKS_FILE)

    def test_add_task(self):
        add_task("Test Task", 5)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "Test Task")
        self.assertEqual(tasks[0]['priority'], 5)

    def test_delete_task(self):
        add_task("Task to Delete", 3)
        tasks = load_tasks()
        task_id = tasks[0]['id']
        delete_task(task_id)
        tasks_after = load_tasks()
        self.assertEqual(len(tasks_after), 0)

if __name__ == "__main__":
    unittest.main()