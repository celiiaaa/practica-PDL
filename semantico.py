# NO SE SI ESTO ES VERDAD...

class SemanticAnalyzer:
    def __init__(self):
        self.environment = {}

    def evaluate(self, node):
        if isinstance(node, tuple):
            node_type = node[0]
            if node_type == 'program':
                return self.evaluate_program(node)
            elif node_type == 'expression_statement':
                return self.evaluate_expression(node[1])
            elif node_type == 'if':
                return self.evaluate_if_statement(node)
            elif node_type == 'literal':
                return node[1]
            elif node_type == 'identifier':
                return self.evaluate_identifier(node)
            elif node_type == 'binary':
                return self.evaluate_binary_expression(node)
            elif node_type == 'logical':
                return self.evaluate_logical_expression(node)
            elif node_type == 'comparison':
                return self.evaluate_comparison_expression(node)
        else:
            raise Exception(f"Unknown node type: {node}")

    def evaluate_program(self, node):
        for statement in node[1]:
            self.evaluate(statement)

    def evaluate_if_statement(self, node):
        condition = self.evaluate(node[1])
        if condition:
            self.evaluate_program(('program', node[2]))  # Ejecuta el bloque de 'if'
        elif node[3] is not None:
            self.evaluate_program(('program', node[3]))  # Ejecuta el bloque de 'else'

    def evaluate_expression(self, node):
        return self.evaluate(node)

    def evaluate_identifier(self, node):
        identifier = node[1]
        if identifier in self.environment:
            return self.environment[identifier]
        else:
            raise Exception(f"Undefined identifier: {identifier}")

    def evaluate_binary_expression(self, node):
        left = self.evaluate(node[2])
        right = self.evaluate(node[3])
        operator = node[1]
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        else:
            raise Exception(f"Unknown binary operator: {operator}")

    def evaluate_logical_expression(self, node):
        left = self.evaluate(node[2])
        right = self.evaluate(node[3])
        operator = node[1]
        if operator == '&&':
            return left and right
        elif operator == '||':
            return left or right
        else:
            raise Exception(f"Unknown logical operator: {operator}")

    def evaluate_comparison_expression(self, node):
        left = self.evaluate(node[2])
        right = self.evaluate(node[3])
        operator = node[1]
        if operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        elif operator == '<':
            return left < right
        elif operator == '<=':
            return left <= right
        elif operator == '>':
            return left > right
        elif operator == '>=':
            return left >= right
        else:
            raise Exception(f"Unknown comparison operator: {operator}")

# Ejemplo de uso:
if __name__ == "__main__":
    import sys
    from parser import parser

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            data = file.read()
            ast = parser.parse(data)
            analyzer = SemanticAnalyzer()
            analyzer.evaluate(ast)
    else:
        print("Usage: python3 semantic_analyzer.py <source_file>")
