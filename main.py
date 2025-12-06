# Expense tracker project:
expenses_list=[] 
print("Welcome to Expense Tracker: kam kharcha karo")
while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View total Expenses")
    print("4. Exit")
    
    choice=int(input("Please enter your choice: "))
    
    if choice==1:
        date=input("Please enter the date: ")
        category=input("Enter type/category of expenses: (food,travel,shopping,etc): ")
        description=input("Enter the details about the expenses: ")
        amount=float(input("Enter the amount: "))
        
        expense={
            "date": date,
            "category":category,
            "description":description,
            "amount":amount
            
        }
        expenses_list.append(expense)
        print("\n DONE BROTHER. Expenses Added Succesfully")
    
    elif choice==2:
        if (len(expenses_list)==0):
            print("No expenses are added !!")
        else:
            print("====HERE ARE YOUR ALL EXPENSES====")
            count=1
            for kharcha in expenses_list:
                print(f"kharcha number {count} ->{kharcha["date"]},{kharcha["category"]},{kharcha["description"]},{kharcha["amount"]}")
                count+=1
                
    elif choice==3:
        total=0
        for kharcha in expenses_list:
            total=total+ kharcha["amount"]
        
        print("\n TOTAL EXPENSES= ",total)
        
    elif choice==4:
        print("THANKS FOR USING MY EXPENSES TRACKER")
        break
    
    else:
        print("INVALID CHOICE !!! TRY Again bro !!.......... ")
    
    
        
        