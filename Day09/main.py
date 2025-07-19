import art
print(art.logo)
bidding = {}
run="True"
while run:
    name=input("Bidder's Name:\n")
    bid=int(input("Your Bid:\n"))
    bidding[name] = bid
    ask=input("Any more bidders?  Yes/No\n").lower()
    if ask == "yes":
        print("\n"*30)
    elif ask == "no":
        break
    else:
        print("\n"*30)
        print("Write a valid choice --> By Default:Yes")
bid_list = []
for bidder in bidding:
    bid_list.append(bidding[bidder])
for key in bidding:
    if bidding[key] == max(bid_list):
        print("\n" * 30)
        print(f"The top bidder was:  {key} ---> {bidding[key]} Primogems!!")