from typing import List

class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description


class TaskManager:
    def __init__(self):
        self.__tasks = []


    def add_task(self, title: str, description: str):
        task = Task(title, description)
        self.__tasks.append(task)


    @property
    def get_tasks(self):
        return self.__tasks


if __name__ == "__main__":
    task_manager = TaskManager()

    task_manager.add_task("Задача 1", "Описание задачи 1")
    task_manager.add_task("Задача 2", "Описание задачи 2")

    tasks = task_manager.get_tasks

    for inx, task in enumerate(tasks, start = 1):
            print(f"Задача {inx}: {task.title} - {task.description}")

