"""
Introduction to Console Programming
Writing a function to print a menu
"""
import sys
sys.path.insert(1, 'week0')
sys.path.insert(1, 'week1')
sys.path.insert(1, 'week2')

from christmasTree import christmasTree
from fibonacci import fibonacci
from animation import animation
from factors import factors
from matrix import matrix
from swap import swap
from factorial import factorial


# Menu options as a dictionary
menu_options = {
    0: 'Exit',
    1: 'Swap',
    2: 'Matrix',
    3: 'Christmas Tree',
    4: 'Animation',
    5: 'Fibonacci',
    6: 'Factor',
    7: 'Factorial',
}

def handleFactorial():
  number = int(input('Enter a number to calculate the facorial: '))
  factorialInput = factorial()
  factorialOutput = factorialInput(number)
  print(factorialOutput)
  
# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, u'\u001b[34m--\u001b[0m', menu_options[key] )
    runOptions()

# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input (u'\u001b[34mEnter your choice 0-7: \u001b[0m'))
         
            if option == 1:
              swap()
            elif option == 2:
              matrix()
            elif option == 3:
              christmasTree()
            elif option == 4:
              animation()
            elif option == 5:
              fibonacci()
            elif option == 6:
              factors()
            elif option == 7:
              handleFactorial()
            # Exit menu    
            elif option == 0:  
              print(u'\u001b[32mExiting! Thank you! Good Bye...\u001b[0m')
              exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 7.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')
      
if __name__=='__main__':
  print_menu2()
  