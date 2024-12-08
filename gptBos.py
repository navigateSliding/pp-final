import os

# Helper functions for file I/O
def load_data(file_name):
    """Load data from text file into a list."""
    data = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file.readlines():
                data.append(line.strip().split(','))
    return data

def save_data(file_name, data):
    """Save list data to text file."""
    print(f"data: {data}")
    with open(file_name, 'w') as file:
        for item in data:
            file.write(','.join(item) + '\n')

# Functions for handling the menu options
def add_product(products):
    """Add a new product."""
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = input("Enter product price: ")
    products.append([product_id, name, description, price])
    save_data('products.txt', products)
    print("Product added successfully!")

def update_product(products):
    """Update existing product details."""
    product_id = input("Enter the product ID to update: ")
    for product in products:
        if product[0] == product_id:
            product[1] = input(f"Enter new name (current: {product[1]}): ")
            product[2] = input(f"Enter new description (current: {product[2]}): ")
            product[3] = input(f"Enter new price (current: {product[3]}): ")
            save_data('products.txt', products)
            print("Product updated successfully!")
            return
    print("Product not found!")

def add_supplier(suppliers):
    """Add a new supplier."""
    supplier_id = input("Enter supplier ID: ")
    name = input("Enter supplier name: ")
    contact = input("Enter supplier contact: ")
    suppliers.append([supplier_id, name, contact])
    save_data('suppliers.txt', suppliers)
    print("Supplier added successfully!")

def place_order(orders, products):
    """Place an order."""
    order_id = input("Enter order ID: ")
    product_id = input("Enter product ID to order: ")
    quantity = input("Enter quantity: ")
    order_date = input("Enter order date: ")
    
    # Check if product exists
    for product in products:
        if product[0] == product_id:
            orders.append([order_id, product_id, quantity, order_date])
            save_data('orders.txt', orders)
            print("Order placed successfully!")
            return
    print("Product not found!")

def view_inventory(products):
    """Display current inventory levels for all products."""
    print("Current Inventory:")
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[3]}")

def generate_reports(orders, products):
    """Generate reports such as low stock items, product sales, and supplier orders."""
    # Example: List orders placed per product
    print("Product Sales Report:")
    sales = {}
    for order in orders:
        product_id = order[1]
        if product_id in sales:
            sales[product_id] += int(order[2])
        else:
            sales[product_id] = int(order[2])

    for product in products:
        product_id = product[0]
        if product_id in sales:
            print(f"Product: {product[1]}, Sold: {sales[product_id]}")
        else:
            print(f"Product: {product[1]}, Sold: 0")

def exit_program():
    """Exit the program."""
    print("Exiting program...")
    exit()

# Main function to display the menu and process user input
def main():
    # Load initial data
    products = load_data('products.txt')
    suppliers = load_data('suppliers.txt')
    orders = load_data('orders.txt')
    
    while True:
        # Display menu
        print("\nMenu:")
        print("1. Add a new product")
        print("2. Update product details")
        print("3. Add a new supplier")
        print("4. Place an order")
        print("5. View inventory")
        print("6. Generate reports")
        print("7. Exit")
        
        # Get user choice
        choice = input("Choose an option (1-7): ")

        # Handle each option
        if choice == '1':
            add_product(products)
        elif choice == '2':
            update_product(products)
        elif choice == '3':
            add_supplier(suppliers)
        elif choice == '4':
            place_order(orders, products)
        elif choice == '5':
            view_inventory(products)
        elif choice == '6':
            generate_reports(orders, products)
        elif choice == '7':
            exit_program()
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
