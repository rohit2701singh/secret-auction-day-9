bidders_dict = {}


def bid_winner():
    highest_bid = 0
    winner = ""
    for bidder in bidders_dict:
        if bidders_dict[bidder] > highest_bid:
            highest_bid = bidders_dict[bidder]
            winner = bidder
    print(f"\nall bidders: {bidders_dict}")
    print(f"The winner is '{winner}' with a bid of ₹ {highest_bid}.")


bids_complete = False
while not bids_complete:
    print("Welcome to the secret auction program.")
    name = input("what is your name? ")
    amount = int(input("type your bid amount ₹ "))
    bidders_dict[name] = amount

    other_bidders = input("are there any other bidders? type 'yes or no'\n").lower()
    if other_bidders == "no":
        bids_complete = True
        bid_winner()
    elif other_bidders == "yes":
        continue
    else:
        bids_complete = True
        print("wrong choice, rerun program.")
