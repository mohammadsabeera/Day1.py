# Task 1

profile = {
    "name": "Mohammad Sabeera",
    "college": "Your College Name",
    "cgpa": 8.5,
    "year": "3rd Year",
    "dream_company": "SAP",
    "german_level": "A1",
    "github_projects": 6
}

print("----- My Profile -----")

for key, value in profile.items():
    print(f"{key} : {value}")
    # Task 2

company_salaries = {
    "SAP": 60000,
    "Siemens": 55000,
    "Zalando": 65000,
    "Bosch": 50000
}

highest_company = ""
highest_salary = 0

for company, salary in company_salaries.items():
    if salary > highest_salary:
        highest_salary = salary
        highest_company = company

print(f"Highest Paying Company: {highest_company}")
print(f"Salary: €{highest_salary}")