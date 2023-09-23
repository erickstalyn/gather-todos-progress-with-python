# Project name
Gather todos progress script using Python.

## Instalation
Make sure you have Python 3.7+ and [requests](https://pypi.org/project/requests/) module installed on your system. Then clone this repository:

`git clone https://github.com/erickstalyn/gather-todos-progress-with-python`

To run the script use the following command:

`python src/index.py ${EMPLOYEE_ID}`

## Exercise
Write a Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, return information about his/her TODO list progress.

### Requeriments
- You must use `urllib` or `requests` module
- The script must accept an integer as parameter, which is the employee ID
- The script must display on the standard output the employee TODO list progress in this exact format:
  - First line: `Employee EMPLOYEE_NAME is donde with task(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
    - `EMPLOYEE_NAME`: name of the employee
    - `NUMBER_OF_DONE_TASKS`: number of completed tasks
    - `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
  - Second and N next lines display the title of completed tasks: `TASKS_TITLE` (with 1 tabulation and 1 space before the `TASKS_TITLE`)

### Example
```
myComputer@ubuntu$ python gather_todos_progress.py 1
Employee Leanne Graham is done with tasks(11/20):
     et porro tempora
     quo adipisci enim quam ut ab
     illo est ratione doloremque quia maiores aut
     vero rerum temporibus dolor
     ipsa repellendus fugit nisi
     repellendus sunt dolores architecto voluptatum
     ab voluptatum amet voluptas
     accusamus eos facilis sint et aut voluptatem
     quo laboriosam deleniti aut qui
     molestiae ipsa aut voluptatibus pariatur dolor nihil
     ullam nobis libero sapiente ad optio sint
```