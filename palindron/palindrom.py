# ce script permet de voir si le texte fournis par l'utilisateur est un palindrom


def palindrom(text):
    text_temp = text
    text_reversed = ""
    temp_list = reversed(text)
    
    for i in temp_list:
        text_reversed += i
    if (text_reversed.title() == text_temp.title()):
        return True
    else:
        return False

print("Bienvenue Palindrom detector soft version O1")
print("\n==========================================")


print("\n")

texte = input("Enter le mot :>> ")
is_palindrom = palindrom(texte)


if (is_palindrom == True):
    print("Le text entrer est un palindrom ")
else:
    print("Le texte entrer n'est pas un palindrom")


print("FIN DU PROGRAMME")

