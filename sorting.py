import time

# SELECTION SORT - SORT BY PRICE
def selection_sort_by_price(data):
    """
    Sort products by price using Selection Sort.
    This function sorts the given list directly.
    Time Complexity: O(n^2)
    """

    n = len(data)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if data[j].price < data[min_idx].price:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

    return data


# MERGE SORT - SORT BY PRODUCT ID
def merge_sort_by_id(data):
    """
    Sort products by Product ID using Merge Sort.
    Returns a new sorted list.
    Time Complexity: O(n log n)
    """

    if len(data) <= 1:
        return data[:]

    mid = len(data) // 2

    left = merge_sort_by_id(data[:mid])
    right = merge_sort_by_id(data[mid:])

    return merge_by_id(left, right)


def merge_by_id(left, right):
    """Merge two lists according to Product ID."""

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i].product_id.lower() <= right[j].product_id.lower():
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# MERGE SORT - SORT BY PRICE
def merge_sort_by_price(data):
    """
    Prepare products in ascending price order.
    This is used only to prepare benchmark test data.
    """

    if len(data) <= 1:
        return data[:]

    mid = len(data) // 2

    left = merge_sort_by_price(data[:mid])
    right = merge_sort_by_price(data[mid:])

    return merge_by_price(left, right)


def merge_by_price(left, right):
    """Merge two lists according to product price."""

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i].price <= right[j].price:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# REVERSE LIST
def reverse_list(data):
    """Create a reversed copy of a list manually."""

    result = []

    for i in range(len(data) - 1, -1, -1):
        result.append(data[i])

    return result

# SELECTION SORT MENU
def selection_sort_menu(inventory):

    print("\n========== SELECTION SORT (PRICE) ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    start = time.perf_counter()

    selection_sort_by_price(inventory)

    end = time.perf_counter()

    print("\nSorted by PRICE using Selection Sort!")
    print(f"Execution Time: {end - start:.10f} seconds")
    print(f"Total Products: {len(inventory):,}")
    print("Big-O: O(n^2)")

# MERGE SORT MENU
def merge_sort_menu(inventory):

    print("\n========== MERGE SORT (PRODUCT ID) ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    start = time.perf_counter()

    sorted_data = merge_sort_by_id(inventory)

    end = time.perf_counter()

    inventory[:] = sorted_data

    print("\nSorted by PRODUCT ID using Merge Sort!")
    print(f"Execution Time: {end - start:.10f} seconds")
    print(f"Total Products: {len(inventory):,}")
    print("Big-O: O(n log n)")