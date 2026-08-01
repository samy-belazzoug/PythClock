import time # sleep()
from dataclasses import dataclass # @dataclass

@dataclass
class Temps: 
    '''Structure de données permettant la calculation d'un système d'horloge'''
    heure:int
    minute:int
    seconde:int

def formattage_temps(temps:Temps)->str:
    '''Permet d'avoir un affichage du temps au format hh:mm:ss'''
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
    # Gestion heures
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
    '''Affiche dans le terminal le temps, se mets à jour toutes les secondes et s'arrête au temps 'delta' voulu en afficheant 'message'.'''
    print(formattage_temps(temps))
    while (not comparer_temps(temps,delta)):
        comparer_temps(temps,delta)
        time.sleep(1)
        mise_a_jour_temps(temps)
        print(formattage_temps(temps))
    print(message)

if __name__ == "__main__":
    temps = Temps(23,59,50)
    affichage_temps_alarme(temps,Temps(0,0,0),"C'est l'heure!")
    # affichage_temps_simple(temps)