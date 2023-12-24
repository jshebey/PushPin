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
                part.find_res_data()
                part.res_decode()
                #Outputs the decoded part values on the Excel sheet
                #part.display_info(index)
            elif(schematicLabel[0] == 'C'):
                part.find_cap_data()
                part.cap_decode()
                #Outputs the decoded part values on the Excel sheet
                #part.display_info(index)
            else:
                print("NOT PART")