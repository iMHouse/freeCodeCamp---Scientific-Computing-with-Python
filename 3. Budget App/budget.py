class Category:

  #categoryName = ""
  #ledger = []

  #balance = 0

  def __init__(self, categoryName, ledger=None, balance=0):
    self.categoryName = categoryName
    self.ledger = ledger if ledger is not None else list()
    self.balance = balance

  def __repr__(self):
    return f"Category(categoryName={self.categoryName}, ledger={str(self.ledger)}, balance={self.balance})"

  def __str__(self):
    valueToReturn = self.categoryName.center(30, "*") + "\n"
    for item in self.ledger:
      valueToReturn = valueToReturn + item["description"][:23].ljust(
        23, " ") + str.rjust(F'{item["amount"]:.2f}', 7)[:7] + "\n"

    valueToReturn = valueToReturn + F'Total: {self.balance:.2f}'
    return valueToReturn

  def deposit(self, amount, description=""):
    #assuming that the amount input is a number (integer or decimal)
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def get_balance(self):
    return self.balance

  def withdraw(self, amount, description=""):
    #assuming that the amount input is a number (integer or decimal)

    if self.check_funds(amount):
      amount = -abs(amount)
      self.ledger.append({"amount": amount, "description": description})
      self.balance += amount

      return True

    return False

  def transfer(self, amount, budgetCategory):

    #assuming budgetCategory is of type "Category"
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + budgetCategory.categoryName)
      budgetCategory.deposit(amount, "Transfer from " + self.categoryName)
      return True

    return False

  def check_funds(self, amount):
    if amount > self.balance:
      return False

    return True


def create_spend_chart(categories):
  numberOfColumns = len(categories) * 3 + 4 + 1
  categoriesExpenses = list()

  chart = "Percentage spent by category\n"

  maxCategoryLength = 0

  #calculate the percentages for the chart
  for category in categories:
    categoryExpenses = 0
    for transaction in category.ledger:
      if transaction["amount"] < 0:
        categoryExpenses += abs(transaction["amount"])
    
    if maxCategoryLength < len(category.categoryName):
      maxCategoryLength = len(category.categoryName)
    
    categoriesExpenses.append((categoryExpenses))

  categoriesPercentages = [int(round((categoryExpenses * 100) / sum(categoriesExpenses), 1))//10 for categoryExpenses in categoriesExpenses]

  #create the upper part of the chart
  for scale in range(10, -1, -1):
    chart = chart + str(scale * 10).rjust(3) + "|"

    for categoryPercent in categoriesPercentages:
      if categoryPercent >= scale:
        chart = chart + "o".center(3)
      else:
        chart = chart + " ".center(3)
  
    chart = chart + " \n"

  #create the horizontal line
  chart = chart + ("-" * (len(categories) * 3 + 1)).rjust(numberOfColumns) + "\n"

  #create the lower part of the chart (category names)
  for index in range(maxCategoryLength):
    tempChart = ""
    for category in categories:
      if index < len(category.categoryName):
        tempChart = tempChart + category.categoryName[index].center(3)
      else:
        tempChart = tempChart + " ".center(3)
    
    tempChart = tempChart + " "
    
    chart = chart + tempChart.rjust(numberOfColumns) + "\n"
  

  return chart[:-1]
