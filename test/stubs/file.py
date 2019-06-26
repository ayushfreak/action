# pyre-strict
class First(object):
    def __init__(self, name):
        print(name)


class Second(object):
    def __init__(self, name):
        self.name = name

    def func(self):
        print(self.name)

