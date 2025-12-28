class parent:
    def infor(self):
        print("Rohan is father of madan----:")
class child(parent):
    def info(self):
        print("madan is the son of Rohan---:")
class vicechild(child):
    def inform(self):
        print("ratan is also the son of Rohan---:")
c=vicechild()
c.info()
c.infor()
c.inform()