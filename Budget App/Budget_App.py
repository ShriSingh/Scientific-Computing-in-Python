'''Building a Budget app project'''


class Category:
    '''
    Should present:
    -> A initial deposit of funds for separate expense 
    categories like food, clothing, and entertainment etc.
    -> Money withdrawn from deposited fund from a category
    -> Total amount of money spent in each category
    -> A bar chart to show the percentage of money spent in each 
    category
    '''

    def __init__(self, s):
        """
        Creating a Category class with a constructor 
        that takes in a category name and creates a ledger 
        list to store the amounts of each deposit or withdrawal.

        :param s: str
        :return: None
        """
        # Creating a Category class with a constructor
        self.category = s
        # Creating a ledger list to store the amounts of each deposit or withdrawal
        self.ledger = []

    def get_balance(self) -> float:
        """
        Calculating the total amount in the ledger list
        
        Returns:
            :float: total amount in the ledger list
        """
        total = 0
        # Going through the ledger list
        for item in self.ledger:
            # Adding up sum of the amount
            total += item["amount"]

        return total

    def check_funds(self, amnt) -> bool:
        """
        Checking if the amount is less than the total amount
        
        Args:
            :amount float: amount to be checked
        
        Returns:
            :bool: True if amount is less than the total amount
        """
        # Checking if the amount is less than the total amount
        fund_checking = self.get_balance() >= amnt

        return fund_checking

    def deposit(self, amnt, desc="") -> None:
        """
        Adding a dictionary to the ledger list with the amount
        deposited with its description.

        Args:
            :amount float: amount to be deposited
            :desc str: description of the deposit
        """
        # Adding a deposit to the ledger list in dictionary form
        self.ledger.append({"amount": amnt, "description": desc})

    def withdraw(self, amnt, desc="") -> bool:
        """
        Adding a dictionary to the ledger list with the amount
        withdrawn with its description.

        Args:
            :amount float: amount to be withdrawn
            :desc str: description of the withdrawal
        """
        # Checking if the amount is less than the total amount
        if self.check_funds(amnt):
            # Adding a withdraw to the ledger list in dictionary form
            # Adding the label of the amount with '-' prefix to indicate withdrawal
            self.ledger.append({"amount": -amnt, "description": desc})
            return True

        return False

    def transfer(self, amnt, catgry) -> bool:
        """
        Adding a dictionary to the ledger list with the amount
        transferred with its description.

        Args:
            :amount float: amount to be transferred
            :category str: category to transfer the amount
        
        Returns:
            :bool: True if amount is transferred
        """
        # Checking if the amount transferred is less than the total amount
        if self.check_funds(amnt):
            # Calling withdrawal and deposit methods to transfer the amount
            self.withdraw(amnt, f"Transfer to {catgry.category}")
            catgry.deposit(amnt, f"Transfer from {self.category}")

            return True

        return False

    def __str__(self):
        """
        Displaying the category name, the ledger list, 
        and the total amount in the ledger list.

        Returns:
            :str: category name, ledger list, and total 
            amount in the ledger list
        """
        # Putting the title of the budget in the bill
        bill = self.category.center(30, "*") + "\n"
        # Printing the ledger list
        for i in self.ledger:
            bill += f'{i["description"][:23]:23}' + f'{i["amount"]:7.2f}' + '\n'

        # Printing the total list
        bill += f'Total: {self.get_balance():.2f}'

        return bill

def create_spend_chart(catgries: list) -> str:
    """
    Function to create a bar chart which shows
    the percentage of money spent in each category

    Args:
        :catgries list: list of categories

    Returns:
        :chart str: bar chart showing the percentage of money spent
    """
    chart = "Percentage spent by category\n"

    # Getting the total amount of money spent
    withdrawals = []
    for cat in catgries:
        total_withdrawal = 0
        for i in cat.ledger:
            amount = i["amount"]
            if amount < 0:
                total_withdrawal += amount
        withdrawals.append(-total_withdrawal)

    # Getting the percentages of money spent
    percent_withrawals = []
    for i in withdrawals:
        percentage = round(i / sum(withdrawals) * 100)
        percent_withrawals.append(percentage)

    # Getting the names of the categories
    names = []
    for cat in catgries:
        name = cat.category.lower().capitalize()
        names.append(name)

    # Creating the bar chart
    # Adding y-axis
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percent_withrawals:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Adding x-axis
    chart += (" " * 4) + ("-" * (3 * (len(catgries)) + 1))
    max_length = len(max(names, key=len))
    axis_names = []
    for i in names:
        adj_spacing = i.ljust(max_length)
        axis_names.append(adj_spacing)

    # Adding x-axis labels
    for i in range(max_length):
        chart += "\n     "
        for name in axis_names:
            chart += name[i] + "  "

    return chart


if __name__ == "__main__":
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    auto = Category('Auto')
    auto.deposit(1000, 'initial deposit')
    auto.withdraw(15)

    print(food)
    print(clothing)
    print(create_spend_chart([food, clothing, auto]))
