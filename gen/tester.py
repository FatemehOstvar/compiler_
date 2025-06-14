from antlr4 import *
from SASLexer import SASLexer
from SASParser import SASParser
from SASEvaluator import SASEvaluator

def main():
    input_code = "int x = 42; int y = 3.14; int z = x + y;"
    input_stream = InputStream(input_code)
    lexer = SASLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SASParser(token_stream)
    tree = parser.program()

    evaluator = SASEvaluator()
    result = evaluator.visit(tree)

    for var, val in result.items():
        print(f"{var} = {val}")

if __name__ == "__main__":
    main()
