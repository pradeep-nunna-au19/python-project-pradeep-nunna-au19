class cabdriver:
    def __init__(self):
        self.driver=[]
    def driver_info(self,NAME, CAB_NUMBER, PH_NUMBER, AVAILABLE, LOCATION_a1, LOCATION_a2):
        Driver={"NAME":NAME, "CAB_NUMBER":CAB_NUMBER,"PH_NUMBER":PH_NUMBER, "AVAILABLE":AVAILABLE, "a1":LOCATION_a1, "a2":LOCATION_a2}
        self.driver.append(Driver)
        return Driver

