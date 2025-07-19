
# 1
def AddExpense():
    # Print output for the user
    print("Adding Expense")
    # Collect information on expense
    dateExp = input("Date of the expense in 'YYYY-MM-DD' format")
    CatExp = input("Category of Expense")
    AmtExp = input("Amount Spent")
    DescExp = input("Description of Expense")
    # Format input as dictionary
    OutDict = {'date':dateExp, 'category':CatExp, 'amount':AmtExp, 'description':DescExp}
    # Return result
    return OutDict

def ViewExpense(filename):
    # Call function that loads expenses from file (described with point 4)
    HistoricalExp = LoadExpenses(filename)
    # Print Expenses
    print(HistoricalExp)

def GetMonthlyBudget(filename):
    # print current month for user
    
    # prompt user to input a monthly budget

    # Call TotalHistoricalExpenses

def TotalHistoricalExpenses(filename):
    # Load expenses from file

    # Total expenses for month

    # Display warning if budget exceeded, and remaining balance if expenses less than budget (ifelse block)

def SaveExpenses(filename, newExpense):
    # Save expenses out to file

def LoadExpenses(filename):
    # Load historical expenses from file

def InteractiveMenu(filename):
    print("You may select one of the following options:\nAdd expense \nView expenses \nTrack budget \nSave expenses \nExit")
    UserInput = input("Option")
    if UserInput == 'Add expense':
        NewExpense = AddExpense()
    elif UserInput == "View expenses":
        ViewExpense(filename)
    elif UserInput== "Track budget":
        GetMonthlyBudget(filename)
    elif UserInput == "SaveExpenses":
        try:
            SaveExpenses(filename, NewExpense)
        except:
            print("Issue saving expenses")
    elif UserInput=="Exit":
        global exitStat+=1
    else: 
        "Did not input option correctly"

exitStat=0
while exitStat==0:
    InteractiveMenu("myfile.txt")