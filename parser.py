from lexLog import LexerLog

class Parser(object):
    def __init__(self, data):
        self.lex = LexerLog(data)
        self.curTok = self.lex.getNextTok()
        #self.lex.test()

    def accept(self, t):
        if self.curTok == t:
            self.curTok = self.lex.getNextTok()
            return True
        return False

    def errorMessage(self):
        print("Syntax error: line {0}, colon {1}".format(self.lex.getLine(), self.lex.getColumn()))

    def Rel(self):
        if self.accept('ID'):
            if self.accept('CORKSCREW'):
                res = self.Disj()
                if self.accept('DOT'):
                    return res
                return False
            if self.accept('DOT'):
                return True
        return False

    def ID(self):
        if self.accept('ID'):
            return True
        if self.accept('LPAREN'):
            res = self.Disj()
            if self.accept('RPAREN'):
                return res
            return False

    def Disj(self):
        res = self.Conj()
        if self.accept('DISJ'):
            return self.Disj()
        return res

    def Conj(self):
        res = self.ID()
        if self.accept('CONJ'):
            return self.Conj()
        return res

    def parse(self):
        while True:
            if not self.curTok:
                break
            if not self.Rel():
                self.errorMessage()
                return
        print("Correct syntax")
