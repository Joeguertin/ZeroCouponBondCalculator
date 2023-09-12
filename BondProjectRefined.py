# Program to calculate if zero-coupon bonds are worth purchasing


def calculate_present_value(future_value, discount_rate, compounding_periods, years):
    #Calculate the bond value based on parameters
    present_value = future_value / (compounding_periods + discount_rate)**(years)
    return present_value

def purchase_bond_check():
    # Bond parameters
    while True:
        try:
            future_value = float(input("Enter the bond's future value: "))
            discount_rate = float(input("Enter the bond's discount rate: "))
            compounding_periods = 1
            years = int(input("Enter the number of years until the bond matures: "))

            # Calculate the present value of the bond and assign returned value to bond_value
            bond_value = round(calculate_present_value(future_value, discount_rate, compounding_periods, years),2)
            print(f"Your current zero-coupon bond value: {bond_value:.2f}")

            # Compare bond value to price and make decision
            price = float(input("Enter the bond's price: "))
            if bond_value < price:
                print("Do not purchase bond")
            # Premium 2% or greater price comparison
            # Calulate the percentage increase and f string the variable into a premium price alert
            elif bond_value - (bond_value*.02) > price:
                find_percent_decrease=int((bond_value - price) / bond_value * 100)
                print(f"Price premium alert 2% threshold met! Bond is {find_percent_decrease}% discount. ")
            # Regular bond alert
            elif bond_value > price:
                print("Purchase bond")
            # Neutral
            else:
                print("Neutral to purchasing bond")
            break
        except ValueError:
            print("Invalid input. Please try again.")
purchase_bond_check()
