class parent:
    def infor(self):
        print("Rohan is father of madan----:")
class p2:
    def info(self):
        print("madan is the son of Rohan---:")
class child1(parent,p2):
    def inform(self):
        print("ratan is also the son of Rohan---:")
c=child1
c.info
c.infor
c.inform