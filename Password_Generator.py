import random
import time

compteur = 0 #compteur pour boucle while
mdp = 0 #définition du mot de passe final
check = 'non' #le check est sur non de base pour que la boucle recrée un mot de passe tant qu'il nous plait pas
data = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','#','/',';','.','?',':','_','-']
#la data est une liste qui va contenir tout les caractères pour le mot de passe
app_mdp = str(input("Pour quel application voulez-vous générer un nouveau mot de passe ? ")) #on définit le nom de l'app correspondant au mot de passe
mdp_length = int(input("De Combien de caractère voulez-vous que le mot de passe soit constitué ? ")) #le mot de passe peut contenir autant de caractères que voulu
while check == 'non': #tant que le mot de passe ne plait pas la boucle tourne
    mdp = "" #le mot de passe est remis à 0 avant chaque boucle
    while compteur<mdp_length: #le compteur doit atteindre le nombre de caractère voulu par l'utilisateur
        compteur = compteur+1
        mdp = mdp + random.choice(data) #chaque caractère est pris aléatoirement dans la liste, et est ajouté au caractère précédemment choisi
    compteur = 0 #compteur remis à 0 pour se préparer à une autre boucle
    print(mdp)
    check = input("Ce mot de passe vous convient-il ? (oui/non)\n") #si oui, on quitte la boucle, sinon elle recommence
print("Votre mot de passe " + app_mdp + " est : " + mdp + '\n')

fichier = open("mot_de_passe.txt", "a") #on crée un fichier en mode ajout de valeur, si le fichier n'existe pas il le crée
fichier.write(app_mdp + " : " + mdp + '\n') #ajout du mot de passe dans un fichier avec légere mise en page pour être plus lisible
fichier.close() #ferme la fonction fichier, plus rien ne se passera dedans

print("Le nouveau mot de passe est maintenant enregistré dans 'mot_de_passe.txt'")
time.sleep(5)
exit()
