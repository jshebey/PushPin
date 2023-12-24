from scrub import Scrub

def main():
    bom_file = "C:/Users/jsheb/PushPin/BOMs/BOM_1.xlsx"
    bom = Scrub(bom_file)
    bom.process_bom()

if __name__ == "__main__":
    main()
