# Gerenciador de Tarefas em Python

## Descrição

Este é um gerenciador de tarefas simples e eficiente implementado em Python. Ele oferece uma interface de linha de comando para gerenciar suas tarefas diárias, permitindo adicionar, visualizar, atualizar, completar e deletar tarefas.

## Funcionalidades

- Adicionar novas tarefas
- Visualizar lista de tarefas
- Atualizar descrições de tarefas existentes
- Marcar tarefas como completas
- Deletar tarefas completadas
- Interface de usuário baseada em menu

## Requisitos

- Python 3.x

## Como usar

1. Clone este repositório ou baixe o arquivo `gerenciador.py`.
2. Abra um terminal e navegue até o diretório contendo `gerenciador.py`.
3. Execute o script com o comando: ```python gerenciador.py```


## Guia do Menu

1. **Adicionar tarefa**: Digite '1' e insira a descrição da nova tarefa.
2. **Ver tarefas**: Digite '2' para exibir todas as tarefas atuais.
3. **Atualizar Tarefa**: Digite '3', selecione o número da tarefa e forneça a nova descrição.
4. **Completar Tarefa**: Digite '4' e selecione o número da tarefa a ser marcada como completa.
5. **Deletar tarefas completadas**: Digite '5' para remover todas as tarefas concluídas.
6. **Sair**: Digite '6' para encerrar o programa.

## Estrutura do Código

O script `gerenciador.py` contém as seguintes funções principais:

- `add_task(tasks, task)`: Adiciona uma nova tarefa à lista.
- `view_task(tasks)`: Exibe todas as tarefas na lista.
- `update_task(tasks, index, new_task)`: Atualiza a descrição de uma tarefa existente.
- `completed_task(tasks, index)`: Marca uma tarefa como completa.
- `delete_completed_tasks(tasks)`: Remove todas as tarefas completadas da lista.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para forkar o repositório e enviar pull requests com melhorias.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.