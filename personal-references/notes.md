# Random Notes

So I don't forget the stuff I learn here.

---
## UserMixIn
It is a class in flask-login module which provides the following methods:
- `is_authenticated()`: Returns True if the user is authenticated.
- `is_active()`: Returns True if the user is active.
- `is_anonymous()`: Returns True if the user is an anonymous user.
- `get_id()`: Returns the unique identifier for the user.

---
## Bcrypt
bcrypt is a hashing library in python, which hashes the passwords so that they can be stored more securely 
in the database. It is used to hash the passwords before storing them in the database and to compare the 
hashed passwords when the user logs in.

Even if the data is compromised, the passwords are still secure because the hacker would have to decrypt it,
which is too difficult to do, unless you have the actual passwords.

---
## Difference Between Module and Library in Python

|  **Feature**   |          **Module**          |           **Library**            |
|:--------------:|:----------------------------:|:--------------------------------:|
| **Definition** |     A single `.py` file.     |     A collection of modules.     |
|   **Scope**    |    Small, specific tasks.    |      Broader functionality.      |
|  **Examples**  |         `math`, `os`         |   `NumPy`, `Pandas`, `Flask`.    |
|   **Usage**    |     `import module_name`     |`import library_name.module_name` |


### **Module**
A module is a single Python file containing code like functions, classes, or variables.

#### Example:
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

import my_module
print(my_module.greet("Alice"))  # Output: Hello, Alice!
```
---
## Decorators

Decorators in Python are functions that modify the behavior of another function or method. They allow you to "wrap" another function to add functionality without changing its structure.

### How Decorators Work
- A decorator takes a function as input, adds some functionality, and returns a new function.
- You use the `@decorator_name` syntax to apply a decorator to a function.

### Example Without Using `@` Syntax
```python
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

def say_hello():
    print("Hello!")

decorated_function = decorator(say_hello)
decorated_function()
```
---
## Modals
Modals are dialog boxes or pop-ups that appear on top of the current page. They are used to display information, ask for user input, or confirm an action.
![img.png](modal.png)
---
## Pagination
### What is Pagination?
Pagination is a technique used to divide content into separate pages, allowing users to navigate through large sets of data in smaller, more manageable chunks. Think of it like chapters in a book or pages in a magazine – instead of showing everything at once, the content is broken down into discrete pages.
### Why Use Pagination?
When dealing with large datasets, pagination offers several important benefits:

- **Performance Optimization**: Rather than loading thousands of records at once, pagination lets servers send only a small portion of data at a time, significantly improving load times and reducing server strain.
- **Better User Experience**: Users can easily navigate through content without being overwhelmed by endless scrolling or massive data dumps. This is particularly important when displaying search results, blog posts, or product listings.