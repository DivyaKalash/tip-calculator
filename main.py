

bill = input("Hii...!, What's the total bill ?")
tip = input("How much tip percentage you guys waana give?")
persons = input("In how many persons you guys wanna split the bill?")

total_bill = float(bill) + (float(bill) * (float(tip) / 100))
bill_person = round(total_bill / int(persons), 2)
print(f"Each Person need to pay {bill_person}.")
