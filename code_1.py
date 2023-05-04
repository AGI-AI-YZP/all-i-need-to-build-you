import ast
from ast import NodeVisitor

class CodeAnalyzer(NodeVisitor):
    def visit_FunctionDef(self, node):
        print(f"Found function: {node.name}")
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        print(f"Found class: {node.name}")
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            print(f"Found import: {alias.name}")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            print(f"Found import from {node.module}: {alias.name}")
        self.generic_visit(node)

if __name__ == "__main__":
    code = """
import os
import sys
from math import pi, sin

class MyClass:
    def my_method(self, x):
        return x * 2

def my_function(y):
    return y + 1
    """

    tree = ast.parse(code)
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)