import time # sleep()
import keyboard # read_key()
import threading # Thread(), start()
from dataclasses import dataclass # @dataclass

etat = 1
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

def gestion_lecture_entree_clavier(temps:Temps):
    global etat
    while etat != 0:
        key_pressed = keyboard.read_key()
        if key_pressed == "space":
            time.sleep(0.3)
            if etat == 1:
                etat = 2
                print("pause.")
            else:
                etat = 1
                print("reprise du temps.")
        elif key_pressed == "esc":
            print("arrêt du temps.")
            etat = 0

def gestion_etat_horloge(temps:Temps):
    while etat != 0:
            if etat == 1:
                time.sleep(1)
                mise_a_jour_temps(temps)
                print(formattage_temps(temps), " ", etat)
            elif etat == 2:
                pass
            else:
                break

def affichage_temps_simple(temps:Temps):
    '''Affiche dans le terminal le temps à partir de 'temps' et se mets à jour toutes les secondes'''
    '''
    etat = 0 -> arrêt de l'horloge
    etat = 1 -> horloge tourne
    etat = 2 -> horloge en pause
    '''
    global etat
    thread_boucle_execution = threading.Thread(target=gestion_etat_horloge,args=(temps,))
    thread_io_operations = threading.Thread(target=gestion_lecture_entree_clavier,args=(temps,))
    thread_boucle_execution.start()
    thread_io_operations.start()
            
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
    temps24 = Temps(23,59,50)
    temps12 = Temps(12,59,55,False)
    # affichage_temps_alarme(temps12,Temps(1,0,0,False,True),"C'est l'heure!")
    affichage_temps_simple(temps24)