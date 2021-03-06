#!/usr/bin/env python2

import csv

tomas = csv.DictReader(open('data.csv'), fieldnames=['move', 'start', 'end'])
collect = csv.reader(open('collect.csv'))

current = None

possible = ['up', 'down', 'left', 'right']

out = open('machine_learning.dat', 'w')

def convert_line(label, features):
    i = possible.index(label)
    s = str(i)
    n = 1
    for f in features:
        s += ' {0}:{1}'.format(n, f)
        n += 1


for row in collect:
    t = float(row[0])
    for r in tomas:
        if t >= float(r['start']) and t <= float(r['end']):
            out.write(convert_line(r['move'], row[1:]))
            out.write('\n')

out.close()
    


