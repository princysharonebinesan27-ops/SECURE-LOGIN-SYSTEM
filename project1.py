print("\n=======EXPENSE MANAGER==========\n")#displaying the title "EXPENSE MANAGER" 
monthly=int(input("\nEnter monthly budget:"))#to get  monthly budget as  an input value from the user
expense1=int(input("\nEnter Expense:"))#to get expense1 amount as an input value from the user
category1=input("\nEnter Expense Category:")#to get the expense category1 from user
expense2=int(input("\nEnter Expense:"))#to get expense2 amount as an input value from the user
category2=input("\nEnter Expense Category:")#to get the expense category2 from user
expense3=int(input("\nEnter Expense:"))#to get expense3 amount as an input value from the user
category3=input("\nEnter Expense Category:")#to get the expense category3 from user
print("\n--------------------------------------------------")
total_expense=expense1+expense2+expense3#getting the total_expense by adding all 3 expense amounts
print("\ntotal_expense:",total_expense)#displaying the total_expense
Remaining=monthly-total_expense#getting the remaining by subtracting monthly amount by total_expense
print("\nRemaining:",Remaining)#displaying the remaining amount
print("\n------------------------------------------------")
print("status:within Budget")#displaying the status as within budget
