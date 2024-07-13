def add_task(tasks, task):
  task = {"task": task, "completed": False}
  tasks.append(task)
  print(f"Tarefa {task['task']} foi adicionada com sucesso!")
  return

def view_task(tasks):
  print("\nLista de tarefas: ")
  if not tasks:
    print("Nenhuma tarefa adicionada ainda.")
    return
  for index,task in enumerate(tasks, start=1):
    status = "✓" if task["completed"] else "" 
    task = task["task"]
    print(f"{index}. [{status}] {task}")
   
    
def update_task(tasks,index,new_task):
  try:
    adjust_index = int(index) - 1
    if adjust_index >= 0 and adjust_index < len(tasks):
      tasks[adjust_index]["task"] = new_task
      print(f"Tarefa {index} atualizada para {new_task}")
    else:
      print("Não existe essa tarefa, verifique o número digitado!")
  except ValueError:
    print("Por favor, digite um número válido para o índice da tarefa.")

def completed_task(tasks, index):
  try:
    adjust_index = int(index) - 1
    if adjust_index >= 0 and adjust_index < len(tasks):
      tasks[adjust_index]["completed"] = True
      print(f"Tarefa {index} marcada como completa!")
    else:
      print("Não existe essa tarefa, verifique o número digitado!")
  except ValueError:
    print("Por favor, digite um número válido para o índice da tarefa.")

def delete_completed_tasks(tasks):
  for task in tasks:
    if task["completed"]:
      tasks.remove(task)
  print("Tarefas completas deletadas com sucesso!")
  return