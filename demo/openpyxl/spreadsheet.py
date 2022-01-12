import openpyxl

dir_path = "./demo/openpyxl"


def get_details_of_product_numbers_owned_by_suppliers():
    # Somehow it is not relative path like in javascript
    inventory_file = openpyxl.load_workbook(f'{dir_path}/inventory.xlsx')

    # Get sheet one from inventory file (spreadsheet)
    product_list = inventory_file["Sheet1"]

    # Dictionaries
    products_per_supplier = {}
    total_value_per_supplier = {}

    # 75 rows -> [2, 3, 4...]
    for row_number in range(2, product_list.max_row + 1):
        # Get supplier name that is in fourth cell in row <row number>
        supplier_name = product_list.cell(row_number, 4).value

        # Get inventory and price from the row
        inventory = product_list.cell(row_number, 2).value
        price = product_list.cell(row_number, 3).value

        # Get cell object from blank column
        inventory_price = product_list.cell(row_number, 5)

        # 1. If supplier name already exist in dictionary
        # Add num of product to the supplier
        if supplier_name in products_per_supplier:
            print("Found 1 more product for existing supplier")
            current_num_products = products_per_supplier.get(supplier_name)
            products_per_supplier[supplier_name] = current_num_products + 1
        else:
            print("Adding a new supplier")
            products_per_supplier[supplier_name] = 1

        # 2. Calculate total value of inventory per supplier
        if supplier_name in total_value_per_supplier:
            current_total_value = total_value_per_supplier.get(supplier_name)
            total_value_per_supplier[supplier_name] = current_total_value + inventory * price
        else:
            total_value_per_supplier[supplier_name] = inventory * price

        # 3. Add value for total inventory price to blank column's cell
        inventory_price .value = inventory * price

    print("Printing in memory dictionary that stores products number per supplier: ", products_per_supplier)
    print("Printing in memory dictionary that stores total value of all inventory per supplier: ", total_value_per_supplier)

    inventory_file.save(f"{dir_path}/inventory_with_inventory_price_column.xlsx")

