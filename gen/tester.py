# import sys
# from antlr4 import *
# from SASLexer import SASLexer
# from SASParser import SASParser
# from SASEvaluator import SASEvaluator
#
# def main():
#     if len(sys.argv) < 2:
#         print("Usage: python tester.py <input-file.sas>")
#         return
#
#     filename = sys.argv[1]
#     input_stream = FileStream(filename)
#
#     lexer = SASLexer(input_stream)
#     token_stream = CommonTokenStream(lexer)
#     parser = SASParser(token_stream)
#     tree = parser.program()
#
#     evaluator = SASEvaluator()
#     result = evaluator.visit(tree)
#
#     for var, val in evaluator.vars.items( ):
#         vartype = evaluator.types.get(var, type(val).__name__)
#
#
# if __name__ == "__main__":
#     main()
import sys, os
import argparse
from antlr4 import *
# Make sure we import the freshly generated modules from the right folder
sys.path.insert(0, os.path.abspath("."))

from SASLexer import SASLexer
from SASParser import SASParser
from SASEvaluator import SASEvaluator


def dump_tokens(token_stream, lexer):
    token_stream.fill()
    names = lexer.symbolicNames
    for t in token_stream.tokens:
        tname = names[t.type] if 0 <= t.type < len(names) else str(t.type)
        print(f"line {t.line}:{t.column}\t{tname}\t{repr(t.text)}")


def print_if_children(tree, parser):
    """
    Quick & dirty walk that prints if/elsif/else groups so you can verify
    how many elseIfBlock() nodes the parser produced.
    """
    from antlr4.tree.Tree import TerminalNode

    def walk(ctx, depth=0):
        rule_name = parser.ruleNames[ctx.getRuleIndex()]
        if rule_name == "ifStatement":
            # Show the exact children the parser attached here
            print("\n[ifStatement @ line {}] {}".format(ctx.start.line, ctx.getText()))
            # Try to reflect structure
            try:
                ifblk = ctx.ifBlock()
                elifs = ctx.elseIfBlock()
                elseblk = ctx.elseBlock()
                print(f"  - has ifBlock:     {bool(ifblk)}")
                print(f"  - elseIfBlock(s):  {len(elifs)}")
                print(f"  - has elseBlock:   {bool(elseblk)}")
                if elifs:
                    for i, e in enumerate(elifs):
                        print(f"    * elsif[{i}]: {e.getText()}")
                if elseblk:
                    print(f"    * else: {elseblk.getText()}")
            except Exception as _:
                pass

        # Recurse
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                continue
            walk(child, depth + 1)

    walk(tree)


def main():
    ap = argparse.ArgumentParser(description="Run SAS lexer/parser/evaluator")
    ap.add_argument("input", help="input .sas file")
    ap.add_argument("--tokens", action="store_true", help="dump token stream (with line/column)")
    ap.add_argument("--tree", action="store_true", help="print parse tree")
    ap.add_argument("--ifdbg", action="store_true", help="print structure of parsed if/elsif/else")
    args = ap.parse_args()

    # Read input
    input_stream = FileStream(args.input, encoding="utf-8")

    # Lex & token stream
    lexer = SASLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # --- ALWAYS dump tokens (line/column, token name, text) ---
    token_stream.fill( )
    names = lexer.symbolicNames
    for t in token_stream.tokens:
        tname = names[t.type] if 0 <= t.type < len(names) else str(t.type)
        print(f"line {t.line}:{t.column}\t{tname}\t{repr(t.text)}")
    # Important: rewind so the parser sees all tokens from the beginning
    token_stream.seek(0)

    # --tokens mode: show what the lexer actually produced (e.g., ELSIF vs IDENTIFIER)
    if args.tokens:
        dump_tokens(token_stream, lexer)
        return

    # Parse
    parser = SASParser(token_stream)
    tree = parser.program()

    if args.tree:
        print(tree.toStringTree(recog=parser))

    if args.ifdbg:
        print_if_children(tree, parser)

    # Evaluate
    evaluator = SASEvaluator()
    result = evaluator.visit(tree)

    # Optional: print final variable states (finish your earlier loop)
    if hasattr(evaluator, "vars"):
        for var, val in evaluator.vars.items():
            vartype = getattr(evaluator, "types", {}).get(var, type(val).__name__)
            print(f"{var} ({vartype}) = {val}")


if __name__ == "__main__":
    main()
