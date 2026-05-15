import ast

from app.ast_engine.constant_extractor import ConstantExtractor


class ASTParser:

    def parse(self, code: str, file_path: str):

        tree = ast.parse(code)

        extractor = ConstantExtractor(file_path)

        extractor.visit(tree)

        return extractor.results