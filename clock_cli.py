import click # @clicK.command, @click.option
import clock_backend # Clock(), Clock().time_terminal_displaying(clk)


@click.command()
@click.option('--time', nargs=5, default=(0,0,0,0,0), help='The starting hour of the clock',type=int)
@click.option('--alarm',nargs=6, default=(0,0,0,0,0,0), help='The alarm time wanted', type=int)
@click.option('--message',default="",help='If alarm, the message that will be displayed when its time',type=str)
def clock(time, alarm, message):
    hour, minute, second, format_clock, am = time
    enabled_alarm, hour_alarm, minute_alarm, second_alarm, format_alarm, am_alarm = alarm
    if enabled_alarm == 0:
        if format_clock == 12:
            if am == 1:
                clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=False)
            elif am == 0:
                clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=True)
        else:
            clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=True ,pm=False)
        return clock_backend.time_terminal_displaying(time=clk,alarm=False)

    elif enabled_alarm == 1:
        if format_alarm == format_clock:
            if format == 12:
                if am == 1:
                    clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=False)
                elif am == 0:
                    clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=True)

                if am_alarm == 1:
                    clk_alarm = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=False)
                elif am_alarm == 0:
                    clk_alarm = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=True)  
            else:
                clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=True ,pm=False)
                clk_alarm = clock_backend.Clock(hours=hour_alarm, minutes=minute_alarm, seconds=second_alarm, format24=True ,pm=False)
            return clock_backend.time_terminal_displaying(clk,True,clk_alarm, message)
        
if __name__ == '__main__':
    clock()