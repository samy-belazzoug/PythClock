# PythClock

*My very first complete CLI app*

## Description

This project is a simple CLI app of a clock that updates every seconds.
If you want to learn how to use it, please read MANUAL.md file.

## Features

The project will not have a GUI, in fact, it will only be a CLI app.
It still has multiple features :
- Possibility to pause (and then resume) or stop the clock in real time thanks to a multithreaded event mangement system.
- You can setup an alarm and the clock will run until the alarm is met.
- CLI arguments/commands management, thanks to click library
- Exception/ Error handling with personal, colored warnings
- Unit testings has been done to test the robustness of the clock verification algorithm
- Logging system implemented to track down user inputs and know if there is something strange with input handling code.

*When the alarm is met, the time will automatically pause, but you can of course resume or stop the clock.*

## Technologies

The main programming language used for this project is Python, the reasons are :
    
### Familiarity with the language

It's been now 4 years that I know and I use Python for some of my IT projects. It's not my main language, but it is definitely one of my favorite and one of the language I know the most.

### Simplicity of the language

Python excells for simple projects like this. You don't have to write a lot of code to get first satisfying results thanks to its very light, simple and effective syntax.

### Efficiency of the libraries and the PIP and the help of the community

Python have very good libraries for this kind of project such as time, keyboard, threading, click etc... which are widely used by the community and well documented. It's very likely to find a solution to a problem by just a 5 minutes reasearch on the web.

## Why did I wanted to do this project 

So, first of all, I've already done a few years ago a clock in Python like this but for some reasons I deleted the repository, which is unfortunate because it was nicely implemented!

Now I am doing the exact same project again but for one main reason : Discover multithreading programming.
And there you gonna tell me : Python is NOT the optimal language for multithreading, and you may be right.. But still, the familiarity, the simplicity and the efficienct libraries of the language makes me choose Python to discover this new way of programming.

I like this project because its a very tiny one, it's in fact just a clock that runs in the terminal.
But this give me the advantage to learn in a very simple way new programming ways like multithreading or new stuff such as unit testing, logs, exceptions etc... 