# Sample Input
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika




n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
query_scores=student_marks.get(query_name)
print(len(query_scores))
if query_scores:
    average=sum(query_scores)/len(query_scores)
    print(f"{average:.2f}")
else:
    print("Student not found")

