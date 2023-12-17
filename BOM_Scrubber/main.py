from scrub import Scrub

def main():
    bom_file = "path/to/your/bom_file.txt"
    bom_processor = Scrub(bom_file)
    bom_processor.process_bom()
    bom_processor.display_parts_info()
    #git test

if __name__ == "__main__":
    main()