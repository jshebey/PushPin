from part import Part
import pandas as pd
import openpyxl as xl

class Scrub:
    def __init__(self, bom_file):
        self.bom_file = bom_file
        self.df = pd.read_excel(bom_file)

    def process_bom(self):
        #Loops over every part in the BOM
        for index, row in self.df.iterrows():
            schematicLabel = row['Schematic']
            #Grabs the part name
            partName = row['Part Number']
            #Creates a part object
            part = Part(partName)
            #Determines if part is a resistor, capacitor, or neither
            if(schematicLabel[0] == 'R'):
                res_manufacturer = part.find_res_manufacturer()
                if(res_manufacturer == "YAGEO (RC_L Series)"):
                    part.yageo_RC_L_decode()
                elif(res_manufacturer == "Kamaya (FRC Series)"):
                    part.kamaya_FRC_decode()
                elif(res_manufacturer == "Susumu (RR Series)"):
                    part.susumu_RR_decode()
                elif(res_manufacturer == "Bourns (CRM Series)"):
                    part.bourns_CRM_decode()
                elif(res_manufacturer == "KOA (RK73H Series)"):
                    part.koa_RK73H_decode()
                else:
                    part.res_decode()
                #Outputs the decoded part values on the Excel sheet
                part.display_info(index)
            elif(schematicLabel[0] == 'C'):
                cap_manufacturer = part.find_cap_manufacturer()
                if(cap_manufacturer == "KEMET (MLCC Series)"):
                    part.kemet_MLCC_decode()
                elif(cap_manufacturer == "Meritek (MA Series)"):
                    part.meritek_MA_decode()
                elif(cap_manufacturer == "TDK (C Series)"):
                    part.tdk_C_decode()
                elif(cap_manufacturer == "AVX (KAM Series)"):
                    part.avx_KAM_decode()
                elif(cap_manufacturer == "Darfon (MLCC Series)"):
                    part.darfon_MLCC_decode()
                else:
                    part.cap_decode()
                #Outputs the decoded part values on the Excel sheet
                part.display_info(index)
            else:
                print("NOT PART")