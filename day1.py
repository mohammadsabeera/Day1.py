print("Hello World!")
print("My name is Sabeera")
print("I will work at SAP Germany in 2028!")
# Creating variables
name = "Sabeera"
college = "DIET Ganguru"
year = 2028
cgpa = 8.5
dream_company = "SAP Germany"

# Printing variables
print(name)
print(college)
print(year)
print(cgpa)
print(dream_company)
is_student = True     # Boolean — only True or False

# Check the type
print(type(name))
print(type(year))
print(type(cgpa))
print(type(is_student))
print(f"My name is {name} and I will work at {dream_company} in {year}.")
# Salary Calculator

monthly = 4500

yearly_salary = monthly * 12
salary_after_tax = yearly_salary * 0.70   # 30% tax deducted
monthly_savings = monthly - (900 + 400)   # Rent = 900, Food = 400

print("Yearly Salary:", yearly_salary, "Euros")
print("Salary After 30% Tax:", salary_after_tax, "Euros")
print("Monthly Savings:", monthly_savings, "Euros")
name = "Mohammad Sabeera"
age = 20
city = "Hyderabad"
country = "India"
course = "B.Tech"
branch = "Data Science"
college = "Your College Name"
goal = "Become a Data Scientist in Germany"

print(f"""
==============================
         PROFILE CARD
==============================
Name      : {name}
Age       : {age}
City      : {city}
Country   : {country}
Course    : {course}
Branch    : {branch}
College   : {college}
Goal      : {goal}
==============================
""")