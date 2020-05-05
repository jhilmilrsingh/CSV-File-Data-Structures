import csv
filename = 'products.txt'

def read_csv_into_list():
    products_list = []
    with open(filename) as input_file_handle:
        input_csv = csv.reader(input_file_handle)
        header_row = next(input_csv)

        for row in input_csv:
            products_list.append(row)
    return products_list

def print_report(products_list):
    print('\nProduct Report:\n')
    
    products_list.sort()
    total_asset = 0
    x = 0
    b = 0
    
    for products in products_list:
        print("Product ID:", products[0])
        print("Description:", products[1])
        print("Unit Price:", products[2])
        print("Inventory Count:", products[3])

        a = int(products[3])
        b += a
        
        y = float(products[2]) * float(products[3])
        x += y
        print("Value: ${:,.2f}".format(y), '\n')

    print("Total Number of items: {:d}".format(b))
    print("Total Of All Assets: ${:,.2f}".format(x))

def main():
    
    try:
        list_of_students = read_csv_into_list()
        print_report(list_of_students)
    except FileNotFoundError:
        print(filename, 'not found')
        
main()
