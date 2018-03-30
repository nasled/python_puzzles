
class StringBuilder:
    def __init__(self):
        self.string = ''

    def append(self,value):
        self.string += value

    def get(self):
        return self.string


# q = StringBuilder()
# q.append('test')
# q.append('ssss')
#
# print(q.get())