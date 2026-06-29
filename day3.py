print("Multiplication Table of 7")

for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
    cities = ["Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne"]

for city in cities:
    print(f"I want to visit {city}!")
    savings = 0
months = 0

while savings < 10000:
    savings += 992
    months += 1
    print(f"Month {months}: €{savings}")

print(f"\nYou reached €10,000 in {months} months!")
