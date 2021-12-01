# Tiur
A simple programming language made using python PLY for the final project of CIIC4030.
Made by Jael Gonzalez
## Usage

To run a tiur script:

    python tiur.py [file_path]





## Mision

Tiur was made for beginners who do not have a grasp of programming languages. It presents a very simple and readable format.

#### Example code:

```
#Creating a variable with string value
a is "Hello world!"
show(a)

#Creating a variable with int value
b is 123
show(b)

#Creating a variable with list value
c is ["this","is","a","list"]
show(c)

#RECEIVE input
d is receive("Chose a value: ")
show("The value for d is:")
show(d)

#Nesting receive withing show
show(receive("Indicate what you want printed: "))
```
#### Output

```
"Hello world!"
123
['"this"', '"is"', '"a"', '"list"']
"Chose a value:" 12
"The value for d is:"
12
"Indicate what you want printed:" 2
2
```
