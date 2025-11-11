semesters = ["s1", "s2", "s3"]
modules = ["m1","m2","m3", "m4", "m5", "m6", "m7", "m8", "m9", "m10"]
size = 3

modulsplit = [modules[i:i+size] for i in range(0, len(modules), size)]
print(modulsplit)

semestereinteilung = dict(zip(semesters, modulsplit))
print(semestereinteilung)

for s, m in zip(semesters, modulsplit):
    print(s, m)
