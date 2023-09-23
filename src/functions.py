import requests;

API = 'https://jsonplaceholder.typicode.com'

endpoints = {
  "users": f"{API}/users", # https://jsonplaceholder.typicode.com/users
  "todos": f"{API}/todos" # https://jsonplaceholder.typicode.com/todos
}

def get_todo_list_progress(employee_id: int) -> str:
  # Obtenemos el empleado con id "employee_id"
  get_employee_endpoint = f"{endpoints['users']}/{employee_id}" # https://jsonplaceholder.typicode.com/users/1
  employee_response = requests.get(get_employee_endpoint)
  employee = employee_response.json()

  # Obtenemos la lista de tareas del empleado con id "employee_id"
  get_employee_todos_endpoint = f"{endpoints['todos']}?userId={employee_id}" # https://jsonplaceholder.typicode.com/todos?userId=1
  todos_response = requests.get(get_employee_todos_endpoint)
  todos = todos_response.json()

  todos_quantity = len(todos)

  # Filtramos las tareas para obtener la lista de tareas completadas
  completed_todos = []
  
  for todo in todos:
    if todo["completed"] == True:
      completed_todos.append(todo)

  completed_todos_quantity = len(completed_todos)

  # Preparamos el texto de salida
  first_line = f"Employee {employee['name']} is done with tasks({completed_todos_quantity}/{todos_quantity}):\n"

  next_line = ''

  for completed_todo in completed_todos:
    next_line = next_line + "\t " + completed_todo["title"] + "\n"

  return first_line + next_line