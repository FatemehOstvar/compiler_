import sys
from antlr4 import FileStream, CommonTokenStream
from parser.gen.SASLexer import SASLexer
from parser.gen.SASParser import SASParser
from parser.gen.MySASVisitor import MySASVisitor

def main(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = SASLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SASParser(tokens)
    tree = parser.program()
    visitor = MySASVisitor()
    visitor.visit(tree)
    print("✅ Done.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tester.py <file.sas>")
    else:
        main(sys.argv[1])
