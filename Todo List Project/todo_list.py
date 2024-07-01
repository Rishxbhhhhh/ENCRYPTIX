from task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def update_task(self, index, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def mark_task_incomplete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_incomplete()

    def __str__(self):
        tasks_str = "\n".join(f"{i + 1}. {str(task)}" for i, task in enumerate(self.tasks))
        return tasks_str if tasks_str else "No tasks in the list."
