# creation d'un objet time
from datetime import datetime



def formatDate(birthday):
    out = birthday.split("/")
    return out

def yourBirthdayIn(day):
    bday = datetime(day[0], day[1], day[2])
    tday = datetime.now()
    if((bday.year < tday.year) or (bday.hour < tday.hour) or (bday.days < tday.days)):
        return ("Votre anniversaire est déjà passsé")
    else:
        stey_day = bday - tday
        retun ("Votre anniversaire est dans :{}".format(stey_day))

day = input("Entrer la date au format : AAAA/MM/JJ\nBirthday >> ")
day2 = formatDate(day)       

print(yourBirthdayIn(day2))