import time

def selection_sort_by_price(data):
    arr = data[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j].price < arr[min_idx].price:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort_by_id(data):
    if len(data) <= 1:
        return data[:]
    mid = len(data) // 2
    left = merge_sort_by_id(data[:mid])
    right = merge_sort_by_id(data[mid:])
    return merge_by_id(left, right)

def merge_by_id(left, right):
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

def reverse_list(data):
    result = []
    for i in range(len(data) - 1, -1, -1):
        result.append(data[i])
    return result

def selection_sort_menu(inventory):
    print("\n========== SELECTION SORT (PRICE) ==========")
    if len(inventory) == 0:
        print("Inventory is empty.")
        return
    start = time.perf_counter()
    sorted_data = selection_sort_by_price(inventory)
    end = time.perf_counter()
    inventory[:] = sorted_data
    print("Sorted by PRICE using Selection Sort!")
    print(f"Execution Time: {end - start:.10f} seconds")
    print(f"Total Products: {len(inventory):,}")
    print("Big-O: O(n^2)")

def merge_sort_menu(inventory):
    print("\n========== MERGE SORT (PRODUCT ID) ==========")
    if len(inventory) == 0:
        print("Inventory is empty.")
        return
    start = time.perf_counter()
    sorted_data = merge_sort_by_id(inventory)
    end = time.perf_counter()
    inventory[:] = sorted_data
    print("Sorted by PRODUCT ID using Merge Sort!")
    print(f"Execution Time: {end - start:.10f} seconds")
    print(f"Total Products: {len(inventory):,}")
    print("Big-O: O(n log n)")

def sorting_performance_testing(inventory):
    print("\n========== SORTING PERFORMANCE TESTING ==========")
    if len(inventory) == 0:
        print("Inventory is empty. Generate mock data first.")
        return
    print(f"Total Products: {len(inventory):,}")
    print("[1] Random Data")
    print("[2] Sorted Data")
    print("[3] Reverse-Sorted Data")
    choice = input("Choose arrangement: ").strip()
    if choice == "1":
        test_data = inventory[:]
        label = "Random"
    elif choice == "2":
        test_data = selection_sort_by_price(inventory) if len(inventory) <= 10000 else inventory[:]
        label = "Sorted"
    elif choice == "3":
        sorted_data = selection_sort_by_price(inventory) if len(inventory) <= 10000 else inventory[:]
        test_data = reverse_list(sorted_data)
        label = "Reverse-Sorted"
    else:
        print("Invalid choice.")
        return
    copy1 = test_data[:]
    start = time.perf_counter()
    selection_sort_by_price(copy1)
    selection_time = time.perf_counter() - start
    copy2 = test_data[:]
    start = time.perf_counter()
    merge_sort_by_id(copy2)
    merge_time = time.perf_counter() - start
    print(f"\nArrangement: {label}")
    print("\n========== RESULTS ==========")
    print(f"Selection Sort (Price): {selection_time:.10f} seconds - O(n^2)")
    print(f"Merge Sort (ID):        {merge_time:.10f} seconds - O(n log n)")
    print("\n========== ANALYSIS ==========")
    if merge_time < selection_time:
        print("Merge Sort was FASTER.")
        print(f"Merge Sort is {selection_time / merge_time:.2f}x faster!")
    else:
        print("Selection Sort was faster (only on very small data).")