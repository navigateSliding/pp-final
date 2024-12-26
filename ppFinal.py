import os
import time

def duplicate_check(input_id, data_content):
    for id_check in data_content:
        if id_check[0] == input_id:
            return True
    return False

def format_header(file_name):
    with open(file_name, 'r') as f:
        first_line = (f.readline()).strip()

    if first_line == "ID | Name | Qty | Description | Price" or first_line == "ID | Name | Contact" or first_line == "Name | Qty":
        return first_line
    else:
        with open(file_name, 'r+') as f:
            original_content = f.read()
            f.seek(0)

            if file_name == "products.txt":
                f.write("ID | Name | Qty | Description | Price" + "\n" + original_content)
            if file_name == "suppliers.txt":
                f.write("ID | Name | Contact" + "\n" + original_content)
            if file_name == "orders.txt":
                f.write("Order ID | Product Name | Qty | Clients" + "\n" + original_content)

def load_data(file_name): #udah
    data = []

    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            for line in f.readlines()[1:]:    
                data.append(line.strip().split(','))
    elif not os.path.exists(file_name):
        with open(file_name, 'w'):
            pass
        
    format_header(file_name)

    return data 

def save_data(file_name, data_content):
    header = format_header(file_name)

    with open(file_name, 'w') as file:
        file.write(header + '\n')
        for data in data_content:
            file.write(','.join([str(item) for item in data]) + '\n')

def add_product(products): #udah
    try:
        while 1:
            product_id = input('Enter your product id: ').upper()
            if duplicate_check(product_id, products):
                print("The ID already exist on the database")
            else:
                break

        product_name = input('Enter product name: ')
        product_count = int(input('Enter how many product: '))
        product_description = input('Enter description of product: ')
        product_price = float(input('Enter product price (in MYR): '))
    except ValueError:
        print("Wrong Value Type")
        
    else:
        products.append([product_id, product_name, product_count, product_description, product_price])
        save_data("products.txt", products)

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
                save_data("products.txt", products)
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
        save_data("suppliers.txt", suppliers)
        print("Suppliers successfully added!")


def place_order(products, orders):
    os.system('cls')
    print("\n -- ORDERING PRODUCT -- \n")       #title
    
    no = 0      #an ordinary number (used in showing the products)
    no1 = 0     #automatic id in order list

    for i in orders :
            no1 += 1        #set the id for the latest (count how many orders have made)


    #TESTING IS THERE ANY DATA ?
    if not products :       #if there is no
        print("Sorry, we don't have any product right now")
        time.sleep(3)
    

    else :      #if there is
    #show the available products
        print("Product Available currently : ")
        for product in products :  
            no += 1
            print (f"{no}. ID = {product[0]} | Name = {product[1]} | Quantity = {product[2]} | Description = {product[3]}")
        ask_user = input("\nWhich way do you prefer to order the products (ID/Name) : ").upper()  # ask the user to choose id or name


        #IF THE USER CHOSE ID
        if ask_user == 'ID' :       
            order_product = input("Select the product (ID) : ").upper()

            # (for) checking if there is a product or not
            for product in products:        
                if product[0] == order_product:

                    #checking if the user input a correct value
                    try:            
                        no1 += 1            #setting the order id
                        order_customer = input("\nInput the client name : ")  
                        order_quantity = int(input(f"How much products do you order (available[{product[2]}]): "))  

                        # to test if the products quantity meet the user's order
                        if order_quantity <= int(product[2]) :                  
                            orders.append([f"{no1:04d}",product[1],order_quantity, order_customer])     # dd the data to the orders list
                            product[2] = int(product[2])- order_quantity        #reduce the product
                            save_data("orders", orders)                         #save data orders
                            save_data("products", products)                     #save data products
                            print(f"\nDetails :\nID = {no1:04d} | Product = {product[1]} | Order = {order_quantity} | Client = {order_customer}\n\nOrders added successfully!\n")    # show the orders which made
                            time.sleep(3)
                            return
                        
                        else :              #if the products quantity not meet the user's order
                            print(f"Sorry, insufficient product\n")
                            time.sleep(2)
                            return

                    except ValueError:          #if the user input the wrong value type
                        print("Wrong value type, please input number type")     
                        time.sleep(2)    
                        return 
                    
            else:           #if there is no such product
                print("Product not found")
                time.sleep(2)
                return
            

        #IF THE USER CHOSE NAME
        elif ask_user == 'NAME' :
            order_product = input("Select the product (product name) : ")

            #(for)checking if there is a product or not
            for product in products:        
                if product[1] == order_product:

                    #checking if the user input a correct value
                    try:            
                        no1 += 1            # setting the order id
                        order_customer = input("\nInput the client name : ")
                        order_quantity = int(input(f"How much products do you order (available[{product[2]}]): ")) 

                        #testing if the products quantity meet the user's order
                        if order_quantity <= int(product[2]) :                  
                            orders.append([f"{no1:04d}",product[1],order_quantity, order_customer])     #add the data to the orders list
                            product[2] = int(product[2])- order_quantity        #reduce the product
                            save_data("orders", orders)                         #save data orders
                            save_data("products", products)                     #save data products
                            print(f"\nDetails :\nID = {no1:04d} | Product = {product[1]} | Order = {order_quantity} | Client = {order_customer}\n\nOrders added successfully!\n")   # show the orders which made
                            time.sleep(3)
                            return
                        
                        else :              #if the products quantity not meet the user's order
                            print(f"Sorry, insufficient product\n")
                            time.sleep(2)
                            return

                    except ValueError:          #if the user input the wrong value type
                        print("Wrong value type, please input number type")
                        time.sleep(2)
                        return 
                    
            else:           #if there is no such product
                print("Product not found")
                time.sleep(2)
                return
            

        #IF THE USER DID NOT INPUT ID NOR NAME 
        else :
            print("Please input correctly(ID/Name)\n")
            time.sleep(2)
            return

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
            case "4": place_order(products, orders)
            case "5": view_inventory(products)   
            case "6": generate_reports()
            case "7": break
            case _: print("Invalid option, pick something within the range of 1-7")

if __name__ == "__main__":
    main()