from collections import Counter
from matplotlib import pyplot as plt

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

print(histogram)

plt.bar(
        [x+5  for x in histogram.keys()], 
        histogram.values(), 
        10,  # each bar width of 10 unit
        edgecolor=(0, 0, 0)
        )
plt.axis([-5, 105, 0, 5])  # x-axis from -5 to 105
plt.xticks([i*10  for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()