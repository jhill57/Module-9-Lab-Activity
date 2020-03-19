# this program was written by Jordan on 3/19/2020
# this program asks for user input to create a list...
# ...and sum of the list if less than or equal to 100
lst = []
while sum(lst) <= 100:
    enternumber = int(input("please enter a number"))
    lst.append (enternumber)
    print (lst)
print("Congratulations, your list adds to ", sum(lst))
