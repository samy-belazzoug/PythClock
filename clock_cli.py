import click # @clicK.command, @click.option
import clock_backend # Clock(), Clock().time_terminal_displaying(clk)


@click.command()
@click.option('--format',default=24,  help='Time format (12h or 24h)', type=int)
@click.option('--time', nargs=4, default=(0,0,0,0), help='The starting hour of the clock',type=int)
def clock(time, format):
    hour, minute, second, am = time
    if format == 12:
        if am == 1:
            clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=False)
        elif am == 0:
            clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=True)
    else:
        clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=True ,pm=False)
    clock_backend.time_terminal_displaying(time=clk,alarm=False)

if __name__ == '__main__':
    clock()