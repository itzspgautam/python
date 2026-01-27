students ={}

while True:
    print("\n1. Add Student")
    print("2. Update")
    print("3. Delete")
    print("4. Search")
    print("5.Exit")
    
    ch = int(input("Enter your choice: "))
    
    match ch:
        case 1:
            roll = int(input("Enter roll number to add: "))
            if roll in students:
                print("Student already exist with this roll number")
            else:
                name = input("Enter your name: ")
                marks =  int(input("Enter your marks: "))
                students[roll] = [name, marks]
                print("Student registered sucessfully.")
                print(students)
                
        case 2:
            roll = int(input("Enter roll number to update: "))
            if roll in students:
                name = input("Enter new name: ")
                marks =  int(input("Enter new marks: "))
                students[roll] = [name, marks]
                print(students)
            else:
                print("Student roll number is invalid or not registered.")
                
        case 3:
            roll = int(input("Enter roll number to delete: "))
            if roll in students:
                del students[roll]
                print(students)
            else:
                print("Student roll number is invalid or not registered.")
                
        case 4:
            roll = int(input("Enter roll number to search: "))
            if roll in students:
                print("Search Found: ", students[roll])
            else:
                print("Student not found.")
                
        case 5:
            print("Existing program. All data will be lost.")
            break;
            
        case _: 
            print("Invalid choice..")
