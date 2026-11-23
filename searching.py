import time
from inventory import inventory
from sorting import merge_sort_by_id


# LINEAR SEARCH
def linear_search():
    print("\n========== LINEAR SEARCH ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    search_id = input("Enter Product ID to search: ").strip()

    if not search_id:
        print("Please enter a Product ID.")
        return

    for product in inventory:
        if product.product_id.lower() == search_id.lower():
            print("\nProduct Found!")
            print(f"Product ID: {product.product_id}")
            print(f"Product Name: {product.name}")
            print(f"Category: {product.category}")
            print(f"Price: PHP {product.price:.2f}")
            print(f"Stock: {product.stock}")
            return

    print("\nProduct not found.")

# BINARY SEARCH
def binary_search():
    print("\n========== BINARY SEARCH ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    search_id = input("Enter Product ID to search: ").strip().lower()

    if not search_id:
        print("Please enter a Product ID.")
        return

    # Manually sort using Merge Sort
    sorted_inventory = merge_sort_by_id(inventory)

    low = 0
    high = len(sorted_inventory) - 1

    while low <= high:
        mid = (low + high) // 2
        current_id = sorted_inventory[mid].product_id.lower()

        if current_id == search_id:
            product = sorted_inventory[mid]

            print("\nProduct Found!")
            print(f"Product ID: {product.product_id}")
            print(f"Product Name: {product.name}")
            print(f"Category: {product.category}")
            print(f"Price: PHP {product.price:.2f}")
            print(f"Stock: {product.stock}")
            return

        elif current_id < search_id:
            low = mid + 1

        else:
            high = mid - 1

    print("\nProduct not found.")


# SEARCH PERFORMANCE TESTING
def performance_testing():

    print("\n========== SEARCH PERFORMANCE TESTING ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        print("Generate mock data first.")
        return

    search_id = inventory[-1].product_id.lower()

    # Prepare sorted data BEFORE timing
    sorted_inventory = merge_sort_by_id(inventory)

    # LINEAR SEARCH TIMING
    start_time = time.perf_counter()

    for product in inventory:
        if product.product_id.lower() == search_id:
            break

    linear_time = time.perf_counter() - start_time

    # BINARY SEARCH TIMING
    low = 0
    high = len(sorted_inventory) - 1

    start_time = time.perf_counter()

    while low <= high:
        mid = (low + high) // 2
        current_id = sorted_inventory[mid].product_id.lower()

        if current_id == search_id:
            break

        elif current_id < search_id:
            low = mid + 1

        else:
            high = mid - 1

    binary_time = time.perf_counter() - start_time

    print(f"\nTotal Products: {len(inventory):,}")
    print(f"Search ID: {search_id.upper()}")

    print("\n========== RESULTS ==========")
    print(f"Linear Search: {linear_time:.10f} seconds")
    print(f"Binary Search: {binary_time:.10f} seconds")

    print("\n========== BIG-O COMPARISON ==========")
    print("Linear Search: O(n)")
    print("Binary Search: O(log n)")

    print("\nPerformance testing completed!")
