#AREA OF A ROOM
#Write a program that asks the user to enter the width and length of a room. 
#Once these values have been read, your program should compute and display 
#the area of the room. The length and the width will be entered as 
#floating-point numbers. Include units in your prompt and output message; 
#either feet or meters, depending on which unit you are more comfortable 
#working with.

width=float(input("Insert the width of the room: "))
lenght=float(input("Insert the lenght of the room: "))
Area=width*lenght
print("The area of the room is:", Area)