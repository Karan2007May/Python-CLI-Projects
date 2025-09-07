# To-Do List Application
tasks = []  
def add_task(task):
  tasks.append(task)  
def view_tasks():
  print("Tasks:")
  for task in tasks:
   print(task)  
def remove_task(task):
 if task in tasks:
  tasks.remove(task)
  print(f"Task '{task}' removed.")
 else:
  print(f"Task '{task}' not found.")  
# Example usage
add_task("Read a book")
add_task("Write code")
view_tasks()
remove_task("Read a book")
view_tasks()

