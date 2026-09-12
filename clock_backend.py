from time import sleep # sleep()
from keyboard import read_key # read_key()
import threading # Thread(), start()
from dataclasses import dataclass # @dataclass
import logging #basicConfig, error, info
import os # name, system() (yes, it's deprecated, but it works well, currently..) 

'''
etat = 0 -> Clock is stopped
etat = 1 -> Clock is running
etat = 2 -> Clock is paused
etat = 3 -> Alarm is triggered
'''
clock_state = 1
printing_state = 0

logging.basicConfig(filename='clock.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class Clock: 
    '''Data structure allowing clock system calculations'''
    hours:int
    minutes:int
    seconds:int
    format24:bool=True
    '''12h (False) or 24h (True) format (by default : True)'''
    pm:bool=False 
    '''AM (0, False) or PM (1, True) (by default : False)'''

def clock_validity(time:Clock):
    '''Checks if the Clock time is a valid time considering its parameters.'''
    # Hours
    if time.format24 == True:
        if 0 > time.hours or time.hours > 24:
            logging.error('User did not entered a valid hours in 24h format.')
            raise ValueError("\033[93mHours cannot be above 24 in a clock context using 24h hh:mm:ss format.")
    else:
        if 1 > time.hours or time.hours > 12:
            logging.error('User did not entered a valid hours in 12h format.')
            raise ValueError("\033[93mHours cannot be above 12 in a clock context using 12h hh:mm:ss format.") 

    # Minutes
    if 0 > time.minutes or time.minutes > 59:
        logging.error('User did not entered a valid hour')
        raise ValueError("\033[93mMinutes cannot be above 59 in any context using classic hh:mm:ss format.")

    # Seconds
    if 0 > time.seconds or time.seconds > 59:
        logging.error('User did not entered a valid second')
        raise ValueError("\033[93mSeconds cannot be above 59 in any context using classic hh:mm:ss format.")
    return True

def clock_testing(time:Clock)->bool:
    '''Copy-Paste of clock_validity but instead returns a boolean for unit testing.'''
    # Hours
    if time.format24:
        if 0 > time.hours or time.hours > 24:
            return False
    else:
        if 1 > time.hours or time.hours > 12:
            return False
        
    # Minutes
    if 0 > time.minutes or time.minutes > 59:
        return False

    # Seconds
    if 0 > time.seconds or time.seconds > 59:
        return False

    return True

def time_formatting(time:Clock)->str:
    '''Returns a string of the time in hh::mm::ss style with 12h or 24h format'''
    hours = ""
    minutes = ""
    seconds = ""
    # Hours management
    if time.hours < 10:
        hours = "0" + str(time.hours)
    else:
        hours = str(time.hours)
    # Minutes management
    if time.minutes < 10:
        minutes = "0" + str(time.minutes)
    else:
        minutes = str(time.minutes)
    # Seconds management
    if time.seconds < 10:
         seconds = "0" + str(time.seconds)
    else:
        seconds = str(time.seconds)
    # Time format management
    if not time.format24:
        if not time.pm:
            return f'{hours}:{minutes}:{seconds} AM'
        else:
            return f'{hours}:{minutes}:{seconds} PM'        
    else:
        return f'{hours}:{minutes}:{seconds}'

def time_updating(time:Clock)->Clock:
    '''Updates the time 'time' to insure that it has correct values belonging to their format'''
    time.seconds += 1
    # Secondes management
    if time.seconds > 59:
        time.minutes += 1; time.seconds = 0
    # Minutes management
    if time.minutes > 59:
        time.hours += 1; time.minutes = 0; time.seconds = 0
    # Hours management with format management
    if not time.format24:
        # 12h format management
        if time.pm == False:
            if time.hours > 12:
                    time.pm = True
                    time.hours = 1; time.minutes = 0; time.seconds = 0
        else:
            if time.hours > 11:
                    time.pm = False
                    time.hours = 0; time.minutes = 0; time.seconds = 0
    #24 hours format management
    else:
        if time.hours > 23:
            time.hours = 0; time.minutes = 0; time.seconds = 0
    return time

def time_comparison(time:Clock, delta:Clock)->bool:
    '''Compare two times and returns if these times are the same'''
    return time.hours == delta.hours and time.minutes == delta.minutes and time.seconds == delta.seconds

def keyboard_input_management():
    '''Manages keyboard inputs and updates clock_state belonging to the key pressed.'''
    global clock_state
    while clock_state != 0:
        key_pressed = read_key()
        if key_pressed == "space":
            sleep(0.3)
            if clock_state == 1:
                clock_state = 2
                logging.info('User paused the time.')
                print("pause.")
            else:
                clock_state = 1
                logging.info('User resumed the time.')
                print("resuming of time.")
        elif key_pressed == "esc":
            logging.info('User stopped the time.')
            print("termination of the clock.")
            clock_state = 0
            break
    return

def clock_state_management(time:Clock, alarm:bool=False, delta:Clock=(0,0,0), message:str=""):
    '''Manages the different states of the clock and also the displaying of the clock in the terminal'''
    os.system('cls' if os.name == 'nt' else 'clear') 
    global clock_state, printing_state
    while clock_state != 0:
            if clock_state == 1:
                printing_state = 0
                if alarm == True:
                    if time_comparison(time,delta) == True:
                            printing_state = 2
                            clock_state = 3
                            time_updating(time)
                    else:
                        sleep(1)
                        time_updating(time)
                        os.system('cls' if os.name == 'nt' else 'clear') 
                        print(time_formatting(time), " ", clock_state, " ", end='', flush=True)
                else:
                    printing_state = 0
                    sleep(1)
                    time_updating(time)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(time_formatting(time), " ", clock_state, " ", end='', flush=True)
            elif clock_state == 2:
                if printing_state == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(time_formatting(time), " ", clock_state, " ", flush=True)
                    print("Press space to resume time. Press esc to stop time")
                    printing_state = 1
            elif clock_state == 3:
                if printing_state == 2:
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    logging.info('Clock has been triggered.')
                    print(message)
                    print(time_formatting(time), " ", clock_state, " ", flush=True)
                    print("Press space to resume time. Press esc to stop time")
                printing_state = 1
            else: # clock_state == 0
                break
    return

def time_terminal_displaying(time:Clock, alarm:bool=False, delta:Clock=(0,0,0), message:str=""):
    '''Display the time in the terminal with/without the alarm from 'time' and updates every seconds.'''
    global clock_state
    logging.info('Time is running.')
    thread_boucle_execution = threading.Thread(target=clock_state_management, args=(time,alarm, delta, message))
    thread_io_operations = threading.Thread(target=keyboard_input_management, args=())
    thread_boucle_execution.start()
    thread_io_operations.start()
    thread_boucle_execution.join()
    thread_io_operations.join()

if __name__ == "__main__":
    time24 = Clock(23,59,50)
    time12 = Clock(12,59,55,False)
    time_terminal_displaying(time12, True, Clock(1,0,0,False,True), "It's time!")
    time_terminal_displaying(time24)