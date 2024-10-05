days = ["Mon ", "Tue ", "Wed ", "Thu", "Fri"]
tasks = []

for day in days:
    n_tasks = int( input ("How many tasks do you have for " + day + "? "))
    today_tasks = []
    for i in range(n_tasks):
        task_name = input(" Task number " + str(i +1) + ": ")
        today_tasks.append(task_name)
    tasks.append(today_tasks)

print("What day is it today?" + str(days))
curr_day = input()

day_index = 4
if curr_day == "Mon":
    day_index = 0
elif curr_day == "Tue": 
    day_index = 1
elif curr_day == "Wed": 
    day_index = 2
elif curr_day == "Thu": 
    day_index = 3

print(" Here is your list of tasks for today ")
for task in tasks[day_index]:
    print(task)