# HOW TO USE PythClock CORRECTLY

This is a CLI app, this means you can run something in the terminal, in this case a clock, without having a GUI.
To do so, you'll need the project, or at least clock_backend.py and clock_cli.py in your computer.
You can do this by cloning the repository and do ```git clone https://github.com/samy-belazzoug/PythClock.git``` in your desired folder.

Now, you can use the code. There is multiple commands to launch a clock : 

### 1) time
Let you start a clock at a desired time, with an alarm that displays a message when triggered.

```cli
python .\clock_cli.py time --start 23 58 55 24 0 --alarm 1 23 59 0 24 0 --message "Its time to go!"
```

Please read this part as its the most important one. You need to respect the flags and the input format in order to correctly execute a clock :

#### --start
This is the time from where you want to start.
The input format is : ```--start hh mm ss timeformat ampm``` with timeformat being either 24 or 12 and, if 12h format, am (0) or pm (1). 

*Please note that if you mention a wrong timeformat (not 24 or 12) it will automatically apply 24h format and if you type a wrong ampm choice (0 or 1) it will automatically apply to AM. If you type a wrong time (inexisting hour or minute or second belonging to the choosed format) it will not launch the clock and return an error.*

Examples of use :

Correct : ```--start 23 59 0 24 0 ``` -> 23h59.0s in 24h format 
Wrong : ```--start 23 59 0 12 0``` -> 12h format doesn't go above 12h
Wrong : ```--start 23 59 0 8 0``` -> time format invalid (8), will be set to 24h.
Correct : ```--start 8 20 10 12 0``` -> 08h20.10 AM in 12h format (AM)
Correct : ```--start 12 30 8 12 1``` -> 12h30.08 PM in 12h format (PM)
Wrong : ```--start 11 -10 66 12 3``` -> Minutes/seconds can't be below 0 nor above 59. If the time would be still valid, if would launch to AM because 3 isn't a valid input for AM/PM.

#### --alarm
This is the time to where you want the alarm to trigger.
The input format is the almost the same as --start, with : ```--alarm enabled hh mm ss timeformat ampm```
You just need to mention whether you want an alarm (1) or not (0) and then proceed with the other inputs.

*Please not that you have to be as carefull to your inputs as --start argument and that if the --start time and --alarm time doesn't have the same timeformat it will not launch an alarm nor the clock and return an error.*

Examples of use : 

Correct : ```--alarm 1 23 59 0 24 0 ``` -> alarm to 23h59.0s in 24h format 
Correct : ```--start 12 58 55 12 0 --alarm 1 12 59 0 12 0``` -> Time starting at 12h58.55 AM with a clock set at 12h59.0 AM.
Wrong : ```--start 12 58 55 12 0 --alarm 1 12 59 0 24 0``` -> Time format between --start and --alarm are wrong. It will return an error.
Wrong : ```--alarm 23 59 0 12 0``` -> enabled alarm valule missed! Don't forget it!
Wrong : ```--alarm 3 23 59 0 12 0``` -> wrong enabling value (3), can be either 1 (enabled) or 0 (disabled).

#### --message
The easiest one to understand and use. It's just a custom message that appears when alarm is triggered. You must put your message in quotes so the program can recognize it as a String.

Examples of use :

Correct : ```--message "It's time! Wake up!"``` -> Will display "It's time! Wake up!" when alarm is triggered
Wrong : ```--message It's time! Wake up!``` -> Not a valid input, will return an error.

### 2) chrono

Simply start a stopwatch, waiting for your inputs. There is no alarm available currently.
You can run it by doing : 

```python .\clock_cli.py chrono ```