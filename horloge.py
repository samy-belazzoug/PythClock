import time # sleep()
from dataclasses import dataclass # @dataclass

@dataclass
class Temps:
    heure:int
    minute:int
    seconde:int

def formattage_temps(temps:Temps)->str:
    return f'{temps.heure}:{temps.minute}:{temps.seconde}'

def mise_a_jour_temps(temps:Temps)->Temps:
    temps.seconde += 1
    if temps.seconde > 59:
        temps.minute += 1; temps.seconde = 0
    if temps.minute > 59:
        temps.heure += 1; temps.minute = 0; temps.seconde = 0
    if temps.heure > 23:
        temps.heure = 0; temps.minute = 0; temps.seconde = 0
    return temps


if __name__ == "__main__":
    temps = Temps(23,58,55)
    while True:
            time.sleep(1)
            mise_a_jour_temps(temps)
            print(formattage_temps(temps))