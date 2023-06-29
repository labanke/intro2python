#create a simple reward system
#use any number 1-5
#they are rewarded

reward = int(input("Enter reward token number"))

if reward == 1:
    print("Reward is a phone")
elif reward == 2:
    print("Reward is a Bike")
elif reward == 3:
    print("Reward is Ksh. 200")
elif reward == 4:
    print("Reward is a Voucher gift card")
elif reward == 5:
    print("Reward is a car")
else:
    print("invalid reward token")