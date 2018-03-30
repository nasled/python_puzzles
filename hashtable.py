
import hashlib
from pprint import pprint

# HashTable
class HashTable:
    def __init__(self):
        self.data = {}
        pass

    def hash(self, variable):
        m = hashlib.md5()
        m.update(str(variable).encode('utf-8'))
        return m.hexdigest()

    def get(self, variable):
        hash = self.hash(variable)
        return self.data[hash]

    def set(self, variable, value):
        hash = self.hash(variable)
        self.data[hash] = value
        pass

    def dump(self):
        pprint(self.data)


# q = HashTable()
# q.set('hey1', 'object')
# q.set('hey2', 'object')
# w = q.get('hey1')
#
# pprint(w)
# q.dump()
