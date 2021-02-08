my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]


#Your code go from here:
def maxfromlist(element):
    max=0
    for i in element:
        if (i > max):
            max = int(i)
    return max

print(maxfromlist(my_list))