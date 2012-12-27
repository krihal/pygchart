import csv
import sys
import getopt

from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis

def open_csv(file):
    labels = []
    values = []

    with open(file, 'rb') as csvfile:
        cr = csv.reader(csvfile, delimiter=',')
        for row in cr:
            labels.append(row[0])
            values.append(row[1])

    csvfile.close()

    return labels, values

def plot(labels, values, filename):
    max_y = 500

    chart = SimpleLineChart(600, 375, y_range=[0, max_y])
    chart.add_data(values)
    chart.set_colours(['0000FF'])
    chart.set_grid(0, 25, 5, 5)

    left_axis = range(0, max_y + 1, 25)
    left_axis[0] = ''

    chart.set_axis_labels(Axis.LEFT, left_axis)
    chart.set_axis_labels(Axis.BOTTOM, labels)
    chart.download("%s.png" % filename)

def usage():
    print "pygchart.py -f <filename>"
    sys.exit(2)
        
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hf:", [])

    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt == "-h":
            usage()
        elif opt == "-f":
            filename = arg
        else:
            usage()

    (labels, values) = open_csv(filename)

if __name__ == '__main__':
    main(sys.argv[1:])