# Task 1: Define Budget Category Class
class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name           # Private for the category name
        self.__budget = budget       # Private for the budget

    # Task 2: Getters and Setters

    # Getter for the category name
    def get_name(self):
        return self.__name

    # Setter for the category name
    def set_name(self, new_name):
        self.__name = new_name

    # Getter for the budget
    def get_budget(self):
        return self.__budget

    # Setter for the budget with validation
    def set_budget(self, new_budget):
        if new_budget > 0:
            self.__budget = new_budget
        else:
            print("Budget must be a positive number.")

    # Task 3: Add Budget Functionality

    # Method to add an expense
    def add_expense(self, amount):
        if amount <= self.__budget:
            self.__budget -= amount
            print(f"{amount} has been deducted. Remaining budget: {self.__budget}")
        else:
            print("Expense exceeds the available budget.")

    # Task 4: Display Budget Details

    # Method to display the budget category details
    def display_category_summary(self):
        print(f"Category: {self.__name}")
        print(f"Initial Budget: {self.__budget}")
        print(f"Remaining Budget: {self.__budget}")

# Usage example
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()