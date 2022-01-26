import art
print(art.logo)
def cls():
    print('\n'*50)
bids = {}
bidding_finished = False

def find_highest_bidder(bidders):
    highest = 0
    for bidder in bidders:
        if bidders[bidder]>highest:
            highest = bidders[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest}")
while not bidding_finished:
    name = input("Please enter your name\n")
    bid = int(input("What is your bid?\n $"))
    should_continue = input("Are there any other people who want to bid? Type 'yes' or 'no'\n").lower()
    bids[name] = bid
    if should_continue == 'no':
        bidding_finished = True
        cls()
        find_highest_bidder(bids)
    else:
        cls()


