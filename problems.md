# Main problems occured during development

*Note that the code is very simplified and is not the same as the real code for purposes of explanation.*

## Handling user inputs in execution time loop

We have a function that allows the display of a clock in real time. What we want to do now is to be able, in real time, to
pause time or stop it.

```
    while True:
        display_clock()
```

Since time rotates in a loop, then the only way to manually pause or stop it
the time has come to detect inputs triggered by the user via their keyboard.
For example, if the user presses the space key, time is paused; if he presses the escape key, time is stopped.
However, to catch up time, the user would also need to press another key or the same key.

```
while True:
    display_clock()
    if space_bar_triggered():
        pause_time()
    if esc_triggered():
        break
```

I find it more convenient to have only one touch to pause and resume time.
However, a problem will quickly occur. If the user presses on space, this pauses time, but if he re-presses on space
nothing can happen because we do not know the state of the clock.

One way to solve this problem is to have a variable that stores the state of the clock so you can know if it is 
either in a running state, in a paused state or in a stopped state and perform operations according to this state.

state = 0 -> stopped
state = 1 -> running
state = 2 -> paused

```
state = 1
while state != 0:
    if state == 1:
        display_clock()
    else if state = 2:
        pass
    if space_bar_triggered():
        if state == 1:
            state = 2
        else if state = 2:
            state = 1
    if esc_triggered():
        state = 0
```

Now, there is one last problem that is undoubtedly the most problematic.
To detect keyboard inputs, we use the "keyboard" library, especially the keyboard.read_key() function.
The keyboard.read_key() function starts a loop and stops when a key is pressed, it returns 
thus the pressed key.
If we use this function in our loop, it means that the entire program will wait for the function
keyboard.read_key() returns something to continue processing. This means that the clock will also have to wait for the end of 
this function to update itself, which is not optimal at all!

What we want, therefore, is to have a loop that manages the clock display and updates it, but also another loop 
running at the same time who manages the keyboard events.
This is possible with multithreading.