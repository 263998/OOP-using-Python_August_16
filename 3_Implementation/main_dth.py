"""module"""

import dth


while True:
    choice = input(" Do you want to check your monthly DTH rent enter yes or no : ")
    if choice == "yes":
        print("----------------Hey Welcome on this page for knowing your DTH plan-----------------")
        print("--------------- please follow instruction and select your choice -----------------")
        name = input(" enter your name : ")
        print(" Enter 1 --> for Silver \n Enter 2 --> for Gold \n Enter 3 --> for Platinum")
        pack_choice = int(input(" Choose your choice from above options : "))
        if pack_choice == 1:
            #base_pack = "Silver"
            BASE_PACK = "Silver"
        elif pack_choice == 2:
            #base_pack = "Gold"
            BASE_PACK = "Gold"
        elif pack_choice == 3:
            #base_pack = "Platinum"
            BASE_PACK = "Platinum"
        else:
            #base_pack = "invalid"
            BASE_PACK = "invalid"
        sub_period = int(input(" Enter subscription period in months (between 1 and 24) : "))
        if 12 < sub_period <= 24:
            print(" --------------Congratulations you are eligible for discount---------------")
        elif sub_period > 24 or sub_period <= 0:
            print("--------------Invalid subscription period please enter valid period------------")
        else:
            print("----------As your subscription plan is below 12 months so no discount----------")
        obj1 = dth.BasePackage(name, BASE_PACK, sub_period)
        print("----------------According to choice following is your plan-----------------")
        print("\t Name of customer as entered : ", obj1.get_consumer_name())
        print("\t Base pack chosen : ", obj1.get_base_pack_name())
        print("\t Subscription period chosen : ", obj1.get_subscription_period())
        print("\t Monthly rent according to chosen choice : ", obj1.calculate_monthly_rent())
    else:
        break
