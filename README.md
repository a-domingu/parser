# Parser for Python code

## Usage

This Python program will accept a file that contains Python code, and it will return to us the structure of its Abstract Syntax Tree (ATS).

### Example

Let's say we have the program `test.py` that contains the following piece of code: 
```
'''
this is a comment
'''
for i in range(5):
        a = 2+2
        b = 'hello world'
```

Then we can run our program from the terminal with: `python parser.py test.py`, and we get the following output:

```
The children of
'\nthis is a comment\n'
for i in range(5):
    a = (2 + 2)
    b = 'hello world'
  are: ('body', 'type_ignores')
The children of
'\nthis is a comment\n'
  are: ('value',)
The children of  '\nthis is a comment\n'
  are: ('value', 'kind')
The children of
for i in range(5):
    a = (2 + 2)
    b = 'hello world'
  are: ('target', 'iter', 'body', 'orelse', 'type_comment')
The children of  i
  are: ('id', 'ctx')
The children of  <_ast.Store object at 0x03447730>  are: ()
The children of  range(5)
  are: ('func', 'args', 'keywords')
The children of  range
  are: ('id', 'ctx')
The children of  <_ast.Load object at 0x03447700>  are: ()
The children of  5
  are: ('value', 'kind')
The children of
a = (2 + 2)
  are: ('targets', 'value', 'type_comment')
The children of  a
  are: ('id', 'ctx')
The children of  <_ast.Store object at 0x03447730>  are: ()
The children of  (2 + 2)
  are: ('left', 'op', 'right')
The children of  2
  are: ('value', 'kind')
The children of  <_ast.Add object at 0x03447940>  are: ()
The children of  2
  are: ('value', 'kind')
The children of
b = 'hello world'
  are: ('targets', 'value', 'type_comment')
The children of  b
  are: ('id', 'ctx')
The children of  <_ast.Store object at 0x03447730>  are: ()
The children of  'hello world'
  are: ('value', 'kind')
```

We can see, for every node, which are their children, and then it will recursively do the same for each child.