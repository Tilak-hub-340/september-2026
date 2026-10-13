import json
import sys


filename = "todo.json"
def load_tasks():
      #loads the tasks list the JSON file and gives you back the list of tasks.
      try :
           with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
                
      except FileNotFoundError:
            return[] 
      except json.JSONDecodeError:
            return[]     

def save_tasks(tasks):
    # Writes the list of tasks into the JSON file
         with open(filename, "w", encoding="utf-8") as f:
              json.dump(tasks, f, indent=2)

# save_tasks([
#     {"id": 1, "task": "buy milk", "status": "done"},
#     {"id": 2, "task": "drink milk", "status": "undone"},
# ])

def add_task(text):
      tasks = load_tasks()

      if len(tasks) == 0:
            new_id = 1 
      else:
           id =[]
           for t in tasks:
               id.append(t['id'])
           new_id = max(id) + 1 

      new_task = {"id":new_id, "task":text, "status":"undone"}
      tasks.append(new_task)
      save_tasks(tasks)

def list_tasks():
      tasks = load_tasks()

      if len(tasks) == 0:
            print("No tasks found.")
            return 
      for t in tasks:
            if t['status'] == 'done':
                  marker = "[x]"
            else:
                  marker = "[ ]"
            print(f"{t['id']}. {marker} {t['task']}")


def done_task(task_id):
      tasks = load_tasks()

      for t in tasks:
            if t['id'] == task_id:
                  t['status'] = 'done'
                  save_tasks(tasks)
                  print(f"Marked task {task_id} as done.")
                  return

      print(f"Task {task_id} not found.")                      


# add_task("buy milk")
# add_task("go to shop")
# done_task(1)
# done_task(4)     
# list_tasks()

def main():
      if len(sys.argv)<2:
            print("Usage: python todo.py add <text> | list | done <id>")
            return

      command = sys.argv[1]

      if command == 'list':
            list_tasks()
      elif command =="add":
            if len(sys.argv)<3:
                  print("plese provide a task to add.")
                  return 
            add_task(sys.argv[2])
      elif command == "done":
            if len(sys.argv)<3:
                  print("please provide a task id to mark as done.")
                  return
            try:
                  task_id = int(sys.argv[2])
            except ValueError:
                  print("Task id must be an integer.")
                  return
            done_task(task_id)  
      else:
            print("Unkowm command.")   

main()
