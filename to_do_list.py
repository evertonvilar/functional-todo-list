# to_do_list.py

# Função de alta ordem: recebe outra função como argumento
def process_tasks(tasks, func):
    return [func(task) for task in tasks]

# Closure: cria função interna que lembra o "prefixo"
def task_prefixer(prefix):
    def add_prefix(task):
        return f"{prefix}: {task}"
    return add_prefix

# Função principal
def main():
    # List comprehension (gera lista inicial de tarefas)
    tasks = [f"Tarefa {i}" for i in range(1, 6)]

    print("Lista inicial:", tasks)

    # Função lambda (para transformar em maiúsculas)
    upper_tasks = process_tasks(tasks, lambda t: t.upper())
    print("Maiúsculas:", upper_tasks)

    # Closure aplicada (prefixo “IMPORTANTE”)
    prefix_func = task_prefixer("IMPORTANTE")
    prefixed_tasks = process_tasks(tasks, prefix_func)
    print("Com prefixo:", prefixed_tasks)

if __name__ == "__main__":
    main()
