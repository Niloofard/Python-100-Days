bid_amount = {}

more_bids= "Yes"
while more_bids== "Yes":
    name= input("What is your name? ")
    bid_amount[name] = int(input("What is your bid? "))
    more_bids= input("Are There any Other Bidders? Type Yes or No: ")
    print("\n" * 100)

max_bid= 0
for name in bid_amount:
    if bid_amount[name] > max_bid:
        max_bid= bid_amount[name]
print("max bid is: ", max_bid)
