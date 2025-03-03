import sys
input = sys.stdin.readline
student = []
no_student = []                 
for _ in range(28):
    num = int(input())
    student.append(num)

for i in range(1, 31):
    if i not in student:
        no_student.append(i)

print(min(no_student))
print(max((no_student)))