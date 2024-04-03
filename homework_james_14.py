# James Carlson 
# Coding Temple - SE FT-144
# Backend Module 4 Lesson 3 Assignment: OOP Principles

import re

### ====== 1. Encapsulation in Personal Budget Management ======
###  === 1.1 Define Budget Category Class ===

class BudgetCategory():
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = self.__allocated_budget
    
###  === 1.2 Implement Getters and Setters ===

    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, new_name):
        # category names can only contain letters
        if re.search(r"^[A-z]+$", new_name):
            old_name = self.__category_name
            self.__category_name = new_name
            print(f"Your {old_name} category has been renamed to \"{self.get_category_name()}\"\n")
        else:
            print("Budget category names cannot be empty, and cannot contain numbers or special characters.")
            print(f"Your {self.get_category_name()} category has not been modified.\n")

    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, new_budget):
        # can only be set to a nonnegative number; otherwise, throws an error
        try:
            if float(new_budget) >= 0:
                self.__allocated_budget = float(new_budget)
                print(f"Allocated budget for {self.get_category_name()} has been updated to ${'{:,.2f}'.format(self.get_allocated_budget())}\n")

                # check that remaining_budget does not exceed allocated budget
                if self.get_remaining_budget() > self.get_allocated_budget():
                    self.set_remaining_budget(self.get_allocated_budget())
                return
            # all failing and and error cases:
            else:
                print("An allocated budget cannot be set to a negative number.")
        except (TypeError, ValueError):
            print("Error: Allocated budget can only be a nonnegative number.")
        except Exception as e:
            print(f"Error: {e}")
        # prints if budget was not updated
        print(f"Allocated budget for {self.get_category_name()} has not been updated.\n")

###  === 1.3 Add Budget Functionality ===

    def get_remaining_budget(self):
        return self.__remaining_budget

    def set_remaining_budget(self, new_amount):
        self.__remaining_budget = new_amount

    # subtract expense from remaining budget, if money is available
    def add_expense(self, expense):
        # can only be set to a nonnegative number; otherwise, throws an error
        try:
            if self.get_remaining_budget() >= float(expense):
                self.set_remaining_budget(self.get_remaining_budget() - expense)
                print(f"${'{:,.2f}'.format(expense)} has been removed from your {self.get_category_name()} budget. ${'{:,.2f}'.format(self.get_remaining_budget())} remains.\n")
                return
            # all failing and error cases:
            else:
                print(f"You cannot afford an expense of ${'{:,.2f}'.format(expense)} with your remaining budget of ${'{:,.2f}'.format(self.get_remaining_budget())}")
        except (TypeError, ValueError):
            print("Error: Expense can only be a nonnegative number.")
        except Exception as e:
            print(f"Error: {e}")
        # prints if budget was not updated
        print(f"Your budget for {self.get_category_name()} has not been updated.\n")

###  === 1.4 Display Budget Details ===

    # print all details for object
    def display_details(self):
        print(f"{self.get_category_name()} Budget:")
        print(f"Allocated Budget: ${'{:,.2f}'.format(self.get_allocated_budget())}")
        print(f"Remaining Budget: ${'{:,.2f}'.format(self.get_remaining_budget())}\n")



### === Test Cases ===
        
clothes_budget = BudgetCategory("Clothes", 100)
entertainment_budget = BudgetCategory("Entertainment", 40)
food_budget = BudgetCategory("Food", 140)
print()

# testing set_category_name()
clothes_budget.set_category_name("1337")
entertainment_budget.set_category_name("")
food_budget.set_category_name("Groceries")

# testing set_allocated_budget()
clothes_budget.set_allocated_budget("eighty bucks")
entertainment_budget.set_allocated_budget(-20)
entertainment_budget.set_allocated_budget(0)
food_budget.set_allocated_budget(120)

# testing add_expense()
clothes_budget.add_expense(34.86)
clothes_budget.add_expense(23.33)
entertainment_budget.add_expense(69.99)
food_budget.add_expense("two double cheeseburgers")

# printing party
clothes_budget.display_details()
entertainment_budget.display_details()
food_budget.display_details()