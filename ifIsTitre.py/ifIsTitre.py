# vérifié si c'est un text

def ifIsµTitle(chaine):
    """
    Ce fonction est sensé vérifié si le texte ou chaine entrée
    est un titre ou pas 
    """
    title_list  = []
    list_temp = chaine.split(" ")

    for title in list_temp:
        if (title.istitle()):
            title_list.append(title)
        else:
            False
    
    if(len(title_list) != 0):
        return title_list
    else:
        return ("The data that you give get not a tilte inside of this!")

print("Mini logiciel de tracker des titre ")
print("===================================")

print("\nVeuillez entrer la phrase ou un mot en bas :")
my_chaine = input(">> ")

all_titles = ifIsµTitle(my_chaine)

if (type(all_titles) != list):
    False
else:
    counter = 1
    for t in all_titles:
        print("Titre {0} : {1} ".format(counter, t))
        counter +=1