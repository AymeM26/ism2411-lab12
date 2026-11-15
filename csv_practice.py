import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

print("---Exercise 1---")
with open(SALES_FILE, "r") as f:
    print(f"Opened (SALES_FILE).")

print("---Exercise 2---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("---Exercise 3---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header:", header)
    for row in reader:
        print(row)

print("---Exercise 4---")

total_revenue = 0
with open(SALES_FILE, "r", newline="") as f:
    reader = csv.reader(f)
    next (reader)
    for row in reader:
        product = row [0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units x ${price:.2f} = ${line_total}")
print(f"Total revenue: ${total_revenue:.2f}")

print("---Exercise 5---")
rows_read = 0
rows_written = 0
with open(SALES_FILE, "r", newline="") as infile, \
    open(CLEANED_FILE, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        rows_read += 1
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        if total > 100:
            writer.writerow([row[0], price, quantity, f"{total:.2f}"])
            rows_written += 1
            print(f"wrote {rows_written} of {rows_read} rows to {CLEANED_FILE}")

print("---Exercise 6---")
dict_total = 0
print("DictReader")
with open (SALES_FILE, "r", newline="") as f:
    reader = csv. DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        dict_total += price * quantity
print(f"DictReader total: ${dict_total:.2f}")
print("Matches Exercise 4:", round(dict_total, 2) == round(total_revenue, 2))
