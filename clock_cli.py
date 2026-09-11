import click # @clicK.command, @click.option
import clock_backend # Clock(), Clock().time_terminal_displaying(clk), clock_validity
from warnings import warn
from time import sleep

@click.group()
def cli():
    pass

@cli.command("time")
@click.option('--start', nargs=5, default=(0,0,0,24,0), help='The starting hour of the clock: hh mm ss format isam/pm',type=int)
@click.option('--alarm',nargs=6, default=(0,0,0,0,0,0), help='The alarm time wanted: enabled hh mm ss format isam/pm', type=int)
@click.option('--message',default="",help="If alarm enabled, the message that'll be displayed if its time",type=str)
def clock(start, alarm, message):
    hour, minute, second, format_clock, am = start
    enabled_alarm, hour_alarm, minute_alarm, second_alarm, format_alarm, am_alarm = alarm
    if enabled_alarm == 0:
        if format_clock == 12 or format_clock == 0:
            if am == 1:
                clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=False)
            elif am == 0:
                clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=True)
            else:
                warn("\033[93mWarning: Invalid AM/PM value. Clock set to AM.\033[0m",SyntaxWarning)
                sleep(5)
                clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=False)
        elif format_clock == 24 or format_clock == 1:
            clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=True ,pm=False)
        else:
            warn("\033[93mWarning: Invalid time format input. Clock set 24h format.\033[0m",SyntaxWarning)
            sleep(3)
            clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=True ,pm=False)
        clock_backend.clock_validity(clk)
        return clock_backend.time_terminal_displaying(time=clk,alarm=False)

    elif enabled_alarm == 1:
        if format_alarm == format_clock:
            if format_clock == 12:
                if am == 1:
                    clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=False)
                elif am == 0:
                    clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=True)
                else:
                    warn("\033[93mWarning: Invalid AM/PM input. Clock set to AM.\033[0m",SyntaxWarning)
                    sleep(3)
                    clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=False)

                if am_alarm == 1:
                    clk_alarm = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=False)
                elif am_alarm == 0:
                    clk_alarm = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=True)  
                else:
                    warn("\033[93mWarning: Invalid alarm AM/PM input. Alarm set to AM.\033[0m",SyntaxWarning)
                    sleep(3)
                    clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=False)
            elif format_clock == 24:
                clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=True ,pm=False)
                clk_alarm = clock_backend.Clock(hours=hour_alarm, minutes=minute_alarm, seconds=second_alarm, format24=True ,pm=False)
            else:
                warn("\033[93mWarning: Invalid time format input. Clock and alarm set 24h format.\033[0m",SyntaxWarning)
                sleep(3)
                clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=True ,pm=False)
                clk_alarm = clock_backend.Clock(hours=hour_alarm, minutes=minute_alarm, seconds=second_alarm, format24=True ,pm=False)
            if clock_backend.clock_validity(clk) and clock_backend.clock_validity(clk_alarm):
                return clock_backend.time_terminal_displaying(clk,True,clk_alarm, message)
            else:
                raise SyntaxError("\033[93mBoth clock and alarm should be valid. Check your inputs.\033[0m")
        else:
            raise SyntaxError("\033[93mClock and alarm time format should be the same.\033[0m")

@cli.command("chrono")
def chrono():
    return clock_backend.time_terminal_displaying(clock_backend.Clock(0,0,0))

if __name__ == '__main__':
    cli()