import os 
from time import sleep

class Roi_Calculator():

    def __init__(self, income, expenses, cashflow, investment, roi):
        self.income = income
        self.expenses = expenses
        self.cashflow = cashflow
        self.investment = investment
        self.roi = roi

    # User adds up and inputs expected monthly income
    def input_income(self):
        self.income = input("\nFirst, we'll look at your expected monthly income. \n\
\nConsider the rental income, plus any additional income from things like washing machines, storage, etc. \n\
\nEnter the total monthly income you expect from this property and then press 'Enter':  \n")
        # total monthly income = 2000

    # User adds up and inputs expted monthly expenses
    def input_expenses(self):
        self.expenses = input(f"Your expected monthly income from this property is ${self.income}. \n\
\nNext, we'll look at your expected monthly expenses. \n\
Consider all of your monthly expenses: taxes, insurance, utilities (e.g. electric, water, sewage, garbage, gas), \n\
HOA fees,lawn/snow care, vacancy, capital expenditures, repairs, property management, mortgage, etc. \n\
\nAdd all of those up and enter your monthly expenses and then press 'Enter': ")
        # total monthly expenses = 1610

    # Add up and return monthly and annual cash flow to the user
    def cash_flow(self):
        self.cashflow = int(self.income) - int(self.expenses)
        # total monthly cash flow = 390

    def get_investment(self):
        print(f"\nYour expected monthly cash flow is ${self.cashflow}.\n\
\nNext, we'll figure out if this property is worth it when we consider your investment in the property.")
        self.investment = input("\nConsider your investment: down payment, closing costs, repair budget, miscellaneous. \n\
Enter your total investment: ") 
        # total investment = 50,000

    def determine_roi(self):  
        annual_cash_flow = int(self.cashflow) * 12
        # annual cash flow = 4680  
        self.roi = (annual_cash_flow / int(self.investment)) * 100
        # 4680 / 50,000 = 9.36%
        os.system('clear')
        print(f"\nYour Cash-on-Cash ROI is {self.roi}%.\n")

brandon = Roi_Calculator("income", "expenses", "cashflow", "investment", "roi")

def run():
    print("\nWelcome to the Rental Property ROI Calculator.\n")
    sleep(3)
    os.system('clear')
    brandon.input_income()
    while brandon.income.isdigit() != True:
        brandon.income = input("Please try re-entering the amount of monthly income you expect from this property. ")
    os.system('clear')
    brandon.input_expenses()
    while brandon.expenses.isdigit() != True:
        brandon.expenses = input("Please try re-entering the amount of monthly expenses you expect from this property. ")
    os.system('clear')
    brandon.cash_flow()
    brandon.get_investment()
    while brandon.investment.isdigit() != True:
        brandon.investment = input("Please try re-entering your investment in this property. ")
    brandon.determine_roi()
    sleep(5)
    os.system('clear')

run()