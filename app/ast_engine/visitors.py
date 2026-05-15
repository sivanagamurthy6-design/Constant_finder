# AST visitors
from ast import NodeVisitor
class ASTVisitor(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.nodes = []
    
    def generic_visit(self, node):
        self.nodes.append(node)
        super().generic_visit(node)
        
