import random
import webbrowser
from unittest import result

Chiffres = "0123456789"
Lettres = "abcdefghijklmnopqrstuvwxyz"
Lettres1 = "ABCDEFGHIJKLMNOP"
Lien =  "https://discord.gift/"

Tout = Chiffres + Lettres + Lettres1
longeur = 18

for i in range(50):
    
    Séquence = "".join(random.sample(Tout, longeur))

    result = Lien + Séquence
    
    webbrowser.open(result)
    print(result)
