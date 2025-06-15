
# TODO handle if else else if statements by printing its type!
# TODO handle while and for loops by printing its type!

import sys
from antlr4 import *
from SASLexer import SASLexer
from SASParser import SASParser
from SASEvaluator import SASEvaluator

def main():
    if len(sys.argv) < 2:
        print("Usage: python tester.py <input-file.sas>")
        return

    filename = sys.argv[1]
    input_stream = FileStream(filename)

    lexer = SASLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SASParser(token_stream)
    tree = parser.program()

    evaluator = SASEvaluator()
    result = evaluator.visit(tree)

    for var, val in evaluator.vars.items( ):
        vartype = evaluator.types.get(var, type(val).__name__)


if __name__ == "__main__":
    main()
