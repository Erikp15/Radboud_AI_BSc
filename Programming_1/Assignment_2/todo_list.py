todo_list = []
done_list = []

print("Welcome to your To-do list!")
for i in range(10):
    print("Options:")
    print("- Check To-do list [1]")
    print("- Check done list [2]")
    print("- Add item to do [3]")
    print("- Mark item as done [4]")
    print("- exit [5]")
    operation = int(input())

    if operation == 5:
        break

    if operation == 1:
        print("To-do list:")
        for task in todo_list:
            print(task)
    
    if operation == 2:
        print("Done list:")
        for task in done_list:
            print(task)
    
    if operation == 3:
        print("What you need to do:")
        task = input()
        todo_list.append(task)

    if operation == 4:
        print("Which task did you complete?")
        task = input()
        done_list.append(task)
        todo_list.remove(task)
        