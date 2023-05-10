
class TextEditor:
    def __init__(self):
        self.cache = []
        self.S = ""

    def append(self, W: str):
        self.cache.append(self.S)
        self.S = "".join([self.S, W])

    def delete(self, k: int):
        self.cache.append(self.S)
        self.S = self.S[:-k]

    def print(self, k: int):
        print(self.S[k-1])

    def undo(self):
        self.S = self.cache.pop()

    def do(self, op: str):
        args = op.split(" ")
        arg0 = args[0]
        if arg0 == "1":
            self.append(args[1])
        elif arg0 == "2":
            self.delete(int(args[1]))
        elif arg0 == "3":
            self.print(int(args[1]))
        elif arg0 == "4":
            self.undo()

def main():
    editor = TextEditor()
    n_ops = input()
    for _ in range(int(n_ops)):
        op = input()
        editor.do(op)

main()
        