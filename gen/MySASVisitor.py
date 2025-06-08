from parser.gen.SASParserVisitor import SASParserVisitor

class MySASVisitor(SASParserVisitor):
    def visitVarDecl(self, ctx):
        print(f"Variable: {ctx.IDENTIFIER().getText()}")
        return self.visitChildren(ctx)

    def visitFuncDecl(self, ctx):
        print(f"Function: {ctx.IDENTIFIER().getText()}")
        return self.visitChildren(ctx)

    def visitClassDecl(self, ctx):
        print(f"Class: {ctx.IDENTIFIER().getText()}")
        return self.visitChildren(ctx)
