'''
Building a Expense Tracker
    - Learnt using lambda functions in Python
        - Lambda Functions are brief, anonymous functions in Python
            - Ideal for simple and one-time tasks
        - Syntax: lambda x: expr, where 'x' -> parameter and 'expr' -> expression
        - Example: lambda x: x ** 2 -> returns the square of the input
'''
def add_expense(expenses, amount, category):
    # Append a dictionary to the list of expenses
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: ${expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    # Using a lambda function add up all the amounts in the list of expenses
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    # Using a lambda function to identify and filter the expenses by category
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = []
    
    while True:
        print('\nExpense Tracker')
        print('1. Add Expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: $'))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
        elif choice == '3':
            print('\nTotal Expenses: $', total_expenses(expenses))
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        elif choice == '5':
            print('Exiting the program.')
            break

if __name__ == '__main__':
    main()
