class cabrider:
    def __init__(self):
        self.rider=[]
    def rider_info(self,NAME,LOCATION,PH_NO,BOOKING,LOCATION_b1,LOCATION_b2):
        Rider={"NAME":NAME,"LOCATION":LOCATION,"PH_NO":PH_NO,"BOOKING":BOOKING,"b1":LOCATION_b1,"b2":LOCATION_b2}
        self.rider.append(Rider)
        return Rider

    def HistoryRides(self):
        print("HISTORY")
        return self.rider