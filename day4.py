# Task 1
def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)

    print("BMI:", round(bmi, 2))

    if 18.5 <= bmi <= 24.9:
        print("Healthy")
    else:
        print("Not Healthy")

    return bmi


bmi_calculator(70, 1.75)

print("----------------------")


# Task 2
def germany_salary(monthly):
    yearly = monthly * 12
    after_tax = yearly * 0.70
    monthly_savings = monthly - 900 - 400

    print("Yearly Salary: €", yearly)
    print("After Tax Salary: €", after_tax)
    print("Monthly Savings: €", monthly_savings)


germany_salary(5000)

print("----------------------")


# Task 3
def is_sap_eligible(cgpa, has_github, german_level):

    if cgpa >= 7 and has_github == True and german_level >= "A1":
        return True
    else:
        return False


print(is_sap_eligible(8.2, True, "A1"))