bid_amount = {}

more_bids= "yes"
while more_bids== "yes":
    name= input("What is your name? ")
    bid_amount[name] = int(input("What is your bid? "))
    more_bids= input("Are There any Other Bidders? Type Yes or No: ").lower()
    print("\n" * 100)
#find max
max_bid= 0
for name in bid_amount:
    if bid_amount[name] > max_bid:
        max_bid= bid_amount[name]
print("max bid is: ", max_bid)
