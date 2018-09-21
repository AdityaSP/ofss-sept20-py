fh = open(r'C:\Users\Dell lap\Desktop\Python\oracle\mar-5-9\idea\marks.txt')
data = [ line.strip().split(":") for line in fh]
#[['1', '44,74,61,54,37,51'], ['2', '66,36,91,59,65,79'], ...

marks = [ [m[0], map(int, m[1].split(','))] for m in data]
#[['1', [44, 74, 61, 54, 37, 51]], ['2', [66, 36, 91, 59, 65, 79]], ...

total_marks=[ [m[0], sum(m[1])] for m in marks]
#[['1', 321], ['2', 396], ...

#convert to a dictionary
total_d = dict(total_marks)
print total_d['200']

print "Top 3 scorers"
print sorted(total_marks, key = lambda x: x[-1], reverse=True)[:3]

print 'Bottom 3 scorers'
print sorted(total_marks, key = lambda x: x[-1])[:3]

print "Marks scored by top 3"
print sorted(marks, key = lambda x: sum(x[1]), reverse=True)[:3]

print "Scored centum in atleast one subject"
print len(filter(lambda x: 100 in x[1], marks))

print "Scored centum in more than one subject"
print len(filter(lambda x: x[1].count(100) > 1, marks))