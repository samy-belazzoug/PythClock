import time # sleep()
from dataclasses import dataclass # @dataclass

@dataclass
class Temps: 
    '''Structure de données permettant la calculation d'un système d'horloge'''
    heure:int
    minute:int
    seconde:int
    format24:bool=True 
    '''Format 12h (False) ou 24h (True) (par défaut : True)'''
    pm:bool=False 
    '''AM (0, False) ou PM (1, True) (par défaut : False)'''

def formattage_temps(temps:Temps)->str:
    '''Permet d'avoir un affichage du temps au format hh:mm:ss au format 12h ou 24h'''
    heure = ""
    minute = ""
    seconde = ""
    # Gestion heures
    if temps.heure < 10:
         heure = "0" + str(temps.heure)
    else:
         heure = str(temps.heure)
    # Gestion minutes
    if temps.minute < 10:
         minute = "0" + str(temps.minute)
    else:
         minute = str(temps.minute)
    # Gestion secondes
    if temps.seconde < 10:
         seconde = "0" + str(temps.seconde)
    else:
         seconde = str(temps.seconde)
    # Gestion format du temps
    if not temps.format24:
        if not temps.pm:
            return f'{heure}:{minute}:{seconde} AM'
        else:
            return f'{heure}:{minute}:{seconde} PM'        
    else:
        return f'{heure}:{minute}:{seconde}'

def mise_a_jour_temps(temps:Temps)->Temps:
    '''Mets à jour le temps 'temps' pour s'assurer qu'il ait des valeures correctes'''
    temps.seconde += 1
    # Gestion secondes
    if temps.seconde > 59:
        temps.minute += 1; temps.seconde = 0
    # Gestion minutes
    if temps.minute > 59:
        temps.heure += 1; temps.minute = 0; temps.seconde = 0
    # Gestion heures selon format
    if not temps.format24:
        if temps.heure > 12:
            if not temps.pm:
                temps.pm = True
            else:
                temps.pm = False
            temps.heure = 1; temps.minute = 0; temps.seconde = 0
    else:
        if temps.heure > 23:
            temps.heure = 0; temps.minute = 0; temps.seconde = 0
    return temps

def affichage_temps_simple(temps:Temps):
    '''Affiche dans le terminal le temps à partir de 'temps' et se mets à jour toutes les secondes'''
    print(formattage_temps(temps))
    while True:
        time.sleep(1)
        mise_a_jour_temps(temps)
        print(formattage_temps(temps))

def comparer_temps(temps:Temps,delta:Temps)->bool:
    '''Compare deux temps et renvoie si ces temps sont les mêmes'''
    return temps.heure == delta.heure and temps.minute == delta.minute and temps.seconde == delta.seconde

def affichage_temps_alarme(temps:Temps,delta:Temps,message:str):
    '''Affiche dans le terminal le temps, se mets à jour toutes les secondes et s'arrête au temps 'delta' voulu en affichant 'message'.'''
    print(formattage_temps(temps))
    while (not comparer_temps(temps,delta)):
        comparer_temps(temps,delta)
        time.sleep(1)
        mise_a_jour_temps(temps)
        print(formattage_temps(temps))
    print(message)

if __name__ == "__main__":
    temps24 = Temps(23,59,50,)
    temps12 = Temps(12,59,55,False)
    affichage_temps_alarme(temps12,Temps(1,0,0,False,True),"C'est l'heure!")
    # affichage_temps_simple(temps)