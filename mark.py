''' Модуль для маркировки объектов'''
class Marked:
    def __init__(self, obj):
        self.o = obj
        self.marks = []
    def Is(self, m):
        return m in self.marks
    def mark(self, m):
        self.marks.append(m)
    def unmark(self, m):
        try:
            self.marks.remove(m)
        except ValueError:
            pass
