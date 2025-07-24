

def analyzeOrders(file):
    orders = []
    file = open(file, "r")
    lines = file.readlines()
    # with open("orders.txt", "r") as file:
    for line in lines:
        customer_id, product, category, price = line.strip().split(",")
        orders.append((int(customer_id), product, category, float(price)))


    # Data containers
    customer_spend = {}           # customer_id -> total spent
    product_frequency = {}        # product_name -> count
    category_revenue = {}         # category -> total revenue

    # Process orders
    for order in orders:
        customer_id, product, category, price = order

        # Track customer spend
        if customer_id not in customer_spend:
            customer_spend[customer_id] = 0
        customer_spend[customer_id] += price

        # Track product frequency
        if product not in product_frequency:
            product_frequency[product] = 0
        product_frequency[product] += 1

        # Track category revenue
        if category not in category_revenue:
            category_revenue[category] = 0
        category_revenue[category] += price

    # Define high-value customer threshold
    high_value_threshold = 1000
    high_value_customers = {cid: spend for cid, spend in customer_spend.items() if spend > high_value_threshold}

    # Most popular products
    popular_products = sorted(product_frequency.items(), key=lambda x: x[1], reverse=True)

    # Most profitable categories
    profitable_categories = sorted(category_revenue.items(), key=lambda x: x[1], reverse=True)

    # --- Report Generation ---
    print("\n--- Customer Classification ---")
    for cid, spend in customer_spend.items():
        label = "High Value" if spend > high_value_threshold else "Regular"
        print(f"Customer {cid}: ${spend:.2f} ({label})")

    print("\n--- Product Popularity ---")
    for product, count in popular_products:
        print(f"{product}: {count} purchases")

    print("\n--- Category Revenue ---")
    for category, revenue in profitable_categories:
        print(f"{category}: ${revenue:.2f}")

    print("\n--- High Value Customers ---")
    for cid, spend in high_value_customers.items():
        print(f"Customer {cid}: ${spend:.2f}")




def InteractiveMenu():
    global exitStat
    print("You may select one of the following options:\n1: Analyze orders \n2: Exit")
    UserInput = input("Option ?")
    if UserInput == '1':
        file = input("Please enter the path to the file or order summary.")
        # "course1/orders.txt"
        NewExpense = analyzeOrders(file)
    elif UserInput=="2":
        exitStat += 1
    else: 
        "Did not input option correctly"

exitStat=0
while exitStat==0:
    InteractiveMenu()