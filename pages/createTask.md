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
2.
* def squareNumbers(sequence):
  * squaresList = []
3. The lists being used in these code segments are call numSequence[] and squaresList[].
4. The data in numSequence[] represent how the comouter will prompt the user to enter 5 numbers, and those numbers will be stored inside the list. With squaresList[], the computer squares each number in the origional list and outputs them.
5. Without the lists, it would be very difficult and time consuming to store each number inside variables and then have to pass each variable into a function that squares each number the user typed in. The lists inside the code make the program easier to read.

### 3C.
1.
* for num in range (0, 5):
  * number = int (input("Enter a number "))
  * numSequence.append(number)
  * return numSequence
2.
* for num in sequence:
  * squares = num * num
  * squaresList.append(squares)
  * return squaresList
3. This procedure shows the computer returning the numbers in the list that the user inputted. It also stores the numbers in the list numSequence[].
4. This procedure shows the computer returning the numbers after they have been squared. The function prints out each element in the list after it have been squared.

### 3D.
1.
* One of the calls in the code is a function telling the computer to square every number the user entered. The numbers are passed into the list as integers, and returned as integers when they are squared.

* if __name__ == "__main__":
  * numSequence = getNums()
  * numSquares = squareNumbers(numSequence)

2. 
* squaresList.append(squares)

* squaresList = []
  * for num in sequence:
  * squares = num * num
  * squaresList.append(squares)

3.
* return numSequence

* return squaresList

[Video of Runtime](https://www.awesomescreenshot.com/video/8313811?key=4ab9f1d893abc307f7a73ec22eac6e53 "Create Task Video")
