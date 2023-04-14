import json

class Database:
    def __init__(self):
        self.path = "db.json"
        self.json = {}
        self.read()

    def write(self):
        f = open(self.path, "w")
        f.write(json.dumps(self.json))
        f.close()

    def read(self):
        try:
            f = open(self.path, "r")
            self.json = json.loads(f.read())
            f.close()
        except:
            return

    def find_all(self, key: str, check: classmethod, *args):
        try:
            ret = []
            for d in self.json[key]:
                if check(d, *args):
                    ret.append(d)
            return ret
        except KeyError:
            return False

    def find(self, key: str, check: classmethod, *args):
        try:
            for d in self.json[key]:
                if check(d, *args):
                    return d
            return False
        except KeyError:
            return False

    def get(self, key: str):
        try:
            return self.json[key]
        except:
            return []
    
    def push(self, key: str, data: str):
        try:
            self.json[key].append(data)
        except:
            self.json[key] = []
            self.json[key].append(data)
        self.write()
    
    def pop(self, key: str, data: str):
        try:
            indx = self.json[key].index(data)
            self.json[key].pop(indx)
        except KeyError:
            return
        except ValueError:
            return
        self.write()
