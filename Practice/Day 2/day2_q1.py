marks = []

while True:
    print("\n\nSTUDENTS MARKS MENU")
    print("1.Add Marks \n2.Delete Marks \n3.Average & Highest \n4.Exit")
    
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            mark = int(input("Enter your marks to add: "))
            marks.append(mark)
            print("Mark", mark, "added sucessfully \nFinal Marks: ", marks)
            
        case 2:
            if not marks:
               
                print("No marks to delete: ")
            else:
               print("Marks: ", marks)
               mark = int(input("Enter your marks to delete: "))
               if mark in marks:
                   marks.remove(mark)
                   print("Mark", mark, "deleted sucessfully \nFinal Marks: ", marks)
               else:
                   print("Mark not found")
                   
        case 3:
            if not marks:
                print("No marks available")
            else:
                avg = sum(marks)/len(marks)
                highest = max(marks)
                print("Marks: ", marks)
                print("Highest: ", highest)
                print("Average: ", avg)
                
        case 4:
           print("Exiting program.")
           break
       
        case _:
            print("Invalid choice. Try again.")
            
                   
        
