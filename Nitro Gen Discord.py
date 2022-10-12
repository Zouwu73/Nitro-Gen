
import random
import webbrowser
import time
from unittest import result

Chiffres = "0123456789"
Lettres = "abcdefghijklmnopqrstuvwxyz"
Lettres1 = "ABCDEFGHIJKLMNOP"
Lien =  "https://discord.gift/"

Tout = Chiffres + Lettres + Lettres1
longeur = 18

time.sleep(10)
##############
x = 40
###############
for i in range(x):
    
    Séquence = "".join(random.sample(Tout, longeur))

    result = Lien + Séquence
    
    webbrowser.open(result)
    print(result)
    
