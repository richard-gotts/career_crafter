"""
This program is designed to validate data that an employer enters into a career application site, 
'CareerCrafter'. The program can also receive details from applicants and provide a report based on
their suitability for the role.

Employers can pre-load the program with details and requirements about their job. For example:

- Minimum age
- Location (on-site/remote)
- Favourable programming languages

They will receive the following details from applicants:

- Name and surname
- Email address
- Phone number
- Age
- Location (and whether they are willing to relocate/travel for on-site work)
- Programming languages

The program will compare employer requirements with applicant details and provide a custom report.
"""

import os

# == Gather employer requirements ==
employer_req = {}

print("\n\033[1m" + "Welcome to CareerCrafter for employers!" + "\033[0m")

# Minimum age
employer_req["Minimum age"] = input("\nWhat is the minimum age for applicants? ")
while not employer_req["Minimum age"].isnumeric():
    employer_req["Minimum age"] = input("Please enter a valid age: ")

# Location
on_site = input("\nDoes the job require the applicant to be on-site? (y/n) ").lower()
while on_site not in ["y", "n"]:
    on_site = input("Please type either 'y' or 'n': ").lower()
if on_site == "y":
    employer_req["On-site/remote"] = "On-site"
else:
    employer_req["On-site/remote"] = "Remote"

uk_regions = ["East of England", "East Midlands", "London", "North East", "North West",
              "South East", "South West", "West Midlands", "Yorkshire and the Humber"]

if employer_req["On-site/remote"] == "On-site":
    print("\nWhere would the applicant be working?\n")
    for pos, region in enumerate(uk_regions):
        print(f"{pos + 1}. {region}")
    region_num = input("\nPlease type the number corresponding to your region: ")
    while not region_num.isnumeric() or int(region_num) not in range(1, len(uk_regions) + 1):
        region_num = input("Please enter a valid number: ")
    for pos, region in enumerate(uk_regions):
        if pos == int(region_num) - 1:
            employer_req["Location"] = region
else:
    employer_req["Location"] = "N/A"

# Favourable programming languages:
prog_langs = ["Python", "Java", "C and C++", "C#", "JavaScript", "SQL", "PHP", "Go", "Kotlin",
              "MATLAB", "R", "Swift", "Rust", "Ruby", "Dart", "Scala"]
req_langs = []
print("\nWhich programming languages should the applicant be able to use?\n")
for pos, lang in enumerate(prog_langs):
    print(f"{pos + 1}. {lang}")
FINISHED_ADDING = False
while not FINISHED_ADDING:
    lang_num = input("\nTo add a programming language, please type the corresponding number, or "
                     "type '0' to finish adding: ")
    while not lang_num.isnumeric() or int(lang_num) not in range(0, len(prog_langs) + 1):
        lang_num = input("Please enter a valid number: ")
    if int(lang_num) == 0:
        employer_req["Programming languages"] = req_langs
        FINISHED_ADDING = True
    else:
        for pos, lang in enumerate(prog_langs):
            if pos == int(lang_num) - 1:
                if lang in req_langs:
                    print(f"\n{lang} already added!")
                else:
                    req_langs.append(lang)
                    print(f"\n{lang} successfully added.")

# == Load applications and write reports ==
current_dir = os.path.dirname(__file__)
APPLICATIONS = os.path.join(current_dir, "Applications\\")
POS_REPORTS = os.path.join(current_dir, "Employer Reports\\Successful Applications\\")
NEG_REPORTS = os.path.join(current_dir, "Employer Reports\\Unsuccessful Applications\\")

NUM_SUCCESSFUL = 0
NUM_UNSUCCESSFUL = 0

for file in os.listdir(APPLICATIONS):
    # Load applicant details
    app_details = {}
    with open(APPLICATIONS + file, "r", encoding = "utf-8") as application:
        for line in application:
            line_info = line.split(":", 1)
            line_info[1] = line_info[1][:-1]
            app_details[line_info[0]] = line_info[1]

    app_details["Programming languages"] = app_details["Programming languages"].split(",")

    # Check against employer requirements
    AGE_MATCH = False
    LOCATION_MATCH = False
    LANGUAGES_MATCH = False
    fail_reasons = []

    if int(app_details["Age"]) >= int(employer_req["Minimum age"]):
        AGE_MATCH = True
    else:
        fail_reasons.append("The applicant is not old enough.")

    if employer_req["On-site/remote"] == "Remote":
        LOCATION_MATCH = True
    elif app_details["Travel/relocate"] == "Yes":
        LOCATION_MATCH = True
    elif app_details["Location"] == employer_req["Location"]:
        LOCATION_MATCH = True
    else:
        fail_reasons.append("The applicant is not willing to travel or relocate.")

    lang_matches = []
    lang_extras = []

    for lang in app_details["Programming languages"]:
        if lang in employer_req["Programming languages"]:
            lang_matches.append(lang)
        else:
            lang_extras.append(lang)

    if len(lang_matches) != 0:
        LANGUAGES_MATCH = True
    else:
        fail_reasons.append("The applicant can't use any of the required programming languages.")

    # Write report for successful application
    if AGE_MATCH and LOCATION_MATCH and LANGUAGES_MATCH:
        NUM_SUCCESSFUL += 1
        with open(POS_REPORTS + \
                f"{app_details["Surname"]}{app_details["Name"]}{app_details["Phone number"]}.txt", \
                    "w", encoding = "utf-8") as report:
            report.write(f"{app_details["Name"]} {app_details["Surname"]}\n\n".upper())
            report.write(f"Contact details:\n{app_details["Email"]}\n{app_details["Phone number"]}")
            report.write(f"\n\nAge: {app_details["Age"]}\nLocation: {app_details["Location"]}\n")
            if employer_req["On-site/remote"] == "On-site" and \
                app_details["Location"] != employer_req["Location"]:
                report.write("Applicant is willing to travel or relocate.\n")
            if lang_matches:
                report.write(f"\nApplicant can use {len(lang_matches)} out of "
                             f"{len(employer_req["Programming languages"])} required language(s):")
                for lang in lang_matches:
                    report.write(f"\n\t- {lang}")
                report.write("\n")
            if lang_extras:
                report.write(f"\nApplicant can use {len(lang_extras)} additional language(s):")
                for lang in lang_extras:
                    report.write(f"\n\t- {lang}")
    else:
        NUM_UNSUCCESSFUL += 1
        with open(NEG_REPORTS + \
                f"{app_details["Surname"]}{app_details["Name"]}{app_details["Phone number"]}.txt", \
                    "w", encoding = "utf-8") as report:
            report.write(f"{app_details["Name"]} {app_details["Surname"]}\n\n".upper())
            report.write(f"Contact details:\n{app_details["Email"]}\n{app_details["Phone number"]}")
            report.write(f"\n\nAge: {app_details["Age"]}\nLocation: {app_details["Location"]}\n")
            if LOCATION_MATCH and employer_req["On-site/remote"] == "On-site" and \
                app_details["Location"] != employer_req["Location"]:
                report.write("Applicant is willing to travel or relocate.\n")
            report.write("\nREASON(S) FOR FAILURE:")
            for reason in fail_reasons:
                report.write(f"\n\t- {reason}")
            report.write("\n")
            if lang_matches:
                report.write(f"\nApplicant can use {len(lang_matches)} out of "
                             f"{len(employer_req["Programming languages"])} required language(s):")
                for lang in lang_matches:
                    report.write(f"\n\t- {lang}")
                report.write("\n")
            if lang_extras:
                report.write(f"\nApplicant can use {len(lang_extras)} additional language(s):")
                for lang in lang_extras:
                    report.write(f"\n\t- {lang}")

print(f"\nYou have {NUM_SUCCESSFUL} successful and {NUM_UNSUCCESSFUL} unsuccessful application(s) "
      "waiting for you.\n\n" + "\033[1m" + "Thank you for using CareerCrafter.\n" + "\033[0m")
