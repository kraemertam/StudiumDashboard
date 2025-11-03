# Tests für mein Programm
from domain.models import Course, Student, Module
from ui.dashboard import start_gui

m1 = Module("m1", "Mathe", 5)
m2 = Module("m2", "Python", 5)
m3 = Module("m3", "Deutsch", 5)
m4 = Module ("m4", "Biologie", 10)

c1 = Course("c1", "Angewandte Künstliche Intelligenz", 180)
c2 = Course("c2", "Informatik", 180)

c1.add_module(m1)
c1.add_module(m2)
c1.add_module(m3)
c1.add_module(m4)

c2.add_module(m1)
c2.add_module(m2)


print(c1)
print(c2)


s1 = Student("s1", "Tamara", "Krämer", 4,)
s2 = Student("s2", "Lisa", "Laus", 3)
print(s1)
print(s2)
print(s1.modules)

s1.enroll_course(c2)
s2.enroll_course(c1)
print(s1.modules)
print(s2.modules)

start_gui(s1.info_student())
start_gui(s2.info_student())

