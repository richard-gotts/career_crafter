"""
This program is designed to validate data that an applicant enters into a career application site,
'CareerCrafter'. The program will generate a file which can be loaded in the employer application.

The applicant will provide the following details:

- Name and surname
- Email address
- Phone number
- Age
- Location (and whether they are willing to relocate/travel for on-site work)
- Programming languages

"""

import re
import os

# == Gather applicant details ==
app_details = {}

print("\n\033[1m" + "Welcome to CareerCrafter for applicants!" + "\033[0m")

# Name and surname
app_details["Name"] = input("\nPlease enter your first name: ")
app_details["Surname"] = input("\nPlease enter your surname: ")

# Email address
VALID_EMAIL_PATTERN = r"^\S+@\S+\.\S+$"
app_details["Email"] = input("\nPlease enter your email address: ")
while not re.fullmatch(VALID_EMAIL_PATTERN, app_details["Email"]):
    app_details["Email"] = input("Email address not valid. Please try again: ")

# Phone number
app_details["Phone number"] = input("\nPlease enter your phone number: ").replace(" ", "")
while not app_details["Phone number"].isnumeric() or len(app_details["Phone number"]) != 11:
    app_details["Phone number"] = input("Invalid phone number. Please enter 11 digits and omit "
                                        "the dialling code: ").replace(" ", "")

# Age
app_details["Age"] = input("\nPlease enter your age: ")
while not app_details["Age"].isnumeric():
    app_details["Age"] = input("Please enter a valid age: ")

# Location
uk_regions = ["East of England", "East Midlands", "London", "North East", "North West",
              "South East", "South West", "West Midlands", "Yorkshire and the Humber"]

print("\nWhere are you based?\n")
for pos, region in enumerate(uk_regions):
    print(f"{pos + 1}. {region}")
region_num = input("\nPlease type the number corresponding to your region: ")
while not region_num.isnumeric() or int(region_num) not in range(1, len(uk_regions) + 1):
    region_num = input("Please enter a valid number: ")
for pos, region in enumerate(uk_regions):
    if pos == int(region_num) - 1:
        app_details["Location"] = region

travel_relocate = input("\nWould you be willing to relocate or travel to another region for work? "
                        "(y/n): ").lower()
while travel_relocate not in ["y", "n"]:
    travel_relocate = input("Please type either 'y' or 'n': ").lower()
if travel_relocate == "y":
    app_details["Travel/relocate"] = "Yes"
else:
    app_details["Travel/relocate"] = "No"

# Programming languages:
prog_langs = ["Python", "Java", "C and C++", "C#", "JavaScript", "SQL", "PHP", "Go", "Kotlin",
              "MATLAB", "R", "Swift", "Rust", "Ruby", "Dart", "Scala"]
app_langs = []
print("\nWhich programming languages can you use?\n")
for pos, lang in enumerate(prog_langs):
    print(f"{pos + 1}. {lang}")
FINISHED_ADDING = False
while not FINISHED_ADDING:
    lang_num = input("\nTo add a programming language, please type the corresponding number, or "
                     "type '0' to finish adding: ")
    while not lang_num.isnumeric() or int(lang_num) not in range(0, len(prog_langs) + 1):
        lang_num = input("Please enter a valid number: ")
    if int(lang_num) == 0:
        app_details["Programming languages"] = ",".join(app_langs)
        FINISHED_ADDING = True
    else:
        for pos, lang in enumerate(prog_langs):
            if pos == int(lang_num) - 1:
                if lang in app_langs:
                    print(f"\n{lang} already added!")
                else:
                    app_langs.append(lang)
                    print(f"\n{lang} successfully added.")

# == Create application file ==
current_dir = os.path.dirname(__file__)
APPLICATIONS = os.path.join(current_dir, "Applications\\")

with open(APPLICATIONS + \
          f"{app_details["Surname"]}{app_details["Name"][0]}{app_details["Phone number"][7:]}.txt",\
              "w", encoding = "utf-8") as application:
    for category, detail in app_details.items():
        application.write(f"{category}:{detail}\n")

print("\033[1m" + "\nApplication submitted! Thank you for using CareerCrafter.\n" + "\033[0m")
