list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(elements):
    even=[]
    odd=[]
    for i in elements:
        if (i % 2 == 0):
            even.append(i)
        if (i % 2 != 0):
            odd.append(i)
    newlist=[]
    newlist= odd+even
    return odd,even
 

print(merge_two_list(list_of_numbers))

