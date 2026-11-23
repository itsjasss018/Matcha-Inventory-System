from inventory import (
    add_product,
    view_inventory,
    generate_mock_data,
    linear_search,
    binary_search,
    performance_testing,
    inventory  # for sorting -ella
)
from sorting import selection_sort_menu, merge_sort_menu, sorting_performance_testing  # for sorting -ella

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
        print("[9] Sorting Performance Testing")  # for sorting -ella
        print("[10] Exit")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            view_inventory()

        elif choice == "3":
            linear_search()

        elif choice == "4":
            binary_search()

        elif choice == "5":
            selection_sort_menu(inventory)  # for sorting -ella

        elif choice == "6":
            merge_sort_menu(inventory)  # for sorting -ella

        elif choice == "7":
            generate_mock_data()

        elif choice == "8":
            performance_testing()

        elif choice == "9":
            sorting_performance_testing(inventory)  # for sorting -ella

        elif choice == "10":
            print("\nThank you for using Matcha Inventory System!")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()