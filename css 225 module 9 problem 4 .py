# this was written by Jordan on 3/19/2020
# this creates a list of all intergers divisble...
# ...by ten under 50
counter = 0
tens = []
while counter <= 50:
    if counter % 10 == 0:
        tens.append (counter)
    counter += 1
print (tens)
