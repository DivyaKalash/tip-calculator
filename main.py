#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

bill = input("Hii...!, What's the total bill ?")
tip = input("How much tip percentage you guys waana give?")
persons = input("In how many persons you guys wanna split the bill?")

total_bill = float(bill) + (float(bill) * (float(tip) / 100))
bill_person = round(total_bill / int(persons), 2)
print(f"Each Person need to pay {bill_person}.")
