from part import Part
import pandas as pd
import openpyxl as xl

class Scrub:
    def __init__(self, bom_file):
        self.bom_file = bom_file
        self.df = pd.read_excel(bom_file)
        self.parts = []

    def process_bom(self):
        #Loops over every part in the BOM
        for index, row in self.df.iterrows():
            schematicLabel = row['Schematic']
            if(schematicLabel[0] == 'R' or schematicLabel[0] == 'C'):
                #Grabs the part name
                partName = row['Part Number']
                #Creates a part object
                part = Part(partName)
                #Determines the part's characteristics
                part.decode()
                #Outputs the decoded part values on the Excel sheet
                part.display_info()
            else:
                print("NOT PART")

    def display_parts_info(self):
        for part in self.parts:
            part.display_info()