class StringVar:
    def __init__(self):
        self.s = ''
    def set (self, deyst):
        self.s = deyst
        return deyst.upper()
    def get(self):
        return self.s

s = StringVar()
print(s.set('всем привет'))
print(s.get())
