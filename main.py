from generator import generate_password
choice = input("1 = Check password\n2 = Generate password\nChoose: ")

if choice == "2":
    print("\nGenerated password:", generate_password())
    exit()

from password_checker import check_strength
from colorama import Fore, Style, init

init()

print("Password Strength Analyzer\n")

password = input("Enter password: ")

strength, entropy, feedback = check_strength(password)

color = Fore.RED
if strength == "Medium":
    color = Fore.YELLOW
elif strength == "Strong":
    color = Fore.GREEN

print("\nStrength:", color + strength + Style.RESET_ALL)
print("Entropy Score:", entropy)

if feedback:
    print("\nSuggestions:")
    for f in feedback:
        print("-", f)
else:
    print(Fore.GREEN + "\nExcellent password!" + Style.RESET_ALL)
with open("report.txt", "w") as f:
    f.write(f"Password: {password}\n")
    f.write(f"Strength: {strength}\n")
    f.write(f"Entropy: {entropy}\n")
