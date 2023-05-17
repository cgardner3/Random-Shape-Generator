'''
Write a program that will randomly assign a number between 1 and 3 a total of
up to 10 times. For each of the 10 times, it will display the output and do the shape
that was selected for example if 1 was selected then it would be the circle, if it is 2 then
it would be a square and if 3 it would be a rectangle. Within the classes, there will be definitions
and methods that will allow for the area to be found and identify what class was selected.

Author: Cheryl Gardner
Course: ITM 313
'''

#import the three classes that were made in a separate file as well as the secrets
import math
import secrets


#Define the main class
def main():

    #Welcome the user to the program with a message
    print("Welcome to the Random Shape Generator!!\nThis program will create an array of the three different shapes randomly\n")

    #Declare the variable goAhead to be true
    goAhead = True
    #As long as the user wants to continue running the program keep running this loop
    while goAhead == True:

        #Ask the user how long they want the length no matter how long
        number = eval(input("\nHow many shapes do you want in your list?: "))

       #Create a shape list with the number of shapes that the user selected  
        myList = createMyList(number)

        #Print the random list to the user
        printRand(myList)

        #Ask the user whether or not they want to make another list
        goChoice = input("\nWould you like to make another random list? (y/n): ")
        #If the user does not want to continue then thank them for using the program 
        if goChoice == "n":
            print("Thank you for using my program!!! Please Come Again Soon!!!")
            #Set the goAhead variable to false so that the loop will stop running
            goAhead = False

#Define a new method that is called createMyList
def createMyList(number):

    #Create a new array called myList and declare secret
    myList = []
    secret = secrets.SystemRandom()

    #As long as the value of x is less than or equal to the number of shapes the user wanted then do this loop
    for x in range(0, number):
        #Choose a random number that is between 1 and 3
        num = secret.randrange(1, 4)

        #If the random number is one then call the circle class and add circle to the list that will be displayed
        if (num == 1):
            circle = Circle()
            myList.append(circle)

        #If the random number is two then call the square class and add circle to the list that will be displayed  
        elif (num == 2):
            square = Square()
            myList.append(square)

        #If the random number is three then call the rectangle class and add circle to the list that will be displayed
        elif (num == 3):
            rectangle = Rectangle()
            myList.append(rectangle)

    #return the list back to the main program so that it can be used 
    return(myList)


#Create a new method that is called printRand which will be used to display all of the random shapes and their details
def printRand(myList):

    #Print the heading for all of the shape displays with the two columns
    print("\n{0:<10}{1:<10}".format("Shape", "Area"))

    #As long as the value of shape is in the list then display the shape data
    for shape in myList:
       shape.display()

#Declare the class circle with a circle that has a radius of two
class Circle():
    #Initialize the variables that will be used
    def __init__(self,radius = 2):
        self.__radius = radius
    def setRadius(self, new):
        self.__radius = new
    #Get the radius value
    def getRadius(self):
        return(self.__radius)
    #Get the shape name and calculate the area
    def getShapeName(self):
        return("Circle")
    def find_area(self):
        return(round((math.pi * self.__radius * self.__radius),4))
    #For the display statement for output
    def display(self):
        print("{0:<10}{1:<10}".format("Circle",self.find_area()))

#Declare the class square with a square that has a side length of 2.5
class Square():
    #Initialize the side variable that will be used
    def __init__(self, side = 2.5):
        self.__side = side
    def setRadius(self, new):
        self.__side = new
    #Get the side value 
    def getSide(self):
        return(self.__side)
    #Get the shape name and calculate the area
    def getShapeName(self):
        return("Square")
    def find_area(self):
        return(round((self.__side * self.__side),4))
    #For the display statement for output
    def display(self):
        print("{0:<10}{1:<10}".format("Square", self.find_area()))

#Declare a class rectangle where the length is 5.675 and the width is 3.2
class Rectangle():
    #Initialize the variables that will be used
    def __init__(self, length = 5.675, width = 3.2):
        self.__length = length
        self.__width = width
    def setSide(self, new, new1):
        self.__length = new
        self.__width = new1
    #Get the width and the height values
    def getWidth(self):
        return(self.__width)
    def getLength(self):
        return(self.__length)
    #Get the shape name and then calculate the area
    def getShapeName(self):
        return("Rectangle")
    def find_area(self):
        return(round((self.__length * self.__width),4))
    #For the display statement for output
    def display(self):
        print("{0:<10}{1:<10}".format("Rectangle", self.find_area()))
        
#Call the main program
main()
