from fucntions_tasks import add_task, view_task, update_task, completed_task, delete_completed_tasks

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
		if tasks:
			index = input("Digite o número da tarefa que deseja atualizar: ")
			new_task = input("Digite a nova descrição da tarefa: ")
			update_task(tasks, index, new_task)
		else:
			print("Não há tarefas para atualizar.")
  
	elif choice == "4":
		view_task(tasks)
		if tasks:
			index = input("Digite o número da tarefa que deseja completar: ")
			completed_task(tasks,index)
		else:
			print("Não há tarefas para completar.")
  
	elif choice == "5":
		delete_completed_tasks(tasks)
		view_task(tasks)
  
	elif choice == "6":
		break

print("Programa finalizado!")