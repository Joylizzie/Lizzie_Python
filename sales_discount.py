import csv
import random
# """First method"""
# total = 0
# path = "C:\Lizhi\Python_study\Excel\example_csv1.csv"
# with open(path, 'r') as read_obj:
#     line = 'init'
#     while line:
#         line = read_obj.readline().strip()
#         fields = line.split(",")
#         if len(fields) != 3:
#             continue
#         try:
#             price = float(fields[1])
#             discount = float(fields[2])
#             total += price - discount
#         except ValueError:
#             pass
# print(total)

"""method 2 Much better, because you should use the CSV library to parse fields"""
# Create random rows as a csv file, named sales-discount.csv. If from Actual File, no need this step.
def create_in_file(num_of_rows, in_path):
    with open(in_path, 'w', newline='') as write_obj:
        # writer = csv.DictWriter(write_obj, fieldnames=['product_name', 'price', 'discount', 'total'])
        # writer.writeheader()
        writer = csv.writer(write_obj)
        writer.writerow(['product_name', 'price', 'discount'])

        for i in range(0, num_of_rows):
            product_name = 'lovely' + str(i)
            price = random.uniform(10, 10_000)
            discount = random.random()
            #write_obj.write(product_name + "," + str(price) + "," + str(discount) + '\n')
            writer.writerow([product_name, price, discount])

# def process_csv(in_path, out_path, err_path):
#     # Read Sales_discount file.
#     # Write a new out put file with no invalid rows, with valid rows.
#     # Write an error file with invalid rows.
#     # Validate the Actual sales_discount file, if it is NOT Random created.""
#
#     total = 0.00
#     total_price = 0.00
#     with open(in_path, 'r') as read_obj, open(out_path, 'w', newline='') as write_obj, open(err_path, 'w',newline='') as err_obj:
#         writer = csv.DictWriter(write_obj, fieldnames=['product_name', 'price', 'discount', 'total'])
#         writer.writeheader()
#         csv_in_reader = csv.reader(read_obj)
#         csv_out_writer = csv.writer(write_obj)
#         csv_err_writer = csv.writer(err_obj)
#
#         for line in csv_in_reader:
#             line = line[:3]
#             if not validate_first_two_columns(line):
#                 csv_err_writer.writerow(line)
#                 continue
#             if not validate_third_column(line):
#                 csv_err_writer.writerow(line)
#                 continue
#             if len(line) == 2:
#                 line.append('0')
#
#             try:
#                 price: float = float(line[1])
#                 discount: float = float(line[2])
#                 total_price += price
#                 total += price * (1 - discount )
#                 line.append(price * (1 - discount))
#                 csv_out_writer.writerow(line)
#             except ValueError:
#                 csv_err_writer.writerow(line)
#         csv_out_writer.writerow(['', str(total_price), '', str(total) ])
#     return total,total_price
#
#
# def validate_first_two_columns(t):
#     if len(t) < 2:
#         return False
#     if t[0] == '':
#         return False
#
#     try:
#         price: float = float(t[1])
#     except ValueError:
#         return False
#     if price < 0:
#         return False
#     return True
#
# def validate_third_column(t):
#     if len(t) >= 3:
#         try:
#             discount: float = float(t[2])
#         except ValueError:
#             return False
#         if discount < 0 or discount > 1:
#             return False
#     return True
#
#
in_path = "C:/Lizhi/Python_study/Excel/sales_discount/sales_discount.csv"
# out_path = "C:/Lizhi/Python_study/Excel/sales_discount/sales_discount_out.csv"
# err_path = "C:/Lizhi/Python_study/Excel/sales_discount/sales_discount_err.csv"
#
create_in_file(1_000, in_path)
#
# total,total_price = process_csv(in_path, out_path, err_path)
# print(total,total_price)
