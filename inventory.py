
import random
from product import MatchaProduct

# Stores all product records
inventory = []


# ==========================================
# ADD PRODUCT
# ==========================================

def add_product():
    print("\n========== ADD PRODUCT ==========")

    product_id = input("Enter Product ID: ").strip()

    if not product_id:
        print("Error: Product ID cannot be empty.")
        return

    # Check for duplicate IDs (case-insensitive)
    for product in inventory:
        if product.product_id.lower() == product_id.lower():
            print("Error: Product ID already exists!")
            return

    name = input("Enter Product Name: ").strip()
    category = input("Enter Category: ").strip()

    if not name or not category:
        print("Error: Name and category cannot be empty.")
        return

    try:
        price = float(input("Enter Price: "))

        if price < 0:
            print("Error: Price cannot be negative.")
            return

    except ValueError:
        print("Error: Please enter a valid price.")
        return

    try:
        stock = int(input("Enter Stock Quantity: "))

        if stock < 0:
            print("Error: Stock cannot be negative.")
            return

    except ValueError:
        print("Error: Please enter a valid quantity.")
        return

    new_product = MatchaProduct(
        product_id, name, category, price, stock
    )

    inventory.append(new_product)

    print("\nProduct added successfully!")


# ==========================================
# VIEW INVENTORY
# ==========================================


def view_inventory():
    print("\n========== MATCHA INVENTORY ==========")

    if len(inventory) == 0:
        print("No products available.")
        return

    print("-" * 85)
    print(
        f"{'ID':<12}{'NAME':<25}"
        f"{'CATEGORY':<18}{'PRICE':<15}{'STOCK':<10}"
    )
    print("-" * 85)

    for product in inventory[:20]:
        print(
            f"{product.product_id:<12}"
            f"{product.name:<25}"
            f"{product.category:<18}"
            f"PHP {product.price:<10.2f}"
            f"{product.stock:<10}"
        )

    print("-" * 85)

    if len(inventory) > 20:
        print(f"Showing 20 of {len(inventory):,} products.")
    else:
        print(f"Total products: {len(inventory)}")


# ==========================================
# MOCK DATA GENERATOR
# ==========================================

def generate_mock_data():

    print("\n========== MOCK DATA GENERATOR ==========")
    print("[1] Generate 1,000 Records")
    print("[2] Generate 10,000 Records")
    print("[3] Generate 30,000 Records")

    choice = input("Choose dataset size: ").strip()

    dataset_sizes = {
        "1": 1000,
        "2": 10000,
        "3": 30000
    }

    if choice not in dataset_sizes:
        print("Invalid choice. Please try again.")
        return

    size = dataset_sizes[choice]

    print(f"\nYou selected {size:,} records.")

    if len(inventory) > 0:
        print("Warning: This will replace your current inventory.")

        confirm = input("Continue? (Y/N): ").strip().upper()

        if confirm != "Y":
            print("Mock data generation cancelled.")
            return

    # Sample product information
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

    generated_products = []

    # Generate unique product records
    for i in range(1, size + 1):

        product_id = f"MOCK{i:05d}"
        name = random.choice(product_names)
        category = random.choice(categories)
        price = round(random.uniform(50, 500), 2)
        stock = random.randint(1, 100)

        product = MatchaProduct(
            product_id,
            name,
            category,
            price,
            stock
        )

        generated_products.append(product)

    # Replace inventory with generated records
    inventory[:] = generated_products

    print("\nMock data generated successfully!")
    print(f"Total records generated: {len(inventory):,}")
    print("All product IDs are unique.")


# ==========================================
# END OF INVENTORY MODULE
# ==========================================
