class roster(object):
    "students and teacher class"
    teacher = ""
    students = []

    def __init__(self, tn='mayun'):
        self.teacher = tn

    def add(self, sn):
        self.students.append(sn)

    def remove(self, sn):
        self.students.remove(sn)

    def to_string(self):
        print "Teacher:", self.teacher
        print "Students:", self.students
        
if __name__ == '__main__':
    r = roster()
    r.add("mincong")
    r.to_string()
