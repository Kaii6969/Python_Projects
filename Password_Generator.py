import random
import time

compteur = 0 #counter for while loop
mdp = 0 #password creation
check = 'no' #check is on 'no' by default, which never stop the loop
data = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','#','/',';','.','?',':','_','-']
#data represent every character that the password will contain
app_mdp = str(input("For which application do you want to generate a new password?")) #the name of the app that matches with the password
mdp_length = int(input("How many characters do you want the password to be?")) #the password can contain as many character as you want
while check == 'no': #while password isn't okay for you, the loop continue
    mdp = "" #password is set to 0 before every loop
    while compteur<mdp_length: #counter has to reach the user's will
        compteur = compteur+1
        mdp = mdp + random.choice(data) #each character is randomly picked, and is added to the last one freshly picked
    compteur = 0 #counter set to 0 and getting ready for another loop
    print(mdp)
    check = input("Is this password right for you ? (yes/no)\n") #if yes, break the loop, else, the loop start again
print("Your Password for " + app_mdp + " is : " + mdp + '\n')

fichier = open("password.txt", "a") #creating a file in adding mode, if the file doesn't exist, python create it
fichier.write(app_mdp + " : " + mdp + '\n') #the password is added in the file
fichier.close()

print("This new password is now save in 'password.txt'")
time.sleep(5)
exit()
