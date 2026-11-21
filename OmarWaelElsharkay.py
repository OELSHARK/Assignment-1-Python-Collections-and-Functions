#Task 1 

scores = [75, 90, 60, 85, 90, 50, 75, 95]

# 1. Unique scores in descending order
unique_scores = sorted(set(scores), reverse=True)
print("Unique scores:", unique_scores)

# 2. Scores >= 70, preserving duplicates
high_scores = [score for score in scores if score >= 70]
print("Scores >= 70:", high_scores)

# 3. Second-highest distinct score and average
second_highest = sorted(set(scores), reverse=True)[1]
average = sum(scores) / len(scores)

print("Second-highest score:", second_highest)
print("Average:", average)

# 4. Replace scores below 60 with 60
updated_scores = [60 if score < 60 else score for score in scores]
print("Updated scores:", updated_scores)

# 5. Frequency dictionary
frequency = {}

for score in scores:
    frequency[score] = frequency.get(score, 0) + 1

print("Frequency:", frequency)

# 6. sort() vs sorted()
''' 
sort() Changes original list
sorted() Returns None doesnt Changes original list , its make a new list 
'''

# Expected output
'''
Unique scores: [95, 90, 85, 75, 60, 50]
Scores >= 70: [75, 90, 85, 90, 75, 95]
Second-highest score: 90
Average: 75.0
Updated scores: [75, 90, 60, 85, 90, 60, 75, 95]
Frequency: {75: 2, 90: 2, 60: 1, 85: 1, 50: 1, 95: 1}
'''

#Task 2 

python_students = {"Ahmed", "Sara", "Omar", "Mona"}
sql_students = {"Sara", "Mona", "Ali", "Youssef"}

# 1. Compare both sets
both_courses = python_students & sql_students
either_course = python_students | sql_students
exactly_one = python_students ^ sql_students

print("Both courses:", sorted(both_courses))
print("Either course:", sorted(either_course))
print("Exactly one course:", sorted(exactly_one))

# 2. Students enrolled in Python only and SQL only
python_only = python_students - sql_students
sql_only = sql_students - python_students

print("Python only:", sorted(python_only))
print("SQL only:", sorted(sql_only))

# 3. Check whether every SQL student is enrolled in Python
is_subset = sql_students <= python_students

print("Every SQL student is in Python:", is_subset)

# 4. Update the sets
python_students.add("Nour")
sql_students.discard("Ali")

print("Updated Python students:", sorted(python_students))
print("Updated SQL students:", sorted(sql_students))

# 5. Count distinct students after updates
total_students = len(python_students | sql_students)

print("Total distinct students:", total_students)

''' 
Expected output

Students in both courses:
{'Sara', 'Mona'}

Students in either course:
{'Ahmed', 'Sara', 'Omar', 'Mona', 'Ali', 'Youssef'}

Students in exactly one course:
{'Ahmed', 'Omar', 'Ali', 'Youssef'}

Python only:
{'Ahmed', 'Omar'}

SQL only:
{'Ali', 'Youssef'}

Is SQL students a subset of Python students?
False

Python students after adding Nour:
{'Ahmed', 'Sara', 'Omar', 'Mona', 'Nour'}

SQL students after removing Ali:
{'Sara', 'Mona', 'Youssef'}

Total distinct students:
6
'''

########################################################################################
#Task 3 
sales = {
    "Laptop": 25000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 7000
}

# Add a new product
sales["Headphones"] = 1800

# Update existing product
sales["Mouse"] = 650

print(sales)

# Calculate total sales
total_sales = sum(sales.values())

# Find product with highest sales
highest_product = max(sales, key=sales.get)

print("Total sales:", total_sales)
print("Highest selling product:", highest_product)
print("Highest sales value:", sales[highest_product])

high_sales = {
    product: value
    for product, value in sales.items()
    if value > 1500
}

print(high_sales)

printer_sales = sales.get("Printer", 0)

print(printer_sales)

sorted_products = sorted(sales, key=sales.get, reverse=True)

print(sorted_products)

sales_percentage = {
    product: round((value / total_sales) * 100, 2)
    for product, value in sales.items()
}

print(sales_percentage)

''' 
Expected output
Updated sales:
{'Laptop': 25000, 'Mouse': 650, 'Keyboard': 1200, 'Monitor': 7000, 'Headphones': 1800}

Total sales: 35650

Highest selling product: Laptop

Products above 1500:
{'Laptop': 25000, 'Monitor': 7000, 'Headphones': 1800}

Printer price: 0

Products sorted by sales:
['Laptop', 'Monitor', 'Headphones', 'Keyboard', 'Mouse']

Sales percentages:
{'Laptop': 70.13, 'Mouse': 1.82, 'Keyboard': 3.37, 'Monitor': 19.64, 'Headphones': 5.05}

'''

####################################################################
#Task 4 
# 1. Calculate average
def calculate_average(scores):
    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)


# 2. Get pass/fail result
def get_result(score, passing_score=60):
    if score >= passing_score:
        return "Pass"
    else:
        return "Fail"


# 3. Summarize student
def summarize_student(name, scores):
    average = calculate_average(scores)
    result = get_result(average)

    return {
        "name": name,
        "average_score": average,
        "result": result
    }


# 4 & 5. Testing
print(calculate_average([]))
print(summarize_student("Ali", [50, 60, 70]))
print(get_result(65, passing_score=70))

# Positional arguments
print(summarize_student("Omar", [80, 90, 70]))

# Keyword arguments
print(summarize_student(name="Sara", scores=[90, 80, 100]))


# 6. Count Pass/Fail results
def count_results(summaries):
    counts = {
        "Pass": 0,
        "Fail": 0
    }

    for student in summaries:
        result = student["result"]
        counts[result] += 1

    return counts


# Test count_results
summaries = [
    summarize_student("Omar", [80, 90, 70]),
    summarize_student("Ali", [40, 50, 30]),
    summarize_student("Sara", [60, 60, 60]),
    summarize_student("Mona", [20, 30, 40])
]

print(count_results(summaries))
print(count_results([]))

''' 
Expected output
Average of empty list: 0

Student summary:
{'name': 'Ali', 'average_score': 60.0, 'result': 'Pass'}

Result for score 65 with passing score 70:
Fail

Positional arguments:
{'name': 'Omar', 'average_score': 80.0, 'result': 'Pass'}

Keyword arguments:
{'name': 'Sara', 'average_score': 90.0, 'result': 'Pass'}

Empty result counts:
{'Pass': 0, 'Fail': 0}

'''
###################################################################
#Task 5 
students = [
    {"name": "Ahmed", "scores": [80, 75, 90]},
    {"name": "Sara", "scores": [95, 88, 92]},
    {"name": "Omar", "scores": [45, 60, 50]},
    {"name": "Mona", "scores": [70, 65, 75]}
]

# 1. Create student summaries
summaries = []

for student in students:
    summary = summarize_student(student["name"], student["scores"])
    summaries.append(summary)


# 2. Rank students by average score (descending)
ranked_students = sorted(
    summaries,
    key=lambda student: student["average_score"],
    reverse=True
)


# 3. Filter passing students
passing_students = list(
    filter(lambda student: student["result"] == "Pass", summaries)
)


# 4. Extract passing students' names
passing_names = list(
    map(lambda student: student["name"], passing_students)
)


# 5. Print ranked students
for student in ranked_students:
    print(
        f"{student['name']} | "
        f"Average: {student['average_score']:.2f} | "
        f"Result: {student['result']}"
    )


# 6. Count passing and failing students
result_counts = count_results(summaries)

print("\nResult counts:", result_counts)
print("Passing students:", passing_names)


# 7. Sort alphabetically by student name
alphabetical_students = sorted(
    summaries,
    key=lambda student: student["name"]
)

print("\nAlphabetical order:")

for student in alphabetical_students:
    print(student["name"])
    
''' 
Expected output
Ranked Students:
Sara | Average: 91.67 | Result: Pass
Ahmed | Average: 81.67 | Result: Pass
Mona | Average: 70.00 | Result: Pass
Omar | Average: 51.67 | Result: Fail

Result counts:
{'Pass': 3, 'Fail': 1}

Passing students:
['Ahmed', 'Sara', 'Mona']

Alphabetical:
Ahmed
Mona
Omar
Sara
'''
    
##########################################################
#Task 6 

#**1. Why is a set suitable for removing duplicates, and what happens to the original ordering?**

#A set is suitable for removing duplicates because it stores only unique elements. However, it does not preserve the original ordering of the elements. The original list remains unchanged when converting it to a set.


#**2. Explain the difference between print() and return inside a function.**

#`print()` displays a value on the screen, but it does not return that value to the caller. `return` sends a value back from the function, allowing it to be stored in a variable or used in other calculations.

#**3. Explain one limitation of lambda expressions compared with functions defined using def.**

#Lambda expressions are limited to a single expression, so they are suitable for simple operations. Unlike functions defined using `def`, they cannot contain multiple statements or complex logic, making `def` more suitable for larger functions.


################################################################
#Task 7 
customers = [
    {"id": 101, "name": " Ahmed ", "city": "cairo"},
    {"id": 102, "name": "Sara", "city": "GIZA"},
    {"id": 101, "name": "Ahmed", "city": "Cairo"},
    {"id": 103, "name": " Omar", "city": "cairo"},
    {"id": 104, "name": "Mona ", "city": "giza"}
]


def clean_customers(records):
    if not records:
        return []

    cleaned = []
    seen_ids = set()
    city_counts = {}

    for customer in records:

        # Remove duplicate IDs, keeping the first occurrence
        if customer["id"] in seen_ids:
            continue

        seen_ids.add(customer["id"])

        # Clean the customer record
        cleaned_record = {
            "id": customer["id"],
            "name": customer["name"].strip(),
            "city": customer["city"].title()
        }

        cleaned.append(cleaned_record)

        # Count unique customers per city
        city = cleaned_record["city"]
        city_counts[city] = city_counts.get(city, 0) + 1

    return cleaned, city_counts


# Call the function
cleaned_customers, city_counts = clean_customers(customers)

# Display original data
print("Original Customers:")
print(customers)

# Display cleaned data
print("\nCleaned Customers:")
print(cleaned_customers)

# Display city counts
print("\nCity Counts:")
print(city_counts)

# Test empty list
print("\nEmpty Test:")
print(clean_customers([]))

''' 
Expected output

Original Customers:
[
 {'id': 101, 'name': ' Ahmed ', 'city': 'cairo'},
 {'id': 102, 'name': 'Sara', 'city': 'GIZA'},
 {'id': 101, 'name': 'Ahmed', 'city': 'Cairo'},
 {'id': 103, 'name': ' Omar', 'city': 'cairo'},
 {'id': 104, 'name': 'Mona ', 'city': 'giza'}
]

Cleaned Customers:
[
 {'id': 101, 'name': 'Ahmed', 'city': 'Cairo'},
 {'id': 102, 'name': 'Sara', 'city': 'Giza'},
 {'id': 103, 'name': 'Omar', 'city': 'Cairo'},
 {'id': 104, 'name': 'Mona', 'city': 'Giza'}
]

City Counts:
{'Cairo': 2, 'Giza': 2}

Empty Test:
[]
'''
##########################################################
#Task 8 
orders = [
    {"customer": "Ahmed", "amount": 1200, "status": "Completed"},
    {"customer": "Sara", "amount": 850, "status": "Completed"},
    {"customer": "Ahmed", "amount": 400, "status": "Cancelled"},
    {"customer": "Omar", "amount": 600, "status": "Completed"},
    {"customer": "Sara", "amount": 300, "status": "Completed"}
]


# 1. Summarize completed orders per customer
def summarize_orders(orders):
    if not orders:
        return {}

    totals = {}

    for order in orders:
        if order["status"] == "Completed":
            customer = order["customer"]
            amount = order["amount"]

            totals[customer] = totals.get(customer, 0) + amount

    return totals


# 2. Calculate customer totals
totals = summarize_orders(orders)

print("Customer Totals:")
print(totals)


# 3. Sort customer totals in descending order using lambda
sorted_totals = sorted(
    totals.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nSorted Totals:")
print(sorted_totals)


# 4. Highest customer total and overall completed revenue
top_customer = max(totals, key=totals.get)
highest_total = totals[top_customer]

overall_revenue = sum(totals.values())

print("\nTop Customer:")
print(top_customer, highest_total)

print("\nOverall Completed Revenue:")
print(overall_revenue)


# 5. Return customers above a minimum amount
def get_customers_above(totals, minimum=1000):
    return sorted([
        name
        for name, amount in totals.items()
        if amount > minimum
    ])


# Test default minimum
print("\nCustomers above default minimum:")
print(get_customers_above(totals))

# Test custom minimum
print("\nCustomers above custom minimum (500):")
print(get_customers_above(totals, minimum=500))

''' 
Expected output

Customer Totals:
{'Ahmed': 1200, 'Sara': 1150, 'Omar': 600}

Sorted Totals:
[('Ahmed', 1200), ('Sara', 1150), ('Omar', 600)]

Top Customer:
Ahmed 1200

Overall Completed Revenue:
2950

Customers above default minimum:
['Ahmed', 'Sara']

Customers above custom minimum (500):
['Ahmed', 'Omar', 'Sara']

'''


###############################################################
## Task 9
'''
**1. What happens when you assign a new value to a dictionary key that already exists?**

When you assign a new value to an existing dictionary key, the old value is replaced with the new value. If the key does not exist, a new key-value pair is added to the dictionary.

**2. Explain the difference between remove() and discard() for sets.**

Both `remove()` and `discard()` remove an element from a set if it exists. However, `remove()` raises a `KeyError` if the element is missing, while `discard()` does not raise an error.
**3. Why should you avoid modifying a list while iterating over that same list?**

Modifying a list while iterating over it can cause elements to be skipped because their indices shift when items are removed. This may lead to unexpected results. It is safer to create a new list or iterate over a copy.

**4. What do map() and filter() return in Python 3, and how can you display their results as lists?**

In Python 3, `map()` and `filter()` return iterators, not lists. `map()` applies a function to each element, while `filter()` selects elements that satisfy a condition. Their results can be converted into lists using the `list()` function.

**5. Explain why averages should be rounded for display after determining pass or fail.**

Averages should be rounded for display only after determining pass or fail because rounding can change the value and lead to an incorrect result. Using the original average ensures accurate comparisons with the passing score, while rounding is only used to make the displayed value easier to read.
'''
