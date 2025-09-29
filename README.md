# Projeto - Lista de Tarefas (Programação Funcional)

Este repositório contém a implementação da atividade parcial da disciplina de Programação Funcional.

## 📌 Descrição
O sistema implementa um **Gerenciador de Lista de Tarefas (To-Do List)** simples, utilizando **Python 3** e conceitos de programação funcional.

## 🚀 Funcionalidades
- Armazenar uma lista de tarefas.
- Transformar tarefas em letras maiúsculas (usando **função lambda**).
- Adicionar prefixos às tarefas (usando **closure**).
- Processamento genérico de tarefas (usando **função de alta ordem**).

## 🛠️ Conceitos Funcionais Utilizados
- **Função lambda** → `lambda t: t.upper()`
- **List comprehension** → `[f"Tarefa {i}" for i in range(1, 6)]`
- **Closure** → `task_prefixer`
- **Função de alta ordem** → `process_tasks`

## 📂 Estrutura do Projeto
```
├── Requisitos.docx        # Documento de requisitos do projeto
├── to_do_list.py          # Código principal
├── test_to_do_list.py     # Casos de teste (unittest)
```

## ▶️ Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   cd NOME_DO_REPOSITORIO
   ```

2. Execute o programa principal:
   ```bash
   python to_do_list.py
   ```

3. Execute os testes unitários:
   ```bash
   python -m unittest test_to_do_list.py
   ```

## ✅ Exemplo de Saída
```
Lista inicial: ['Tarefa 1', 'Tarefa 2', 'Tarefa 3', 'Tarefa 4', 'Tarefa 5']
Maiúsculas: ['TAREFA 1', 'TAREFA 2', 'TAREFA 3', 'TAREFA 4', 'TAREFA 5']
Com prefixo: ['IMPORTANTE: Tarefa 1', 'IMPORTANTE: Tarefa 2', 'IMPORTANTE: Tarefa 3', 'IMPORTANTE: Tarefa 4', 'IMPORTANTE: Tarefa 5']
```

## 📚 Observações
- O projeto foi desenvolvido em Python 3.x.
- ChatGPT foi utilizado para auxiliar na estruturação dos requisitos, exemplos de código e testes.
