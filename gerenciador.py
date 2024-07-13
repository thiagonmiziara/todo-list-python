def add_task(tasks, task):
  task = {"task": task, "completed": False}
  tasks.append(task)
  print(f"Tarefa {task['task']} foi adicionada com sucesso!")
  return

def view_task(tasks):
  print("\nLista de tarefas: ")
  for index,task in enumerate(tasks, start=1):
    status = "✓" if task["completed"] else "" 
    task = task["task"]
    print(f"{index}. [{status}] {task}")
   
    
def update_task(tasks,index,new_task):
  adjust_index = int(index) - 1
  if adjust_index >= 0 and adjust_index < len(tasks):
    tasks[adjust_index]["task"] = new_task
    print(f"Tarefa {index} atualizada para {new_task}")
  else:
    print("Não existe essa tarefa, verifique o número digitado!")
    return  

def completed_task(tasks, index):
  adjust_index = int(index) - 1
  tasks[adjust_index]["completed"] = True
  print(f"Tarefa {index} marcada como completa!")
  return

def delete_completed_tasks(tasks):
  for task in tasks:
    if task["completed"]:
      tasks.remove(task)
  print("Tarefas completas deletadas com sucesso!")
  return

tasks = []

while True:
	print("\nMenu do gerenciador de tarefas:")
	print("1. Adicionar tarefa")
	print("2. Ver tarefas")
	print("3. Atualizar Tarefa")
	print("4. Completar Tarefa")
	print("5. Deletar tarefas completadas")
	print("6. Sair")

	choice = input("Digite a sua escolha: ")
	if choice == "1":
		task = input("Digite o nome da tarefa que deseja adicionar: ")
		add_task(tasks,task)
  
	elif choice == "2":
		view_task(tasks)
  
	elif choice == "3":
		view_task(tasks)
		index = input("Digite o número da tarefa que deseja atualizar: ")
		new_task = input("Digite a nova descrição da tarefa: ")
		update_task(tasks, index, new_task)
  
	elif choice == "4":
		view_task(tasks)
		index = input("Digite o número da tarefa que deseja completar: ")
		completed_task(tasks,index)
  
	elif choice == "5":
		delete_completed_tasks(tasks)
		view_task(tasks)
  
	elif choice == "6":
		break

print("Programa finalizado!")
