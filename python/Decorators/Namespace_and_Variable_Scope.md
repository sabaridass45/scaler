# Namespace and Scope of the Variable 

### What is Namespace?

In python, namespace is a system that has a unique name for each object that object may be variable name, method name, class name. A namespace is like a dictionary that maps a variable name to an object i.e. name is a key and value is an object.

### Types of Namespace
1. Global Namespace: Contains names defined at the module level.
2. Local Namespace: Created during the execution of a function or method, containing its local variables.
3. Built-in Namespace: Contains Python’s built-in functions and exceptions (e.g., len, print, int).

![img not found](/scaler/python/Decorators/types_namespace-1.png)
#### Global Namespace
Global namespaces are the variables that are defined at the module level and the global variable inside the module can used.

Examples:
```python
num = 10; # global variable
print('Num value is: ',num);
```
    Output:
    Num value is: 10

Using global variables from the import files

in details.py
```python
firstName = 'Tony'
secondName = 'Stark'
```

in main.py
```python
from details import firstName, secondName
print('Fullname: ', firstName + ' ' + secondName)
```
    Output:
    Fullname: Tony Stark

#### Local Namespace
Local namespaces are the variables that are created in the method or a function. But the variables cannot be used outside the function.

```python
def fun():
    a = 10 # local variable
    print('value of a inside function: ', a)
fun()
print('value of a outside function ', a) 
```
    Output:
    value of a inside function: 10
    NameError: name a is not defined

#### Built-in Namespaces
Built-in namespaces are the predefined/built-in functions and objects that has the scope as a lifetime of the entire program.

The following examples are the built-in functions
- input
- dict
- sum
- eval

These name spaces form the following hierarchy: **Local>Global>Built-in**.

If there are 2 or more variables with the same name, the variable higher in the scope hierarchy will be used. These namespaces aren’t separate concepts. Instead, the local namespace is a subset of global, and the global namespace is a subset of built-in.

### What is variable scope in python?
In python, Scope of the variable inside a method or function, class is accessible. Scope is important for variables to overcome the conflicts of using same variable name.

### Types of Scope
1. Local Scope
2. Global Scope
3. Enclosing Scope
4. Built-in Scope

**Local Scope:** A local scope refers to the area within a function or method and accessible only inside the function or method. These variables are created when the function is called and destroyed when the function execution is complete.
- Isolation: Variables in the local scope are isolated from global or other local scopes.
- Lifetime: Local variables exist only during the function's execution.
- Access: Variables in local scope cannot be accessed outside the function.

> Example:
<details>
    <summary>Example for Local Scope</summary>

```python
def inner():
    a = 10 # local variable
    print(a)
inner()
print(a) # error occurs
```
<details>
    <summary>Output:</summary>
    
    10
    NameError: name a is not defined
</details>
</details>

**Global Scope:** A global scope refers to the area where variables are defined and accessible throughout the program including inside functions. 

- Accessibility: Global variables can be accessed from any part of the program, but they can only be modified inside a function if explicitly declared as global.
- Lifetime: Global variables exist as long as the program runs.
- Best Practices: Overuse of global variables can lead to code that is difficult to debug and maintain.

> Example:

<details>
    <summary>Example for global scope without modification</summary>

```python
b = 20 # global variable
def inner():
    a = 10 # local variable
    b = 15
    print('a:', a)
    print('inner function b:', b)

print('b:', b)
inner()
```
<details>
    <summary>Output:</summary>

    b: 20
    a: 10
    inner function b: 15
</details>
</details>

But in the same example when tries to modify global variable shows error **'UnboundLocalError'**. To overcome this, use **global keyword** as follows:
<details>
    <summary>Example for global scope with modification</summary>

```python
b = 20 # global variable
def inner():
    a = 10 # local variable
    global b
    b = b + 5 # modify the value globally
    print('a:', a)
    print('inner function b:', b)

inner()
print('b:', b)
```
<details>
    <summary>Output:</summary>

    a: 10
    inner function b: 25
    b: 25
</details>
</details>

**Enclosed Scope:** An enclosed scope in the variables are defined and accessible in the enclosed functions i.e. the nested function where variables are declared. Variables in the enclosing function’s scope can be accessed by the inner (nested) function but cannot be directly modified unless explicitly declared as nonlocal.

- Where it exists: Enclosed scope applies to nested functions.
- Access: Inner functions can read variables from the enclosing function's scope.
- Modification: To modify an enclosing variable, use the nonlocal keyword.
- Lifetime: Variables in the enclosed scope persist as long as the enclosing function exists.

> Example:
<details>
    <summary>Enclosed scope without modification</summary>

```python
b = 20
def outer():
    c = 15 # enclosed variable or nonlocal variable 
    def inner():
        a = 10 # local variable
        print('a:', a)
        print('inner function c:', c)
    inner()
    print('c:', c)

outer()
```
<details>
    <summary>Output:</summary>
    a: 10
    inner function c: 15
    c: 15
</details>
</details>
Similar to the global scope, to modify the enclosed variable need to use **nonlocal keyword** to overcome the **UnboundLocalError**.
<details>
    <summary>Enclosed scope with modification</summary>

```python
b = 20
def outer():
    c = 15 # enclosed variable or nonlocal variable 
    def inner():
        a = 10 # local variable
        nonlocal c
        c = c + 15 # modify the enclosed variable
        print('a:', a)
        print('inner function c:', c)
    inner()
    print('c:', c)

outer()
```

<details>
    <summary>Output:</summary>
    
    a: 10
    inner function c: 30
    c: 30
</details>
</details>

> **Note:** To modify the global variable in the local scope use **'global' keyword**, in the same way to modify the enclosed variable use **'nonlocal' keyword**.

**Built-in Scope:** The built-in scope in Python is the widest or outermost scope that contains all the built-in functions, exceptions, and objects provided by Python. These include functions like print(), len(), and keywords like True, False, etc.

- Predefined: The built-in scope is automatically available in every Python program.
- Accessibility: You can access built-in names anywhere in the program unless they are shadowed by a global or local variable with the same name.
- Lifetime: Built-in names are available as long as the Python interpreter is running.

<details>
<summary>Example for Built-in</summary>

```Python
print('hello!')
```
<details>
<summary>Output:</summary>

    hello!
</details>
</details>



[LEGB_Rule](/scaler/python/Decorators/LEGB_Rule.md)