skills = ["Python", "SQL", "Power BI", "Excel", "Git", "Machine Learning"]

# Print first skill
print("First Skill:", skills[0])

# Print last skill
print("Last Skill:", skills[-1])

# Print number of skills
print("Total Skills:", len(skills))

# Add a new skill
skills.append("GenAI")

# Remove one skill
skills.remove("Excel")

# Print final list
print("Updated Skills List:", skills)
companies = ["SAP", "BMW", "Siemens", "Bosch", "Mercedes-Benz"]

for company in companies:
    print(f"I will apply to {company} in January 2027!")

# Sort the list
companies.sort()

print("\nCompanies in Alphabetical Order:")

for company in companies:
    print(company)
    marks = [85, 90, 78, 88, 95]

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    total += mark

average = total / len(marks)

print(f"Marks: {marks}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Average Marks: {average:.2f}")

