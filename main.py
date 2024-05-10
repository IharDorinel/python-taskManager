class Task():
    def __init__(self, description, deadline, status="не выполнено"):
        self.description = description
        self.deadline = deadline
        self.status = status


    def mark_as_done(self):
        self.status = "выполнено"

task1 = Task("приготовить завтрак", "утро")
task2 = Task("зайти к соседке", "полдень")
task3 = Task("сходить в магазин", "вечер")

class Task_manager():
    def __init__(self):
        self.tasks_list = []

    def add_task(self, task):
        self.tasks_list.append(task)

    def print_tasks(self):
        for task in self.tasks_list:
            print(task.description)

    def mark_task(self, description):
        for task in self.tasks_list:
            if task.description == description:
                task.mark_as_done()
                return True
        return False

    def print_pending_tasks(self):
        pending_tasks = [task for task in self.tasks_list if task.status == "не выполнено"]
        if pending_tasks:
            for task in pending_tasks:
                print(f"{task.description} - {task.deadline}")



todoList = Task_manager()
todoList.add_task(task1)
todoList.add_task(task2)
todoList.add_task(task3)
todoList.print_tasks()
todoList.mark_task("приготовить завтрак")
todoList.print_pending_tasks()




