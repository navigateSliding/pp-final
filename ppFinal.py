import os

file_list = ["products.txt", "suppliers.txt", "orders.txt"]

def environment_check():
    for files in file_list:
        if not os.path.exists(files):
            with open(files, 'w') as f:
                if files == "products.txt":
                    f.write("ID | Name | Qty | Description | Price")
                if files == "suppliers.txt":
                    f.write("ID | Name | Contact")
                if files == "orders.txt":
                    f.write("Name | Qty")

def load_data(file_name):
    data = []

    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file.readlines():    
                data.append(line.strip().split(','))
    return data

def add_product(products): 
    product_id = input('Enter your product id: ')
    product_name = input('Enter product name: ')
    product_count = int(input('Enter how many product: '))
    product_description = input('Enter description of product: ')
    product_price = float(input('Enter product price (in MYR): '))
    
    products.append([product_name, product_id, product_count, product_description, product_price])
    with open('products.txt', 'w') as file:
        for product in products:
            file.write(','.join([str(item) for item in product]) + '\n')

    print(f'Number of product added: {len(products)}')
    print('Product is successfully added')


def update_product(products):
    product_id = input('Enter the product id : ')
    for product in products:
        if product[1] == product_id:
            product[0] = input(f"Enter new name (current: {product[0]}): ")
            product[2] =  int(input(f"Enter new count (current: {product[2]}): "))
            product[3] = input(f"Enter new description (current: {product[3]}): ")
            product[4] = float(input(f"Enter new price (current: {product[4]}): "))
            with open('products.txt', 'w') as file:
                for item in products:
                    file.write(','.join(item) + '\n')
            print("Product updated successfully!")
            return
        else :
            print("product not found")

def add_supplier(suppliers):
    supplier_id = input("Enter supplier ID: ")
    name = input("Enter supplier name: ")
    contact = input("Enter supplier contact: ")

    suppliers.append([supplier_id, name, contact])
    with open('suppliers.txt', 'w') as file:
        for supply in suppliers:
            file.write(','.join(map(str, supply)) + '\n')
        print("Suppliers successfully added!")


def place_order():
    user_order_name = input("What product to order?: ")
    user_order_count = int(input("How much of that product to order?: "))

    orders = open("orders.txt", "a")
    orders.write(user_order_name + ": " + user_order_count + "\n")

    user_order_count = int(user_order_count)
    with open("products.txt", "r") as products:
        for product in products:
            if user_order_name == products[0]:
                product[4] = int(product[4])
                price = product[4] * user_order_count
                print(price)

def view_inventory():
    with open ("products.txt", "r") as inventory:
        inventory.read()
        for product in inventory:
            product[2] = int(product[2])
            print(product[0] + product[2])

def generate_reports():
    print("test")

def main():
    products = load_data('products.txt')
    suppliers = load_data('suppliers.txt')
    orders = load_data('orders.txt')

    while True:
        user_input = input("1. Add a new product \n"
                            "2. Update product details \n"
                            "3. Add a new supplier \n"
                            "4. Place an order \n"
                            "5. View inventory \n"
                            "6. Generate reports \n"
                            "7. Exit \n"
                            "Enter Number : ")

        match user_input:
            case "1": add_product(products)
            case "2": update_product(products)
            case "3": add_supplier()
            case "4": place_order()
            case "5": view_inventory()   
            case "6": generate_reports()
            case "7": break
            case _: print("Invalid option, pick something within the range of 1-7")

if __name__ == "__main__":
    main()