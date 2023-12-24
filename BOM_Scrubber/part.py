class Part:
    def __init__(self, part_number):
        self.part_number = part_number
        self.manufacturer = None
        self.resistance = None
        self.capacitance = None
        self.tolerance = None
        self.voltage = None
        self.size = None
        self.power = None
        self.dielectric = None

    def find_res_manufacturer(self):
        pass

    def find_cap_manufacturer(self):
        pass

    def res_decode(self):
        pass

    def cap_decode(self):
        pass
    
    def yageo_RC_L_decode(self):
        pass

    def kamaya_FRC_decode(self):
        pass

    def susumu_RR_decode(self):
        pass

    def bourns_CRM_decode(self):
        pass

    def koa_RK73H_decode(self):
        pass

    def kemet_MLCC_decode(self):
        pass

    def meritek_MA_decode(self):
        pass

    def tdk_C_decode(self):
        pass

    def avx_KAM_decode(self):
        pass

    def darfon_MLCC_decode(self):
        pass

    def display_info(self):
        # Add a method to display information about the part
        print(f"Part Number: {self.part_number}")
        # Print other decoded information