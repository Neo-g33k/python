

texte = input("Enter the text : ")
i = 0

while i <= len(texte):
    print(sorted(texte))
    i +=1

    if i == len(texte):
        break
    else:
        continue
