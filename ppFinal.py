import os

def load_data(file_name): #udah
    data = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file.readlines()[1:]:    
                data.append(line.strip().split(','))
    elif not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            if file_name == "products.txt":
                f.write("ID | Name | Qty | Description | Price" + "\n")
            if file_name == "suppliers.txt":
                f.write("ID | Name | Contact" + "\n")
            if file_name == "orders.txt":
                f.write("Name | Qty" + "\n")
    return data 

def save_data(data_type, data_content):
    if data_type == "products":
        categories = "ID | Name | Qty | Description | Price"
    elif data_type == "suppliers":
        categories = "ID | Name | Contact"
    elif data_type == "orders":
        categories = "Name | Qty"

    with open(data_type + ".txt", 'w') as file:
        file.write(categories + '\n')

        print(categories, data_type, data_content)

        for data in data_content:
            file.write(','.join([str(item) for item in data]) + '\n')

def add_product(products): #udah
    try:
        product_id = input('Enter your product id: ').upper()
        product_name = input('Enter product name: ')
        product_count = int(input('Enter how many product: '))
        product_description = input('Enter description of product: ')
        product_price = float(input('Enter product price (in MYR): '))

    except ValueError:
        print("Wrong Value Type")
        
    else:
        products.append([product_id, product_name, product_count, product_description, product_price])
        save_data("products", products)

        print(f'Number of product added: {len(products)}')
        print('Product is successfully added')


def update_product(products):   #udah 
    product_id = input('Enter the product id : ').upper()
    for product in products:
        if product[0] == product_id:
            try:
                product[1] = input(f"Enter new Name (current: {product[1]}): ")
                product[2] = int(input(f"Enter new Qty (current: {product[2]}): "))
                product[3] = input(f"Enter new Description (current: {product[3]}): ")
                product[4] = float(input(f"Enter new price (current: {product[4]}): "))
            except ValueError:
                print("Wrong Value Type")
                return
            else: 
                save_data("products", products)
                print("Product updated successfully!")
                return
    else:
        print("Product not found")

def add_supplier(suppliers): #belom cek
    try:
        supplier_id = input("Enter supplier ID: ").upper()
        name = input("Enter supplier name: ")
        contact = int(input("Enter supplier contact number: "))
    except ValueError:
        print("Wrong Value Type")
    else:
        suppliers.append([supplier_id, name, contact])
        save_data("suppliers", suppliers)
        print("Suppliers successfully added!")


def place_order(): #belom cek
    try:
        user_order_name = input("What product to order?: ")
        user_order_count = int(input("How much of that product to order?: "))
    except ValueError:
        print("Wrong Value Type")
    else:
        orders = open("orders.txt", "a")
        orders.write(user_order_name + ": " + user_order_count + "\n")

        user_order_count = int(user_order_count)
        with open("products.txt", "r") as products:
            for product in products:
                if user_order_name == products[0]:
                    product[4] = int(product[4])
                    price = product[4] * user_order_count
                    print(price)

def view_inventory(products): #belom cek
    try:
        for product in products:
            product[2] = int(product[2])
    except IndexError:
        print("No Data In the File")
    else:
        print("ID | Qty | Price")
        for product in products:
            print(product[0], product[2], product[4])

def generate_reports(): #belom samsek
    print("test")

def main():
    while True:
        products = load_data('products.txt')
        suppliers = load_data('suppliers.txt')
        orders = load_data('orders.txt')
        
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
            case "3": add_supplier(suppliers)
            case "4": place_order(orders)
            case "5": view_inventory(products)   
            case "6": generate_reports()
            case "7": break
            case _: print("Invalid option, pick something within the range of 1-7")

if __name__ == "__main__":
    main()