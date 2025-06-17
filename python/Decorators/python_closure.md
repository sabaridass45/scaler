###### Contents:
- prerequisites to python closures
    - [Nested Function](#nested-function)
    - [Function are first class object](#function-are-first-class-object)
- [Python Closures](#python-closures)

#### <a name="nested-func"></a>Nested Function
  - A function within another function called Nested Function or Inner Function.
  
<details>

<summary><strong><i><code>Example for Nested Function</code></i></strong></summary>

```python
def outer_func(): # outer function which is defined here
    print ("Hello Sabaridass from outer function")
    def inner_func(): # inner function
        print ("Hello Sabaridass from inner function")
    inner_func() #call func which calling the inner func and perform the inner_func() opration.

func = outer_func
print(f"func.__name__: {func.__name__}")
print(f"{outer_func()}")
```

> **Output:**: 
```
func.__name__: outer_func
Hello Sabaridass from outer function
Hello Sabaridass from inner function
```

```python
#Below example shows that an inner function is able to access variables present/accessible in the outer function.
def num1(x):
   def num2(y):
      return x * y
   return num2 #func reference which returns only the obj of the inner func num2()

res = num1(10) #call func which returns '<function num1.<locals>.num2 at 0x1005a03a0>'

print(f"res : {res}") # res : <function num1.<locals>.num2 at 0x1004be0d0>
print(f"res.__name__ : {res.__name__}") #res.__name__ : num2
print(f"Output for res(5) : {res(5)}") #returns the value as 50 where x=10 and y=5
```

> **Output:**: 
```
res : <function num1.<locals>.num2 at 0x1005a03a0>
res.__name__ : num2
Output for res(5) : 50
```
</details>

> **Source**: https://stackabuse.com/python-nested-functions/ 

#### <a name="func-are-first-class-obj"></a>Function are first class object

- A first-class object is a program entity that can be:
  - Created at runtime.
  - Assigned to a variable or element in a data structure.
  - Passed as an argument to a function.
  - Returned as the result of a function.


<details>

<summary><strong><i><code>Example for Function are first class object</code></i></strong></summary>

```python
#Functions Assigned to Variables
def greet(name):
    return f"Hello, {name}"

#assign the func greet to a new variable say_hello
say_hello = greet
print(say_hello("Sabaridass M"))
```

> **Output:**: 
```
Hello, Sabaridass M
```


```python
#Functions Passed as Arguments to other Functions 
def greet(name):
    return f"Hello, {name}"

def loud_greeting(func, name):
    print(func(name).upper())

loud_greeting(greet, "Sabaridass M")  # Output: HELLO, SABARIDASS M
```

> **Output:**: 
```
HELLO, SABARIDASS M
```

```python
#Functions Returned by other Functions
def get_greeting_function(name):
    def greet():
        print(f"Hello, {name}")
    return greet

greet_john = get_greeting_function("Sabaridass M")
greet_john()  # Output: Hello, Sabaridass M
```

> **Output:**: 
```
Hello, Sabaridass M
```
</details>



## Python Closures

  A function object that has access to variables from its own local scope, even when the function is called outside that scope. In simple words, Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.
 
[The concept of closures is related to nested functions, where a function is defined within another function. If the nested function references a variable from the enclosing function, then the nested function is a closure]: #

#### Condition to create a python closure:


1. There must be a nested function.

2. The inner function has to refer to a value that is defined in the enclosing scope(outer function).

3. The enclosing function must return the nested function.


<details>

<summary><strong><i><code>Example for closure</code></i></strong></summary>

```python
#closure
def num1(x): #outer func
  def num2(y): #inner func
    return x + y
  return num2 #returns the func obj

func = num1(10)
print(f"func.__name__ : {func.__name__}")
print(f"num1(10) : {num1(10)}")
print(f"num1(10)(5) : {num1(10)(5)}") #Execute the inner func operation
#Here Hides the data of 'x' and 'y' where x=10 and y=5 and return only the result i.e. 15
```

>Output:
```
func.__name__ : num2
num1(10) : <function num1.<locals>.num2 at 0x1005a01f0>
num1(10)(5) : 15
```

```python
#closure with factory functions. 
def power_generator(num): #outer function
    # Create the inner function
    def power_n(power):
        return num ** power
    return power_n

power_two = power_generator(2)
power_three = power_generator(3)
print(f"power_two(8) : {power_two(8)}")
print(f"power_three(4) : {power_three(4)}")
#In the script above, from the power_n(power) function, we have created two other objects, power_two and power_three. This makes power_n(power) a factory function since it generates the power_two and power_three functions for us using the parameter we pass it.
```

> Output:
```
power_two(8) : 256
power_three(4) : 81
```
</details>


#### Pros of Python Closures:

1. Data Hiding --> Helps in encapsulating the data.
2. Code Organization --> used as block or template which can use it again and again
3. Avoids use of global variables --> Avoid the use of global values and provides some form of data hiding.


#### Cons of Python Closures:

1. Memory Usage --> Consume more memory as those variables are kept alive as long as the closure exists.
2. Complexity and Debugging --> Harder to understand the code for new developer

