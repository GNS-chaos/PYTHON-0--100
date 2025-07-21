programmif={"bug":"run"}

print(programmif["bug"])

empty={}

empty={"uno":"1"}

print(empty)

#to wipe existed_dic={}

programmif["za"]="ne?"

print(programmif)

#nesting
capitals={
    "France":"Paris",
    "germany":"berlin"
}
travel_log= {
    "francee": ["paris", "lil", "dijon"],
    "germanyy": ["köln","berlin", "sttutgard"],
}

print(travel_log["germanyy"][0])
nested_list=["a", "b", ["c","d"]]

#print("\n" *100) to clean the screen xd
#name: key, bid:value

#blind auct,on

def find_highest_bidder(biddding_dict):
    highest_bid=0
    winner=""
    max(biddding_dict)

    for bidder in biddding_dict:
        bid_amount=biddding_dict[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"winner is {winner} and the bid is {highest_bid}!!")
    

bids={} 

continue_bidding=True
while continue_bidding:
    name=input("Whats your name: ")
    price=int(input("whats your bid: "))
    bids[name]=price
    
    should_continue=input("are there any bidders? y or n: \n").lower()
    if should_continue=="n":
        continue_bidding=False
        find_highest_bidder(bids)
    elif should_continue=="y":
        print("\n"*100)
        
