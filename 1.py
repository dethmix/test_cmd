start=1000
rate=0.05
numyear=5
year=1
while year <= numyear:
    start = start * (1 + rate)
    print "%d %0.3f" % (year, start)
    year +=1

