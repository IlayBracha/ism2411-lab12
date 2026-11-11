# Reflection 1:
# I think Python is better for repeating tasks and working with large files.
# Excel is easier for viewing and editing data manually.
# Both are useful, but Python can save more time with automation.

# Reflection 2:
# A store could use an append-mode log to track daily sales.
# Append mode is useful because it adds new information without
# deleting previous records.
import csv

# Exercise 2:
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

# Exercise 3:
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

# Exercise 4:
total_revenue = 0

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        product, price, quantity = row

        price = float(price)
        quantity = int(quantity)

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")

# Exercise 5:
high_value_orders = []
total_orders = 0

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        product, price, quantity = row

        price = float(price)
        quantity = int(quantity)
        total = price * quantity

        total_orders += 1

        if total > 100:
            high_value_orders.append([product, price, quantity, f"{total:.2f}"])

with open("data/cleaned.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["Product", "Price", "Qty", "Total"])
    writer.writerows(high_value_orders)

print(f"Wrote {len(high_value_orders)} out of {total_orders} orders to cleaned.csv")

# Exercise 6:
# I would use csv.reader for simple files with a few columns.
# I would use csv.DictReader when I want to access data by column names.

dict_total_revenue = 0

with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total Revenue (DictReader): ${dict_total_revenue:.2f}")

# Exercise 7:
sales_summary = {}

with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        sales_summary[product] = sales_summary.get(product, 0) + total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")

    # Exercise 8:
from datetime import datetime

with open("data/run_log.txt", "a") as f:
    current_time = datetime.now()
    f.write(f"{current_time}: Total Revenue = ${total_revenue:.2f}\n")

print("Run log updated.")