# import ast


# def extract_literals_from_code(code):

#     literals = []

#     def safe_eval(node):
#         try:
#             return ast.literal_eval(node)
#         except Exception:
#             return None

#     class LiteralVisitor(ast.NodeVisitor):

#         def visit_Constant(self, node):
#             literals.append(node.value)

#         def visit_List(self, node):

#             value = safe_eval(node)

#             if value is not None:
#                 literals.append(value)

#             self.generic_visit(node)

#         def visit_Tuple(self, node):

#             value = safe_eval(node)

#             if value is not None:
#                 literals.append(value)

#             self.generic_visit(node)

#         def visit_Set(self, node):

#             value = safe_eval(node)

#             if value is not None:
#                 literals.append(value)

#             self.generic_visit(node)

#         def visit_Dict(self, node):

#             value = safe_eval(node)

#             if value is not None:
#                 literals.append(value)

#             self.generic_visit(node)

#     try:
#         tree = ast.parse(code)
#         LiteralVisitor().visit(tree)

#     except SyntaxError as e:
#         print(f"Syntax error while parsing code: {e}")

#     return literals

import ast
from typing import List, Optional

from app.ast_engine.models import ConstantRecord


class ConstantExtractor(ast.NodeVisitor):

    def __init__(self, file_path: str):

        self.file_path = file_path

        self.results: List[ConstantRecord] = []

        self.current_class: Optional[str] = None

        self.current_function: Optional[str] = None

    def add_result(self, name, value, lineno, scope):

        record = ConstantRecord(
            file=self.file_path,
            class_name=self.current_class,
            function_name=self.current_function,
            name=name,
            value=value,
            line=lineno,
            scope=scope
        )

        self.results.append(record)

    def get_literal_value(self, node):

        try:
            return ast.literal_eval(node)

        except Exception:
            return None

    def visit_Assign(self, node: ast.Assign):

        value = self.get_literal_value(node.value)

        if value is None:
            return

        for target in node.targets:

            # MODULE / CLASS VARIABLES
            if isinstance(target, ast.Name):

                scope = (
                    "module"
                    if self.current_class is None
                    else "class"
                )

                self.add_result(
                    target.id,
                    value,
                    node.lineno,
                    scope
                )

            # INSTANCE VARIABLES
            elif (
                isinstance(target, ast.Attribute)
                and isinstance(target.value, ast.Name)
                and target.value.id == "self"
                and self.current_function == "__init__"
            ):

                self.add_result(
                    target.attr,
                    value,
                    node.lineno,
                    "instance"
                )

        self.generic_visit(node)

    def visit_ClassDef(self, node):

        prev_class = self.current_class

        self.current_class = node.name

        self.generic_visit(node)

        self.current_class = prev_class

    def visit_FunctionDef(self, node):

        prev_function = self.current_function

        self.current_function = node.name

        self.generic_visit(node)

        self.current_function = prev_function