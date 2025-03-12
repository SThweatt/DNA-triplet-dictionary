import time

# Hidden dictionary: Maps DNA triplets to ASCII decimal values
dna_triplet_dict = {
    "TAC": 82,  "TGG": 111, "GAC": 123, "TGC": 77,  "TGA": 117, "TGT": 116, 
    "GCT": 97,  "CGT": 101, "CGA": 100, "CCG": 95,  "AGT": 71,   "CGC": 110, 
    "GGT": 109, "TCT": 115, "GGA": 125
}

def main():
    print("\nWelcome to the DNA sequence triplet dictionary.\n")

    while True:
        # Get user input for DNA triplet
        triplet = input("Enter a DNA triplet (e.g., TAC, GCG): ").upper()

        # Check if the triplet exists in the dictionary
        if triplet in dna_triplet_dict:
            print(f"Result: {dna_triplet_dict[triplet]}")
        else:
            print("Error: Triplet not found in the dictionary.")

        # Menu options
        print("\nMenu:")
        print("1. Search for another triplet")
        print("2. Exit")

        choice = input("Select an option (1 or 2): ")

        if choice == "2":
            print("\nThank you for using our dictionary.")
            time.sleep(3)  # Wait 3 seconds before exiting
            break
        elif choice != "1":
            print("Invalid choice. Returning to menu...\n")

if __name__ == "__main__":
    main()
