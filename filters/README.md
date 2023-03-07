# Custom Filters

### Upper Filter Example
An example Blueprint filter looks like the following:
```python
"""
Each filter must define an attribute containing its name. This is the name which invokes the filter in the template code. 
"""
FILTER_NAME = "upper"

"""
init() must be defined, which is executed once the filter is imported (only once per configuration).

It is a safe place to generate any random values required by the filter and perform any necessary initialization logic. 
"""

def init():
    return

"""
variables() must be defined, which receives a copy of the templates variables before the template is rendered. 

This is the filter's opportunity to define any custom variables it requires, by adding them along with their values to the `variables` parameter. 

The same parameter must be returned, so that the new variables are applied to the template being rendered.
"""

def variables(variables: dict):
    return variables

"""
filter() must be defined, which is executed when the filter is invoked. 

Here is the place to process input and return output which will end up in the finalized template.
"""

def filter(input) -> str:
    return input.upper()
```







