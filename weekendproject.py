class Mortgage():

    def __init__(self):
        self.price_of_property = float(input('how much did you pay for the house?: '))
        self.rental_income = float(input('how much are you going to charge for rent?: '))
        self.expenses = float(input('what are your monthly expenses?: '))
        self.return_on_investment = 0

    def income(self):
       return (self.rental_income * 12)-self.expenses 
    
        
    def roi(self):
        annual_net_income = self.income()
        return(annual_net_income / self.price_of_property)
    

investment_property = Mortgage()

investment_property.return_on_investment = investment_property.roi()*100

print(f"Property Price: {investment_property.price_of_property}")
print(f"Rental Income: {investment_property.rental_income}")
print(f"Expenses: {investment_property.expenses}")
print(f"Cashflow: {investment_property.income()}")
print(f"Return on Investment (ROI): {investment_property.return_on_investment:.2f}%")