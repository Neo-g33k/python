# Detection d'un anagramme
def anagramme(mot1, mot2):
    """
    cette fonction est sensé returné une liste des anagrammes trouveé
    est s'll y a pas d'anagramme dans le dictionnaire présent dans le
    programme, elle return rien: ***
    * Paramettre:
        mot = correspond à mot au quel l'algorithme doit trouvé ces anagramme
    * return:
        list : correspond à la liste des anagrammes trouvé dans le mot
        False : S'il y a pas d'anagramme, elle return un booléen faux
    """
    if((mot1 and mot2) !=""):
        if (len(mot1) > len(mot2))  or (len(mot2) > len(mot1)):
            return "N'est le pas!"
        else:
            if(sorted(mot1) == sorted(mot2)):
                return "C'est un anagramme"
            else:
                return "Nonon" 
    else:
        return ("Error : L'un de mot est vide !")

# ==========================================
print("===========================================")
print("Generateur anagramme simple sur un seul mot")
print("===========================================\n")

word1 = input("Entrer 1er mot : ")
word2 = input("Entrer le 2e mot :")

is_anagram = anagramme(word1, word2)

if (is_anagram == True):
    print("\n-- {}".format(is_anagram))
    print("-----------------------------")

elif(is_anagram == False):
    print("-- {}".format(is_anagram))
    print("-----------------------------")
else:
    print(is_anagram)