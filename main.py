import json
import random
from datetime import datetime

name = input("Enter your name: ")

print(f"\nHello {name}! Welcome to Smart Student Assistant")

with open("tips.json", "r") as file:
    data = json.load(file)

while True:

    print("\n===== SMART STUDENT ASSISTANT =====")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        result = random.choice(data["study_tips"])
        print("\nStudy Tip:")
        print(result)

    elif choice == "2":
        result = random.choice(data["motivation_quotes"])
        print("\nMotivation Quote:")
        print(result)

    elif choice == "3":
        result = str(datetime.now())
        print("\nCurrent Date & Time:")
        print(result)

    elif choice == "4":
        print("Thank you for using Smart Student Assistant!")
        break

    else:
        print("Invalid option.")
        continue

    with open("output.txt", "a") as file:
        file.write(f"{name}: {result}\n")

    print("\nSaved to output.txt")