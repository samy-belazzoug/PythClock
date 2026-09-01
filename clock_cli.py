import click # @clicK.command, @click.option
import clock_backend # Clock(), Clock().time_terminal_displaying(clk)


@click.command()
@click.option('--time', nargs=3, default=(0,0,0), help='The starting hour of the clock',type=int)
@click.option('--format',default=24,  help='Time format (12h or 24h)', type=int)
@click.option('--am', default=False, help='If format = 12, tell if time is starting AM or PM',type=bool)
def clock(time, format, am):
    hour, minute, second = time
    if format == 12:
        if am == 'am':
            clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=False)
        else:
            clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=False ,pm=True)
    else:
        clk = clock_backend.Clock(hours=hour, minutes=minute, seconds=second, format24=True ,pm=False)
    clock_backend.time_terminal_displaying(clk)

if __name__ == '__main__':
    clock()