import ast
import sys
import astunparse

'''The following function will take a PARSED code, it will iterate through all of the child nodes, and
recursively get the child nodes of these child nodes
'''

def _reader(filename):
    with open(filename) as f:
        content = f.read()
        return content

def child_nodes(parsed):
    print('The children of ', parsed,  ' are:',parsed._fields)
    g = ast.iter_child_nodes(parsed)
    for item in g:
        child_nodes(item)

if __name__ == '__main__':
    filename = sys.argv[1]
    code = _reader(filename)
    p = ast.parse(code)
    child_nodes(p)