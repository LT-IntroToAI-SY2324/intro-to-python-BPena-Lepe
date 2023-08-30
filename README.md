# How to start coding with chatGPT

## Description
There is a lot of value in using chatGPT (or other generative AI) outside of just asking for answers.  I believe that if you effectively learn how to program, you'll find AI as a tool that helps you speed up daily tasks instead of a tool that will replace you.  In order to do this we need to know how to ask it the correct questions and use it as a great resource.

## How to Ask Questions
The majority of developers work by searching for information on Google and StackOverflow, in fact, this is how I learned how to program, and I still do that.  So, it is completely normal for you to spend a lot of time on those platforms, including chatGPT. You just need to know how to ask the correct questions, and you won't always ask the correct questions, so you'll continue to learn from your mistakes.

1. Learn the basics first - Before we start using chatGPT extensively we should learn the basics of python first.  Everyone should have some basic programming knowledge, but we will go over the basics of python.  I'm going to go over a lot of information, but I would also recommend doing a free online tutorial like this one on freecodecamp.
2. Ask questions, then learn - Having an answer and just copying and pasting it won't make us learn how to program.  If the code you get from chatGPT works, you should ask it to explain it and why it is used.  At the beginning, your role is to learn so that in the future you can use chatGPT less and be more independent, which is why you should always ask for code explanations.
3. Solve actual problems - When programming, we can solve the same problem with different methods: this is why it doesn’t make any sense to just ask ChatGPT to generate some random code. We absolutely need to ask chatGPT for something related to a project we are making or a problem we need to solve.
4. Don't blindly trust it - chatGPT is prone to errors, they are improving and quite good, but they still make mistakes.  Do the research via google and stackOverflow so you know that they answers are correct.

## Always refer to the documentation
No matter what, you ALWAYS have to read the documentation.  This is how you will learn.  This is true in industry as well, so start doing it now.  If we find a snippet of code that can solve a problem we’re facing, and we don't understand it, then we won’t be able to generalize the code we’re using. This means that in the future we won't be able to solve a similar problem because we haven’t learned anything: we just copied and pasted the code.  

ChatGPT has been known to use libraries that don't even exist.  So, if you go searching for that library and can't find it, then maybe you can ask chatGPT for some more of an explanation on the library to try to figure out where it came from.  If you don't do the research on your own, then you'll never actually know if what you are using is actually factual.

Reading the documentation is always going to give you more understanding of programming and why certain things work.  You may even find better ways to solve problems when going through the documentation.

## Troubleshooting and debugging
We will be using the debug feature in VSCode, but you can also use chatGPT as an option.  Here is a general workflow for debugging:
Write your program
Debug your code in VSCode
Read the warning you get from the debugger if something doesn't work
Paste the warning on Google if you don't know how to solve them
Paste the warning on chatGPT if Googling doesn't solve your problem
Paste the whole code in chatGPT if you still haven't solved your issue
Go read the documentation if the previous point solved your issue

Don't blindly paste the code into chatGPT asking it to search for troubles in your code.  First, strive to find them on your own the hard way b/c this is the best way to learn new things. 

## Examples
Ask chatGPT the following question (I used Bard):
"How can we print in python?"

Here is the answer I received:
In Python, you can use the `print()` function to display output on the screen. The `print()` function takes one or more arguments, which can be strings, variables, or expressions, and displays them in the console. Here's the basic syntax:

```python
print("Hello, world!")  # Printing a string
```

You can also print multiple items by separating them with commas:

```python
name = "Alice"
age = 30
print("Name:", name, "Age:", age)  # Printing multiple items
```

If you want to print variables along with strings, you can use string formatting. There are several ways to format strings, and one commonly used method is using f-strings (formatted string literals):

```python
name = "Bob"
age = 25
print(f"Name: {name}, Age: {age}")  # Using f-string for formatting
```

In addition to printing strings and variables, you can print the results of expressions:

```python
x = 5
y = 10
result = x + y
print("The sum of", x, "and", y, "is", result)
```

You can also control the formatting of the output using various formatting options. For example:

```python
number = 3.14159
print("Formatted number: {:.2f}".format(number))  # Formatting with two decimal places
```

Remember that the `print()` function automatically adds a newline character (`\n`) at the end of the output, which moves the cursor to the next line. If you want to prevent this behavior, you can use the `end` parameter:

```python
print("Hello,", end=" ")
print("world!")  # Output: Hello, world!
```

These are some of the basic ways to use the `print()` function in Python to display output. Depending on your needs, you can further customize and format the output as desired.


---

That is a lot of information.  The prompt was too generic so chatGPT gave us a generic answer.

So, be specific! 
Here is a better question:

"I have a list with some strings in Python: how can I print them efficiently?"

If you have a list of strings in Python and you want to print them efficiently, you can use a loop to iterate through the list and print each string. The most common way to do this is by using a `for` loop. Here's an example:

```python
string_list = ["apple", "banana", "cherry", "date"]

for item in string_list:
    print(item)
```

This will iterate through the `string_list` and print each string on a separate line.

If you want to print the strings on the same line or with some specific formatting, you can use the `end` parameter of the `print()` function:

```python
string_list = ["apple", "banana", "cherry", "date"]

for item in string_list:
    print(item, end=" ")  # Print on the same line with a space between items
```

If you want to print the items along with their indices in the list, you can use the `enumerate()` function:

```python
string_list = ["apple", "banana", "cherry", "date"]

for index, item in enumerate(string_list):
    print(f"Item at index {index}: {item}")
```

Using list comprehensions, you can achieve concise printing of the entire list in a single line:

```python
string_list = ["apple", "banana", "cherry", "date"]
print(" ".join(string_list))  # Join and print the list items with spaces
```

This approach is efficient for printing lists, especially when you want to customize the formatting or display of the elements. Choose the method that best fits your specific requirements.

---

As you can see, it also gives you a lot of information, but super useful information.  At that point you might want to know more about the `join` function, so you could ask it:

"Could you explain the join function with an example"

---

Certainly! The `join()` function is a string method in Python that allows you to concatenate elements of an iterable (like a list, tuple, or set) into a single string. It's a powerful tool for combining strings with a specific separator. Here's how it works:

```python
separator = " - "
string_list = ["apple", "banana", "cherry", "date"]

result = separator.join(string_list)
print(result)
```

In this example, the `join()` function is called on the `separator` string and passed the `string_list` as its argument. The `join()` function then concatenates the elements of the list using the separator. The output will be:

```
apple - banana - cherry - date
```

The separator (" - " in this case) is placed between each pair of adjacent elements in the list, creating a single string. The result is stored in the `result` variable and then printed.

The `join()` function is particularly useful when you want to create nicely formatted output from elements in a list or any other iterable.

Keep in mind that the `join()` function works with strings, so if your list contains non-string elements, you'll need to convert them to strings first using techniques like list comprehensions or mapping functions.

---

Now, at this point, you should do other two things:

1. Searching for “join() Python” on Google and see some other examples and read the documentation.
2. Continue the chat and ask for an example (then, read the documentation that may come with the next examples).