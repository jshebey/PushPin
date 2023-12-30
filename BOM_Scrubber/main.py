from scrub import Scrub

def main(file):
    bom_file = str(file)
    bom = Scrub(bom_file)
    bom.process_bom()

if __name__ == "__main__":
    main()