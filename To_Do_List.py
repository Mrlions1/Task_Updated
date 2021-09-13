class check():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        self.n.remove(b)
    def dis(self):
        return (self.n) 
       
obj=check()
 
choice=1 
choice1=obj.dis()
while choice!=0: 
    print("\t<======Main Menu======>")
    print("0. Exit")
    print("1. Add a Task to Complete")
    print("2. Remove a Added Task")
    print("3. Display Added Tasks") 
    print("4. Mark Task as Complete\n=========================") 
    choice=int(input("Enter choice: ")) 

    if choice==1:
        n=str(input("Enter a To Do Task : "))
        obj.add(n)
        print("Task Added\n\n")
 
    elif choice==2:
        n=str(input("Enter Task to Remove : ")) 
        obj.remove(n)
        print("Task Removed: \n\n\n" )
 
    elif choice==3:
        print("List: ",obj.dis()) 
    
    elif choice==4: 
        print("Select from the following: ",obj.dis()) 
        if choice1!=0: 
            print(input("Type Task name to mark it as complete : "))  
            print("Task Marked as Complete") 
            print("Unmarked Tasks will be regarded as Incomplete\n\n\n")
            
    elif choice==0:
        print("Exiting....\n\n")
    else:
        print("Wrong Input. Kindly Enter the correct one")
 
print() 