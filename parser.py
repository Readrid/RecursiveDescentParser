from lexLog import LexerLog

class Parser(object):
    def __init__(self, data):
        self.lex = LexerLog(data)
        self.curTok = self.lex.getNextTok()

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
                if not self.Disj():
                    return False
                if self.accept('DOT'):
                    return True
                return False
            if self.accept('DOT'):
                return True
        return False

    def ID(self):
        if self.accept('ID'):
            return True
        if self.accept('LPAREN'):
            if not self.Disj():
                return False
            if self.accept('RPAREN'):
                return True
            return False

    def Disj(self):
        if not self.Conj():
            return False
        if self.accept('DISJ'):
            return self.Disj()
        return True

    def Conj(self):
        if not self.ID():
            return False
        if self.accept('CONJ'):
            return self.Conj()
        return True

    def parse(self):
        while True:
            if not self.curTok:
                break
            if not self.Rel():
                self.errorMessage()
                return
        print("Correct syntax")
