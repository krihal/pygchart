import os

from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis

def dataparser(filename):
    dates = [0]
    funds = [0]
    values = [0]

    fd = open(filename, "r")
    
    for line in fd:
        (date, fund, value) = line.split(";")
        dates.append(date)
        funds.append(fund)
        values.append(int(float(value.strip())))

    fd.close()

    return (dates, values)
        
def plotter(fund):
    
    (dates, values) = dataparser("data/%s" % fund)
    left_axis = [int(min(values)), 0, int(max(values) + 1)]
    
    chart = SimpleLineChart(600, 375, y_range=[min(values), max(values) + 1])
    chart.add_data(values)
    chart.add_data([0] * 2)
    chart.set_colours(['76A4FB'] * 5)
    chart.add_fill_range('76A4FB', 0, 1)
    chart.set_grid(0, 5, 1, 25)
    chart.set_axis_labels(Axis.LEFT, left_axis)
    chart.set_axis_labels(Axis.BOTTOM, dates)

    chart.download("charts/%s.png" % fund)

if __name__ == '__main__':
    for dirname, dirnames, filenames in os.walk('data/'):
        for file in filenames:
            print "Plotting file: data/%s.png" % file
            plotter(file)
