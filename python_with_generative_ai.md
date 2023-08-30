### Learn Python with generative AI
The idea of this portion is that you will be coming up with your own practice questions that are tailored to your level of programming experience.  

Go to ChatGPT, or any other generative AI and type in a prompt like this:

```
I've just completed an entry-level programming course and want to put my 
Python coding skills to practice. 
Can you give me some programming challenge questions at a 
beginner-intermediate level?
```

Here is ChatGPT's response, yours could be different:
---
Absolutely! Here's a set of beginner-intermediate level programming challenges in Python to help you practice and solidify your skills:

**1. Palindrome Checker:**
Write a program that checks if a given string is a palindrome (reads the same forwards and backwards).

**2. FizzBuzz:**
Write a program that prints numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

**3. Prime Number Checker:**
Write a program that checks whether a given number is prime or not.

**4. Word Counter:**
Create a program that takes a sentence as input and counts the number of words in it.

**5. Reverse a String:**
Write a program that takes a string as input and prints its reverse.

**6. Temperature Converter:**
Create a program that converts temperatures between Fahrenheit and Celsius.

**7. Guess the Number:**
Implement a simple number guessing game where the program generates a random number and the user tries to guess it.

**8. Hangman Game:**
Create a text-based Hangman game where a player tries to guess a hidden word letter by letter.

**9. To-Do List Application:**
Build a basic console-based to-do list application that allows users to add, remove, and list tasks.

**10. Calculator:**
Create a basic calculator that can perform addition, subtraction, multiplication, and division operations.

**11. Even-Odd Number Sum:**
Write a program that calculates the sum of even and odd numbers within a given range.

**12. Character Frequency Counter:**
Create a program that takes a string as input and counts the frequency of each character in it.

**13. Fibonacci Sequence:**
Generate the first n numbers of the Fibonacci sequence.

**14. Simple ATM Simulator:**
Build a simple ATM simulator that allows users to check balance, deposit, and withdraw money.

**15. Rock-Paper-Scissors Game:**
Create a simple rock-paper-scissors game where the user plays against the computer.

**16. Vowel and Consonant Counter:**
Write a program that counts the number of vowels and consonants in a given string.

**17. Shopping Cart:**
Build a basic shopping cart program where users can add items, view the cart, and calculate the total cost.

**18. Binary to Decimal Converter:**
Create a program that converts a binary number to its decimal equivalent.

**19. Basic Password Generator:**
Write a program that generates a random password with a specified length.

**20. Morse Code Translator:**
Implement a program that can convert English text to Morse code and vice versa.

These challenges cover various programming concepts and techniques. As you work through them, you'll gain practical experience and become more confident in your programming skills. Remember to break down the problems into smaller steps and test your code frequently. Happy coding!
---

Let's pick FizzBuzz, we probably want some additional information, so ask the following question:

```
Can you explain the requirements of the "FizzBuzz" question? 
```
Here is the response we get:
---
Certainly! The "FizzBuzz" problem is a classic coding interview question often used to assess a programmer's basic understanding of loops and conditionals. The task is to write a program that prints numbers from 1 to a specified upper limit (usually 100), but with a twist:

1. For numbers that are multiples of 3, print "Fizz" instead of the number.
2. For numbers that are multiples of 5, print "Buzz" instead of the number.
3. For numbers that are multiples of both 3 and 5, print "FizzBuzz".

Here's an example implementation for the numbers 1 to 15:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

Explanation:
- The number 3 is a multiple of 3, so it's replaced with "Fizz".
- The number 5 is a multiple of 5, so it's replaced with "Buzz".
- The number 6 is a multiple of 3, so it's replaced with "Fizz".
- The number 10 is a multiple of 5, so it's replaced with "Buzz".
- The number 15 is a multiple of both 3 and 5, so it's replaced with "FizzBuzz".

The goal of the FizzBuzz problem is to demonstrate your ability to use conditional statements (if/elif/else) and loops (such as a for loop) effectively. It's also a way to check if a programmer can break down a problem into smaller steps and implement a solution efficiently.
---
Okay, that is a pretty good explanation of the problem, definitely way more than Mr. Berg would give you. 

Now you should go ahead and try to program the solution in `a1_ai_problems.py`

I have added the fizzbuzz solution to the file with some asserts to test it out.  Once you have that solution paste it into ChatGPT in order to get its feedback:

```
Here is my code to solve FizzBuzz.
Is this accurate, and if not, can you guide me in getting the correct answer?
```
---
Your code is on the right track, but there's a small issue with the order of your conditions. The code will correctly identify numbers that are divisible by 3 or 5, but when it comes to numbers that are divisible by both 3 and 5 (i.e., multiples of 15), it will only return 'Fizz' or 'Buzz'. To fix this, you should check for multiples of 15 first before checking for individual divisibility by 3 or 5. Here's the corrected code:

```python
def fizzbuzz(input_num):
    if input_num % 15 == 0:
        return 'FizzBuzz'
    elif input_num % 3 == 0:
        return 'Fizz'
    elif input_num % 5 == 0:
        return 'Buzz'
    else:
        return input_num

# Test the function for numbers 1 to 20
for i in range(1, 21):
    print(fizzbuzz(i))
```

With this order of conditions, the code will correctly print 'FizzBuzz' for numbers that are multiples of both 3 and 5.
---

Interesting response here.  Our solution was technically correct for individual numbers including numbers that are divisible by 3 and 5, but it doesn't print out the solution from 1 to 100.  I notice this and can ask it for a revision:

```
Could you check my above code again?  I don't think that it executes from 1 to 100 as it says in the original problem, could you help me with that?
```
It produces the following response:
---
Apologies for the confusion. You're right; the code I provided doesn't address the requirement of printing numbers from 1 to 100. Here's the modified version of your original code that correctly prints the FizzBuzz sequence from 1 to 100:

```python
def fizzbuzz(input_num):
    if input_num % 3 == 0:
        if input_num % 5 == 0:
            return 'FizzBuzz'
        return 'Fizz'
    elif input_num % 5 == 0:
        return 'Buzz'
    else:
        return input_num

# Print FizzBuzz sequence from 1 to 100
for i in range(1, 101):
    print(fizzbuzz(i))
```

This code will iterate through numbers from 1 to 100 and apply the FizzBuzz rules correctly. It should produce the expected FizzBuzz sequence where multiples of 3 are replaced with "Fizz," multiples of 5 are replaced with "Buzz," and multiples of both 3 and 5 are replaced with "FizzBuzz."
---

There you go, you have two solutions now.  One that you coded and one that ChatGPT coded, you hopefully have learned a little through the process and have a better understanding of the python language.  You have a real time tutor that will give you advice on your solutions, but you need to be thoughtful and not believe everything that ChatGPT has to say.  Go and read the documentation and write your own asserts along the way.

ChatGPT can tailor indidual assignments to you and can help you through those solutions...pretty awesome!! If you use it correctly.

## Complete a few more of the practice questions that you received from ChatGPT

In the `a1_ai_problems.py` file, complete a few more of the problems that ChatGPT gave you.  Once you have completed them, make sure to answer the reflection questions in the writeup.