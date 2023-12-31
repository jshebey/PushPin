from scrub import Scrub

def main(boms):
    rowTotal = 0
    #Each BOM that was entered through the GUI gets processed
    for bom in boms:
        currFile = str(bom)
        currBom = Scrub(currFile, rowTotal)
        currBom.process_bom()
        rowTotal += currBom.rowCount
    
    currBom.partList.close()
        

if __name__ == "__main__":
    main()