inventory = 0
rejected_entries = 0

while True:
    stock_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()

    if stock_input.lower() == "quit":
        print(f"Total Units Processed: {inventory}")
        print(f"Number of Failed/Rejected Entries: {rejected_entries}")
        break

    elif stock_input.isdigit():
        stock_qty = int(stock_input)
        inventory += stock_qty

        if inventory > 500:
            print("Alert: Overstock detected! Inventory has exceeded 500 units.")
            print(f"Total Units Processed: {inventory}")
            print(f"Number of Failed/Rejected Entries: {rejected_entries}")
            break

        print(f"Current inventory: {inventory}")

    elif stock_input.startswith("-") and stock_input[1:].isdigit():
        rejected_entries += 1
        print("Error: Negative stock quantities are not allowed.")

    else:
        rejected_entries += 1
        print("Error: Please enter a valid non-negative integer.")
