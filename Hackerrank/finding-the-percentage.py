if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    mlist = []
    avg = 0
    for _ in range(n):
        name, *line = input().split()  # name and marks
        scores = list(map(float, line))  # list of marks
        student_marks[name] = scores  # adding name and marks in dictionary
    query_name = input()
    for key, values in student_marks.items():
        if key == query_name:
            mlist.extend(values)
            break
    for marks in mlist:
        avg = avg + marks
    avg = avg / len(mlist)
    print('{n:4.2f}'.format(n=avg))