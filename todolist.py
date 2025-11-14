class TodoList:
    def __init__(self,tasks= []):
        self.tasks = tasks
    def add_task(self,task):
        if task not in self.tasks:
            self.tasks.append(task)
        else:
            return f"{task} already exists"
    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"{task} removed.")
        else:
            print(f"{task} not in your to do lists")
    def show_tasks(self):
        return (f"You have {len(self.tasks)} remaining tasks.\ncurrent task = {self.tasks}")                                                                        
todo = TodoList([])
todo.add_task("task 1")
todo.add_task("task 2")
todo.add_task("task 3")
todo.add_task("task 4")
todo.add_task("task 5")
print(todo.show_tasks())
todo.remove_task("task")
todo.remove_task("task 1")
