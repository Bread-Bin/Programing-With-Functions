print("Company I.D. Badge")
print("Please enter in the following information.")
print(" ")
name_f = input("First Name: ")
name_l = input("Last Name: ")
email = input("Email Adress: ")
phone = input("Phone Number: ")
job_t = input("Job Title: ")
id_num = input("I.D. Number: ")
hair_c = input("Hair Color: ")
eye_c = input("Eye Color: ")
month = input("Hiring Month: ")
train = input("Training: ")
print(" ")

format = f'''The ID Card is:
----------------------------------------
{name_l.upper()}, {name_f}
{job_t.title()}
ID: {id_num}

{email.lower()}
{phone}

Hair: {hair_c.capitalize()}           Eyes: {eye_c.capitalize()}
Month: {month.capitalize()}           Training: {train.capitalize()} 
----------------------------------------'''

print(format)