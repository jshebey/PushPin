from part import Part

class Scrub:
    def __init__(self, bom_file):
        self.bom_file = bom_file
        self.parts = []

    def process_bom(self):
        # Add logic to read the BOM file, create Part objects, and store them in self.parts
        # Example: Read the BOM file line by line, create Part objects, and append to self.parts
        pass

    def display_parts_info(self):
        for part in self.parts:
            part.display_info()