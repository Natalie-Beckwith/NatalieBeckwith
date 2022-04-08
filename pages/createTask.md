{% include navigation.html %}

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@NatalieBeckwith/Create-Task?embed=true"></iframe>

# Written Responses:

### 3a.
1. The overall use of this project is to ask the user to input 5 numbers, and the computer outputs those numbers and squares them on the next row.
2. The video shows the computer asking the user to enter 5 numbers, and returns those numbers and the row blow returns the squares of those numbers.
3. The input is the user entering 5 integers. The output demonstrated in the video shows the computer printing out the list of 5 integers and their squares.

### 3b.
1. 
* def getNums():
    * numSequence = []
    * print("Enter a sequence of 5 numbers: ")

  * for num in range (0, 5):
    * number = int (input("Enter a number "))
    * numSequence.append(number)
    * return numSequence

2.
* def squareNumbers(sequence):
  * squaresList = []

  * for num in sequence:
    * squares = num * num
    * squaresList.append(squares)
    * return squaresList

3. The lists being used in these code segments are call numSequence[] and squaresList[].
4. The data in numSequence[] represent how the comouter will prompt the user to enter 5 numbers, and those numbers will be stored inside the list. With squaresList[], the computer squares each number in the origional list and outputs them.
5. 
