def number_of_bottles(n):
	if (n == 1):
		objects = 'bottle'
		objectsMinusOne = 'bottles'
	elif (n == 2):
		objects = 'bottles'
		objectsMinusOne = 'bottle'
	else:
		objects = 'bottles'
		objectsMinusOne = 'bottles'


	if (n == 1):
		print(str(n) + " " + objects + " of milk on the wall, " + str(n) + " " + objects + " of milk.")
		print("Take one down and pass it around, no more bottles of milk on the wall")
		print(" ")
    else if (n == 0):
		print("No more bottles of milk on the wall, no more bottles of milk.")
		print("Go to the store and buy some more, 99 bottles of milk on the wall.")        
	else:

         print(str(n) + " " + objects + " of milk on the wall, " + str(n) + " " + objects + " of milk.")
		print("Take one down and pass it around, " + str(n-1) + " " + objectsMinusOne + " of milk on the wall.")
		print(" ")
        
bottles = 99
while bottles >= 0:
	number_of_bottles(bottles)
	bottles -= 1

