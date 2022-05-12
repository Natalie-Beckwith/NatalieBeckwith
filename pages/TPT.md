{% include navigation.html %}

# Week 8:

## Blockchain Tech Talk

Notes:
* Blockchain - ex: Bitcoin
* Architecture
* Beyond Bitcoin
* US printing more money
* Harder to buy products
* ex: cost of a house is increasing
* Bitcoin’s value does not change
* Cannot be created
* Skills Companies need:
* Understand technology
* Allows flexibility
* History:
* Blockchain has been around a long time - 1982
* Bitcoin was created in 2009
* Crypto-currency is created through blockchains
* Certain amount of Bitcoin 
* The creator of Bitcoin is not know
* What does the Bitcoin blockchain do? - keeps track of the amount of Bitcoin there is
* Autherium blockchain - takes Bitcoin and improves it
* Saves affect of execution from blockchain
* Network architecture:
* Certain server network
* Bitumen
* No certain server
* Communication through protocols
* Hashing - technology that allows you to generate something
* When you tamper with one byte - the hash no longer exists
* You only hash the block of contents once, you don’t hash the hash
* Consensus Protocol
* Two types - Highway 2.0 and 3.0
* Uses hashing to solve problems
* As more people use it, hashing increases
* Producing bad block is almost impossible because it takes more work to produce a block, don’t want effort to be wasted
* Proof of stake - electricity is swapped out for bonding
* Nodes in network agree on a set of transactions
* No central coordinating authority
* Consensus - solution to a theoretical problem in CS
* Byzantine theory - If you have 2 generals that are sending messengers to a warfront, how will you guarantee the troops will not be defeated?
* Need order to make sure the protocol is decentralized
* Anyone can run it, and shut it off
* Has to be safe and live
* Safety - When I make a transaction, it guarantees it won’t be wound back
* Doesn’t add blocks - dead
* User proposes block that the networks consider safe, and they add the block to the blockchain
* Sends transaction in less than 3 hours
* Central banks are afraid of Bitcoin because it’s very decentralized, and secure, anyone can access them
* At a minimum, contains runtime, network, consensus protocol layer, global state tri
* Block - a memory of a set of past transactions
* Each block has a certain number of 
* Tip of block is most recent transactions
* Like a giant book
* Lists set of transactions
* One large book, containing every transaction ever made
* 2 TB disk space of the global chain
* Re-running all existing transactions
* Block chains are basically databases
* Each computer stays in touch by connecting to the global server
* APIs to communicate with accept transaction
* Client APIs - queue all transactions and processed into blocks
* People keep cryptos in keys
* Remember, you have to get a leisure to secure crypto
* Ensures you have ownership over crypto
* Asymmetrical cryptography - address key, or secret keys
* Secret keys should never be shared - how to access account and how to send crypto
* Public keys can see how much crypto someone has and can send crypto to someone
* Smart contract
* Runs on certain criteria
* Participants get all money they need
* 84% of enterprises are looking at blockchains
* Important to understand how blockchain works

Reflection:
Bitcoin is a type of cryptocurrency that allows for people to make online transactions. Bitcoin is one of the most popular types of blockchains. A blockchain is a shared database that stores information. In Bitcoin’s case, the blockchain keeps a collection, or block of each transaction ever made on Bitcoin. I learned the uses of hashing, which is a function that figures out how to solve for a transaction. You will always produce the same amount of data, and once you change a single byte of a blockchain, the hash is destroyed. Each device can access Bitcoin just by connecting to the blockchain and running all existing transactions. After the presentation, I did not know that Bitcoin runs on no central network, I always thought something as important as cryptocurrency, to be stored inside a central bank, sort of like how real central banks oversee other banking systems and controls their money supply. I also found it fascinating that Bitcoin eliminates inflation because Bitcoin always has the same amount of cryptocurrency. 

## Markdown using SQL Database:

Vocab:
* **Persistent Data** - data that stays even if you reload the page
* **One-to-One Relationship** - one on one
* **One-to-Many Relationship** - one person on many people
* **Many-to-One Relationship** - many people to one person
* **Many-to-Many Relationship** - many people to many people

Notes:
* Frontend features:
    * Textbox for where to type note
    * Button to submit note
* Backend features:
    * Requires user login
    * converts MD syntax to HTML (in textbox)
    * ForeignKey - every note needs to be tied to a specific user
          * establishes relationships between tables
          * When you want to have a One-to-Many Relationship, add a new table

To-Do:
* Try to recreate MD SQL Notes page on CSP Coders Example for website - can use something similar to teacher creating assignments for students
* Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
* Still using same database from login, just adding more tables to that database (one of the tables is Notes)

# Week #4:

## Accounts and Login

Notes:
* Login to protect database
* Sponsor: Add login to different pages
* Encrypted passwords in database
* app = Flask(__name__)
* MVC - model view controller
* __init__(self, name, email, password, phone):
* html files: view in MVC
* MVC - control, view driver
* 

# Week #3:
(Crossover Coding - no TPT this week)

# Week #2:

## 5.5
Notes:
* In some cases, it is ok for you to claim something as your own - must have a license
* Free has a cost
     * If you derive a piece of software with a free license, your work is also free use
* If you add a piece of code that has a free license, then you cost a company billions of dollors for that small block of code
* Different types:
     * Create Commons
     * GPL
     * Open Source

GitHub Actions:
1. My group is using a MIT License for our project.
2. The MIT License is user and open-source friendly and very easy to access

## 5.6
Notes:
* Why is safe computing important
     * To protect our information
* Things to keep secret
     * Social security
     * Address
     * Phone
     * Date of Birth
* Multi-factor authentication to make accounts secure
* Deploy website - find information
* Sometimes its good to post information
* Want people to know who you are
* Be mindful of what information you share on the internet
* SSL
* Organization Management:
     * to organize our own information in our code
     * as we build it up, it will be neatly arranged and easy to read
* OOP and Creating a Class
     * package data structures together
     * Name class - ex: Fibonacci
     
* class Fibonacci():
     * def __init__(self):
          * self.fiboSeg = [0, 1, 1, 2, 3, 5, 8, 13, 21]
* Set breakpoint to ensure that code works
     * Computer stops at where the breakpoint was in your code

GitHub Actions:
1. On college board it asks you to enter an email, your birthday, and other personal information. On my MacBook, I use a fingerprint scanner that automatically fills in my passwords when I am logging into websites
2. It depends on what the webpage is. If the website is a school website, then I would be ok with sharing my information for the purpose of school.
3. A good password has multiple different characters and capitals, it's some very complax that is almost impossible to guess. Another step is two-factor authentication.
4. 
     * Symmetric: type of encryption where only one key is used
     * Asymmetric: uses a pair of related keys
5. An example of symmetrical symmetrical encryption is through card transactions where PII needs to be protected
6. I have made a mistake of clicking on something that was clickbait. I have also downloaded something that eventually gave my computer a malware virus.

# Week #1:

## 5.3
Notes:
* Humans are prone to errors and biased
* There can be intentional or purposeful bias in computers
* EX: Facebook, TikTok, Amazon, Alexa Google, Apple Siri, Netflix
     * Has flaws in detecting accents or young voices
     * Bias certain amount of information on certain watchers
     * Purposeful exclusion

GitHub Page Actions:
1) No, the owner of the computer did not think this was intentional.
2) Computers are designed to be unbiased
3) It's likely that the person who designed the face detecting feature on the computer did not think this issue would happen. It's also likely that the creator only tested the facial recognition on themselves.
4) No, I don't think this issue was supposed to be harmful. Computers are designed to function unbiased and without errors. However, the human programming the computer can be biased
5) Yes, this issue should be corrected so that everyone can be able to access the facial recognition software, no matter what race.
6) I would test the face recognizing with many different people, particularly people of different races to see if the computer is still able to work.

## 5.4
Notes:
* Crowdsourcing- gathering data from a target audience to make improvements to code
* EX: Wikipedia, using API's, forking GitHub code
* All crypto exchanges are checked by 3 different miners

GitHub Page Actions:
1) One way to crowdsource my idea is by using a survey to get input from my peers on the website I am building
2) During my AmLit class, I can make a google form about what are the best books that the students in that class can take so everyone can give my group input on what the best books are in my AmLit class.

# Week #0

## 5.1
Notes:
* Drone functions include search and rescue and recreational uses
     * Can be used as military drones
* Dopamine - the happiness hormone
* You can get dopamine from online services such as games and social media
* Sometimes, games can become addictive
     * EX: Anthony Rosner

1) Easy access to endless information → It can be the wrong information. It’s hard to find a reliable source
2) Provides a source of entertainment → Can become addictive and consume a person’s social life
3) You can meet new people using technology → those people can be dangerous

1) Yes, being addicted to your device is a problem. This is because you are getting an alternate source of dopamine.

## 5.2
Notes:
* Digital divide: some countries have different or restricted areas
     * Maybe have different ways to access internet
* People may have less access to latest technology updates
* Some don't use technology
     * EX: Religious groups like the Amish
* At the start of COVID, 90,000 students in NJ did not have access to computers for distance learning
* In DNHS, we provide chromebooks to every student and have free internet access to all students and staff

1) One example of digital empowerment is to go to a Library or a school where they provide a device and access to the internet
2) An example of digital empowerment is to provide devices and free internet access.
3) Some of Del Norte’s classes require assignments to be submitted online via Canvas. People who don’t have access to the internet are unable to submit assignments on Canvas.
