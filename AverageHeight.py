student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
sumHeight = 0
numOfHeights = 0
for height in student_heights:
    sumHeight += height
    numOfHeights += 1
print(round(sumHeight/numOfHeights))
