import sys

class User:
    def __init__(self, buf):
        buf = buf.split(' ')
        self.name = buf[0].strip()
        self.surename = buf[1].strip()
        self.age = buf[2].strip()

    def show(self):
        print("Name %s" % self.name)
        print("SureName %s" % self.surename)
        print("Age %s" % self.age)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("Usage python " + sys.argv[0] + " <filename>")
        sys.exit(-1)

    file = open(filename, 'r')
    buff = file.read()
    file.close()

    buff = buff.split("\n")
    users = []
    for i in buff:
        users.append( User(i))

    for i in users:
        i.show()

    print(buff)
