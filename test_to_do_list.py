# test_to_do_list.py
import unittest
from to_do_list import process_tasks, task_prefixer

class TestTodoList(unittest.TestCase):
    def test_process_tasks_with_lambda(self):
        tasks = ["a", "b"]
        result = process_tasks(tasks, lambda x: x.upper())
        self.assertEqual(result, ["A", "B"])

    def test_task_prefixer_closure(self):
        prefix_func = task_prefixer("FIXO")
        self.assertEqual(prefix_func("tarefa"), "FIXO: tarefa")

if __name__ == "__main__":
    unittest.main()
