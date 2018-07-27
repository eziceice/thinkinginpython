from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from urllib.request import *
from reportlab.graphics.charts.lineplots import LinePlot

COMMENT_CHARS = ':#'
URL = 'ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt'


def init_data():
    data = []
    for line in urlopen(URL).readlines():
        line = line.decode()
        if line[0] not in COMMENT_CHARS:
            data.append([float(n) for n in line.split()])
    return data


def draw_report():
    data = init_data()
    pred = [row[2] for row in data]
    high = [row[3] for row in data]
    low = [row[4] for row in data]
    times = [(row[0] + row[1]/12.0) for row in data]
    d = Drawing(400, 200)
    title = String(250, 180, 'Sunspots', fontsize=14, fillColor=colors.red)
    lp = LinePlot()
    lp.x = 50
    lp.y = 50
    lp.height = 125
    lp.width = 300
    lp.data = [list(zip(times, pred)), list(zip(times, high)), list(zip(times, low))]
    lp.lines[0].strokeColor = colors.blue
    lp.lines[1].strokeColor = colors.red
    lp.lines[2].strokeColor = colors.green
    d.add(title)
    d.add(lp)
    renderPDF.drawToFile(d, 'report.pdf', 'Sunspots')


if __name__ == '__main__':
    draw_report()