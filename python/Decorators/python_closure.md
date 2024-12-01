# Python Closures

  A function object that has access to variables from its own local scope, even when the function is called outside that scope. In simple words, Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.
 
 [The concept of closures is related to nested functions, where a function is defined within another function. If the nested function references a variable from the enclosing function, then the nested function is a closure]: #

```
> The following are the conditions that are required to be met in order to create a closure in Python:

> These are the conditions you need to create a closure in Python:

> There must be a nested function

> The inner function has to refer to a value that is defined in the enclosing scope

> The enclosing function has to return the nested function

> Source: https://stackabuse.com/python-nested-functions/ 
```

## prerequisites to python closures:

1. Nested Function
2. Function are first class object

#### Nested Function
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

> Output
```
res : <function num1.<locals>.num2 at 0x1005a03a0>
res.__name__ : num2
Output for res(5) : 50
```

</details>


#### Function are first class object

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

> Output:
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

> Output:
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

> Output:
```
Hello, Sabaridass M
```
</details>