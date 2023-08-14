#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")   
def greet(name):
    print("Hello, " + name + "!")

def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2

# Example usage
greet_programmer()
greet("Alice")
greet_with_default()
greet_with_default("Bob")
result = add(5, 7)
print("Result of addition:", result)
halved_value = halve(20)
print("Half of 20:", halved_value)


