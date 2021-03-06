"""
View the latest output file in the current directory
for NJU cluster
"""
import os

latest = '000000'
latime = 0.0
for filenam in os.listdir('.'):
    # filename looks like output.123456
    if 'output' in filenam:
        fileno = filenam[7:]
        mtime = os.stat(filenam).st_mtime
        if fileno > latest or mtime > latime:
            latest = fileno
            latime = mtime

latestfile = 'output.' + latest
os.system("vim " + latestfile)
