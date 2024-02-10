# Get input from the user
NS = 2000  # Number of shares
BP = 40.00  # Buying price per share
BC_rate = 0.03  # Buy commission rate
SP = 42.75  # Selling price per share
SC_rate = 0.03  # Selling commission rate

# Calculate amounts
buy_amount = NS * BP  # Amount Joe paid for the stock
buy_commission = buy_amount * BC_rate  # Commission Joe paid when buying the stock

sell_amount = NS * SP  # Amount Joe received for selling the stock
sell_commission = sell_amount * SC_rate  # Commission Joe paid when selling the stock

# Calculate total amount after selling and paying commissions
total_amount = sell_amount - sell_commission - (buy_amount + buy_commission)

# Display the information
print("1. Amount Joe paid for the stock:", buy_amount)
print("2. Commission Joe paid his broker when he bought the stock:", buy_commission)
print("3. Amount for which Joe sold the stock:", sell_amount)
print("4. Commission Joe paid his broker when he sold the stock:", sell_commission)
print("5. Amount of money Joe had left after selling the stock and paying commissions:", total_amount)

# Determine if Joe made a profit or loss
if total_amount > 0:
    print("Joe made a profit.")
elif total_amount < 0:
    print("Joe incurred a loss.")
else:
    print("Joe broke even.")
