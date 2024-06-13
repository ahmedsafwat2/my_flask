class SomeObj():
    def __init__(self, param):
        self.param = param
    def query(self):
        self.param += 1
        return self.param

global_obj = SomeObj(0)