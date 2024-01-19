# Career Crafter

This is a set of two programs which collect and validate employer requirements and applicant details.

The current workings of the programs are as follows:

- Applicants can enter their details by running the 'career_crafter_applicants.py' program.
- Once they have successfully added all their details, a .txt file is created in the 'Applications' folder.
- The employer can then enter their requirements by running the 'career_crafter_employers.py' program.
- Once they have successfully added their requirements, the program will read in each application and generate a .txt report for that application.
- For applications which may be successful, the reports are added to the 'Employer Reports\\Successful Applications' folder.
- For applications which are unsuccessful, the reports are added to the 'Employer Reports\\Unsuccessful Applications' folder.

To use the set of programs, please ensure that you store the program files in the same working directory. Please also create two folders in this directory: 'Applications' and 'Employer Reports'. The 'Employer Reports' folder should contain two sub-folders: 'Successful Applications' and 'Unsuccessful Applications'. **Unfortunately, failure to set up the directory in this way will mean that the programs won't run as intended!**

I appreciate that this is a rather primitive setup and would not be anywhere near suitable for a real career match site! The main purpose of this project was to practise reading and writing .txt files and input validation.

The vision with this project would be to have online portals for the employer and applicants - I look forward to learning more about how to implement this!
