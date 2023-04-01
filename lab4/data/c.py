from datetime import date
 
def age(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <  (birthDate.month, birthDate.day))
    return age

print(age(date(2005, 2, 8)), "years")