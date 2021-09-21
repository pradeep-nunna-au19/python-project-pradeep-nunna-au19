from d_registration import cabdriver
from rider_registration import cabrider
from distance import distance
from wlcome import welcome
from reachpoint import destination

if __name__ == "__main__":
    opening=welcome()
    hackman=cabdriver()
    passenger=cabrider()
    DriverCount= 1
    for k in range(DriverCount):
        NAME=input("Please Add your Name: ")
        CAB_NUMBER=input("Please Enter your Cab_NUMBER: ")
        PH_NUMBER=input("Please Enter your PH_NUMBER: ")
        AVAILABLE=input("Press<YES> if you are available else <NO>: ")
        print("Enter your location Co_ordinates: ")
        a1= int(input("Enter of X Co_ordinates: "))
        a2= int(input("Enter of Y Co_ordinates: "))
        Driver=hackman.driver_info(NAME,CAB_NUMBER,PH_NUMBER,AVAILABLE,a1,a2)
        print("Your Details", Driver)

        NAME=input("Type Your NAME: ")
        LOCATION=input("Enter Your Place: ")
        PH_NO=input("Your Mobile Number: ")
        BOOKING=input("Type <YES> if you want a ride: ")
        b1=int(input("Type your x Co_ordinates: "))
        b2=int(input("Type your y Co_ordinates: "))

        Rider=passenger.rider_info(NAME,LOCATION,PH_NO,BOOKING,b1,b2)
        print("Your Details:", Rider)
    allriders= passenger.HistoryRides()
    print("cab types <low>, <medium>, <high> ")

    entry = input("Provide your Input here: ")
    if entry == "low" or entry == "medium" or entry == "high":
        print("pls enter the destination point:")
        d1=int(input("enter x co_ordinates: "))
        d2=int(input("enter y co_ordinates: "))
        space=9999999999
        cab_registered=None
        for i in range(DriverCount):
            d=distance(a1, a2, b1, b2)
            print("Driver is ", 'NAME',"is", d ,"KM from you")
            if d < space:
                space=d
            cab_registered=Driver.get(NAME)
            print(cab_registered, "will pick at your pointed location shortly")
            print("Welcome....Have a safe journey")


            for j in range(len(allriders)):
                l= destination(allriders[0]["b1"], allriders[0]["b2"], d1, d2)
            print("Arrived to your Destination point")

            if entry == "low":
                amount = 3
                print("Pay the Amount of Rs. ", l*amount*(d/10))
            elif entry == "medium":
                amount = 4
                print("Pay the Amount of Rs. ", l*amount*(d/10))
            elif entry == "high":
                amount=6
                print("Pay the Amount of Rs. ", l*amount*(d/10))

    while True:
        print("To see history of all your Rides type<check>: ")
        print("To quit type <EXIT>: ")

        entry = input("Provide you Input here: ")

        if entry == "check":
            print(allriders)

        if entry == "EXIT":
            print("Thank You, visit Again!")
            break