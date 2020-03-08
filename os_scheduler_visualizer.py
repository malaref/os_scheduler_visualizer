#!/usr/bin/python

from re import match
from numpy import arange
from matplotlib.pyplot import figure, tight_layout, savefig


def render(scheduler_log, figure_path):
    switches = []
    arrivals = []
    finishes = []

    with open(scheduler_log) as f:
        for line in f:
            if not line.startswith('#'):
                line = line.strip()
                time, process, event, arrival = match('At time (\d+) process (\d+) (\S+) arr (\d+)', line).groups() 
                switches.append((int(time), int(process)))
                
                if event == 'finished':
                    arrivals.append((int(arrival), int(process)))
                    finishes.append((int(time), int(process)))

    max_time = max(point[0] for point in switches) + 1
    max_process = max(point[1] for point in switches) + 1

    ax = figure(figsize=(max_time / 2, max_process / 2)).gca()

    def plot(points, style):
        x, y = zip(*points)
        ax.plot(x, y, style)

    plot(switches, '-b')
    plot(arrivals, 'og')
    plot(finishes, 'xr')

    ax.set_xlim(0, max_time)
    ax.set_ylim(0, max_process)
    ax.set_xticks(arange(0, max_time))
    ax.set_yticks(arange(0, max_process))
    ax.grid(True)
    tight_layout()
    savefig(figure_path)


if __name__ == '__main__':
    from sys import argv, exit
    
    if len(argv) != 3:
        exit('USAGE: os_scheduler_visualizer.py SCHEDULER_LOG_PATH FIGURE_PATH')
    render(argv[1], argv[2])
