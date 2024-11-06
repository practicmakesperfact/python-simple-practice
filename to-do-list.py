# add task 
#  remove task
# mark task 
# show task
def main():
    tasks = []
    while True:
      print("1. Add task")
      print("2. show task")
      print("3. mark task as done")
      print("4. Exit")
    
      choice = input("inter your choice :")
      if choice =='1':
         n_tasks = int(input("how many taskes you want to add: "))
         for i in range(n_tasks):
             task = input("Enter the task: ")
             tasks.append({"task":task, "done":False})
             print("task added")
      elif choice =='2':
           print("\n tasks")
           for index, task in enumerate(tasks):
            status = 'Done' if task['done'] else 'not done'
            print(f"{index +1}.{task['task']} - {status}")
      elif choice == '3':
           task_index = int(input("Enter the task number to mark as done: "))-1
           if 0 <=task_index < len(tasks):
             tasks[task_index]['done']=True
             print('task mark as done!')
           else:
              print('invalid task number')
      elif choice =='4':
           print("Existing the to-do-list.")
           break
      else :
          print("invalid choice. please try again")
if __name__=="__main__":
    main()

