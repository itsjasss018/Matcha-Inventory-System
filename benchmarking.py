# measure how fast your algorithms execute

# MATCHA INVENTORY SYSTEM
# PERFORMANCE BENCHMARKING
import random
import time

from product import MatchaProduct

from sorting import (
    selection_sort_by_price,
    merge_sort_by_id,
    merge_sort_by_price,
    reverse_list
)

# DATASET GENERATOR
def generate_test_data(size):
    """Generate mock products with unique Product IDs."""

    products = []

    product_names = [
        "Classic Matcha",
        "Strawberry Matcha",
        "Iced Matcha Latte",
        "Matcha Frappe",
        "Vanilla Matcha",
        "Matcha Cheesecake",
        "Matcha Cookies",
        "Matcha Powder",
        "Matcha Whisk",
        "Matcha Bowl"
    ]

    categories = [
        "Beverage",
        "Ingredient",
        "Pastry",
        "Equipment"
    ]

    for i in range(1, size + 1):

        product = MatchaProduct(
            f"MOCK{i:05d}",
            random.choice(product_names),
            random.choice(categories),
            round(random.uniform(50, 500), 2),
            random.randint(1, 100)
        )

        products.append(product)

    return products

# SEARCHING ALGORITHMS
def linear_search_algorithm(data, search_id):
    """Search for a Product ID using Linear Search."""

    for product in data:

        if product.product_id.lower() == search_id.lower():
            return product

    return None


def binary_search_algorithm(data, search_id):
    """Search for a Product ID using Binary Search."""

    low = 0
    high = len(data) - 1

    while low <= high:

        mid = (low + high) // 2

        current_id = data[mid].product_id.lower()

        if current_id == search_id.lower():
            return data[mid]

        elif current_id < search_id.lower():
            low = mid + 1

        else:
            high = mid - 1

    return None


# PREPARE SEARCH AND MERGE SORT ARRANGEMENTS
def prepare_id_arrangements(data):

    random_data = data[:]
    random.shuffle(random_data)

    sorted_data = merge_sort_by_id(data)

    reverse_sorted_data = reverse_list(sorted_data)

    return {
        "Random": random_data,
        "Sorted": sorted_data,
        "Reverse-Sorted": reverse_sorted_data
    }

# PREPARE SELECTION SORT ARRANGEMENTS
def prepare_price_arrangements(data):

    random_data = data[:]
    random.shuffle(random_data)

    sorted_data = merge_sort_by_price(data)

    reverse_sorted_data = reverse_list(sorted_data)

    return {
        "Random": random_data,
        "Sorted": sorted_data,
        "Reverse-Sorted": reverse_sorted_data
    }

# SEARCH BENCHMARK
def benchmark_searching(data, search_id):

    # Prepare sorted data before timing Binary Search
    sorted_data = merge_sort_by_id(data)

    # LINEAR SEARCH
    start = time.perf_counter()

    linear_search_algorithm(data, search_id)

    linear_time = time.perf_counter() - start

    # BINARY SEARCH
    start = time.perf_counter()

    binary_search_algorithm(sorted_data, search_id)

    binary_time = time.perf_counter() - start

    return linear_time, binary_time

# SORTING BENCHMARK
def benchmark_sorting(selection_input, merge_input, run_selection=True):

    selection_time = None

    # SELECTION SORT
    if run_selection:

        # Copy is prepared outside the timed section
        selection_data = selection_input[:]

        start = time.perf_counter()

        selection_sort_by_price(selection_data)

        selection_time = time.perf_counter() - start

    # MERGE SORT
    # Merge Sort returns a new sorted list.
    start = time.perf_counter()

    merge_sort_by_id(merge_input)

    merge_time = time.perf_counter() - start

    return selection_time, merge_time


# DISPLAY RESULTS
def display_results(size, arrangement, results):

    linear_time, binary_time, selection_time, merge_time = results

    print("\n" + "=" * 75)
    print(f"DATASET SIZE: {size:,} RECORDS")
    print(f"ARRANGEMENT: {arrangement}")
    print("=" * 75)

    print(f"{'ALGORITHM':<28}{'EXECUTION TIME':>25}{'BIG-O':>18}")
    print("-" * 75)

    print(
        f"{'Linear Search':<28}"
        f"{linear_time:>25.10f}"
        f"{'O(n)':>18}"
    )

    print(
        f"{'Binary Search':<28}"
        f"{binary_time:>25.10f}"
        f"{'O(log n)':>18}"
    )

    if selection_time is not None:

        print(
            f"{'Selection Sort':<28}"
            f"{selection_time:>25.10f}"
            f"{'O(n^2)':>18}"
        )

    else:

        print(
            f"{'Selection Sort':<28}"
            f"{'SKIPPED':>25}"
            f"{'O(n^2)':>18}"
        )

    print(
        f"{'Merge Sort':<28}"
        f"{merge_time:>25.10f}"
        f"{'O(n log n)':>18}"
    )

    print("=" * 75)


# MAIN BENCHMARKING FUNCTION
def run_benchmarks():

    print("\n" + "=" * 75)
    print("             MATCHA INVENTORY SYSTEM")
    print("                  BENCHMARKING")
    print("=" * 75)

    dataset_sizes = [1000, 10000, 30000]

    print("\nRequired Dataset Sizes:")
    print("1,000 | 10,000 | 30,000 Records")

    print("\nRequired Data Arrangements:")
    print("Random | Sorted | Reverse-Sorted")

    print("\nAlgorithms:")
    print("Linear Search | Binary Search")
    print("Selection Sort | Merge Sort")

    print("\nIMPORTANT:")
    print("Selection Sort on 30,000 records may take a long time.")

    confirm = input(
        "\nRun Selection Sort on all dataset sizes, including 30,000? (Y/N): "
    ).strip().upper()

    run_large_selection = confirm == "Y"

    if not run_large_selection:
        print("\nSelection Sort on 30,000 records will be skipped.")

    # TEST ALL REQUIRED DATASET SIZES
    for size in dataset_sizes:

        print("\n\n" + "#" * 75)
        print(f"GENERATING {size:,} TEST RECORDS...")
        print("#" * 75)

        # Data generation is outside algorithm timing
        dataset = generate_test_data(size)

        # Prepare arrangements for each algorithm's sorting key
        id_arrangements = prepare_id_arrangements(dataset)

        price_arrangements = prepare_price_arrangements(dataset)

        # Use the last generated Product ID as the search target
        search_id = dataset[-1].product_id

        # Test all three arrangements
        for arrangement_name in id_arrangements:

            print(f"\nTesting {arrangement_name} Data...")

            # SEARCHING TESTS
            search_data = id_arrangements[arrangement_name]

            linear_time, binary_time = benchmark_searching(
                search_data,
                search_id
            )

            # SORTING TESTS
            selection_data = price_arrangements[arrangement_name]

            merge_data = id_arrangements[arrangement_name]

            run_selection = True

            if size == 30000 and not run_large_selection:
                run_selection = False

            selection_time, merge_time = benchmark_sorting(
                selection_data,
                merge_data,
                run_selection
            )

            results = (
                linear_time,
                binary_time,
                selection_time,
                merge_time
            )

            display_results(
                size,
                arrangement_name,
                results
            )

    print("\n" + "=" * 75)
    print("ALL BENCHMARKING TESTS COMPLETED!")
    print("=" * 75)

# RUN MODULE DIRECTLY
if __name__ == "__main__":
    run_benchmarks()