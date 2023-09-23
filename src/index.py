import sys
from functions import get_todo_list_progress


employee_id = sys.argv[1]

output = get_todo_list_progress(employee_id)

print(output)