amount = float(input("What is the total amount to be paid?: $"))
tip = int(input("What percentage tip would you like to give? Enter number: "))
num_people = int(input("How many people to split the amount?: "))

ans = (amount / num_people) * tip/100 + (amount / num_people)

print(f"Each person should pay: ${float(ans):.2f}")