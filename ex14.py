import random

# Lottery Simulation

ticket_price = 10
winning_number = random.randint(1, 10)

user_number = int(input("Choose a number (1-10): "))

print("Winning Number:", winning_number)

if user_number == winning_number:
    print("🎉 You won 50!")
    profit = 50 - ticket_price
else:
    print("😢 You lost")
    profit = -ticket_price

print("Profit/Loss:", profit)
