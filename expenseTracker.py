import datetime

def addExpense(expences,catagory,amount):
    currentDate=datetime.date.today    #give us the current date 2nd feb
    expense={"catagory":catagory,"amount":amount,"date":currentDate}
    expences.append(expense)
    print("expense added succesfully")

def viewExpense(expences):
    if not expences:      #if the expenses list is empty
        print("NO Expences!")
    else:
        print("expences: ")
        # 1. catagory: study amount: 100$ date:1 feb
        for index,expence in enumerate (expences,start=1):
            print(f"{index}. catagory: {expence['catagory']}, amount: RS {expence['amount']},Date: {expence['date']}")

def CalculateTotal(expences):
    total=sum(expense['amount'] for expense in expences)
    print(f"total expence: RS{total}")

def main():
    expences=[]

    while True:
        print("WELCOME TO EXPENSE TRACKER MENU \n Press 1 to add expense \n Press 2 to View Your expence \n Press 3 to view total amount of expences \n press 4 to exit")   
        choice=input("enter your choice")

        if choice=="1":
            catagory=input("enter catagory: ")
            amount=float(input("enter Amount: "))
            addExpense(expences,catagory,amount)

        elif choice=="2":
            viewExpense(expences)

        elif choice=="3":
            CalculateTotal(expences)
        elif choice=="4":
            print("Exiting from the Expense Tracker Menu GOODBYE!")
        else:
            print("invalid input: ")

if __name__=="__main__":
    main()
