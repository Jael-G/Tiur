![Tiur logo](https://github.com/Jael-G/Tiur/blob/main/tiur.jpg)
# Tiur
Tiur (or Tir) is the god of written language, schooling and wisdom worshipped in ancient Armenia.
This language made using Python's PLY seeks to make programming more similar to written language and easier to learn, therefore following what the Tiur god stands for.
The logo is a representation of the Armenian eternity sign, a symbol that is part of the national identity of the Armenian people and commonly seen on walls of churches.

## Usage

To run a tiur script:

    python tiur.py [file_path]

The file to be executed most be of .tiur extension



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

#Math operations
show(1+4)
show([1,2,3,4] + [5,6,7])

#There is much more
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
5
[1,2,3,4,5,6,7]
```
