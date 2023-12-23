print(f"\033[1m{'Welcome to the Secret Auction Program':-^50}\033[0m")

list_of_bids = {}


def bids(name, bid):
    list_of_bids[name] = bid


while True:

    name = input("What's your name?: ")
    price = int(input("What's your bid?: $"))
    bids(name, price)

    more = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more == "no":
        break

bigger_bidder = ''
bigger_bid = 0

for num, person in enumerate(list_of_bids):
    if num == 0:
        bigger_bidder = person
        bigger_bid = list_of_bids[person]
    else:
        if bigger_bid < int(list_of_bids[person]):
            bigger_bidder = person
            bigger_bid = list_of_bids[person]

print(f"The winner is {bigger_bidder} with a bid of ${bigger_bid}")
