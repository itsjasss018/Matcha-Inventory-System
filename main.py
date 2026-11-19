from inventory import add_product, view_inventory, generate_mock_data

def main():
    while True:
        print("\n" + "=" * 40)
        print("       MATCHA INVENTORY SYSTEM")
        print("=" * 40)
        print("[1] Add Product")
        print("[2] View Inventory")
        print("[3] Linear Search")
        print("[4] Binary Search")
        print("[5] Selection Sort")
        print("[6] Merge Sort")
        print("[7] Generate Mock Data")
        print("[8] Performance Testing")
        print("[9] Exit")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            view_inventory()

        elif choice == "3":
            print("\nLinear Search is not yet integrated.")

        elif choice == "4":
            print("\nBinary Search is not yet integrated.")

        elif choice == "5":
            print("\nSelection Sort is not yet integrated.")

        elif choice == "6":
            print("\nMerge Sort is not yet integrated.")

        elif choice == "7":
            generate_mock_data()

        elif choice == "8":
            print("\nPerformance Testing is not yet integrated.")

        elif choice == "9":
            print("\nThank you for using Matcha Inventory System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
