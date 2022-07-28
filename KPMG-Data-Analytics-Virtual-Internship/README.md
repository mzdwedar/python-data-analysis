# KPMG-Data-Analytics-Virtual-Internship

### Dataset:
[Sprocket Central Pty Ltd](https://docs.google.com/spreadsheets/d/1F8vZYniK4AXy3jiwsv7hEjGIE9-RE38KmtXnS9f3fe8/edit?usp=sharing)

### Data Quality assesment:
The ‘customer demographic’ has the following issues:
* Last_name, DOB, job_title, job_industry_category, tenure are incomplete (have missing values)
* Customer with id ‘34’ has DOB of ‘1843-12-21’ which makes her age 175 !
* Gender values are inconsistent i.e. F, femal, M, Female, and Male.
* It seems that the ‘default’ column has been parsed wrong, as the entries are incomprehensible.

The ‘customer address’ has the following issues:
* Customers with Customer_id (4001, 4002, 4003) aren’t associated with any entries in customer demographic.
* 'state' values are inconsistent i.e. 'New South Wales','NSW', 'Victoria','VIC'

The ‘transactions’ has the following issues:
* online _order, brand, product_line, product_class, product_size, and standard_cost aren incomplete.
* There are three transactions associated with customer_id of 5034, which isn’t associated with any entries in customer demographic.
* ‘Product_first_sold_date’ entries aren’t a date format.
