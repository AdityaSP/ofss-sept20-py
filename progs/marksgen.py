import random

def get_marks():
    return ",".join([str(random.randint(35, 100)) for x in range(6)])

college = [str(x) + ":" + get_marks() + "\n" for x in range(1, 501)]

with open('marks.txt', 'wt') as fh:
    fh.writelines(college)

print "Job Done. Marks created"