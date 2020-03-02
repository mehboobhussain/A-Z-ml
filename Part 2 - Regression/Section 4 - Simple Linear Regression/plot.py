# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 06:48:39 2020

@author: S134002
"""
'''PLotting a graph in python is quite easy using matplotlib libraray. 
However, plotting the right graphs is challenging
'''
from matplotlib import pyplot as plt

''' Graphs get into each other so only the relevant code has to be executed
otherwise, python will mix the graphs while displaying
'''


years = [1950,   1960,   1970,   1980,   1990,    2000,    2010]
gdp   = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#make sure number of elements in both the arrays are same

#plt.bar(years, gdp, color = 'green', marker = 'o', linestyle = 'solid')
plt.plot(years, gdp, color='green', marker = 'o', linestyle='solid')
plt.title('Nominal GDP')
plt.ylabel('Billions of $')
plt.show()

movies = ['Annie Hill', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West-side story']
num_oscars = [5, 11, 3, 8, 10]
xs = [i+0.1 for i, j in enumerate(movies)]

plt.bar(xs, num_oscars, width = 0.7)
plt.title("my favorite movies")
plt.ylabel("no of academy awards")
plt.xticks([i for i, _ in enumerate(movies)], movies)
plt.show()


from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade //10 * 10
histogram = Counter(decile(grade) for grade in grades)

keys = [x for x in histogram.keys()]
values = [x for x in histogram.values()]
print (keys, values)

plt.bar(histogram.keys(), histogram.values(), width = 8)
plt.axis([-5, 105, 0, 5])
plt.xticks([10 * i for i in range(11)])
plt.ylabel("No of students")
plt.title("Distribution of grades in class 1")
plt.show()

mentions = [500, 505]
years = [2013, 2014]
plt.bar([2012.6, 2013.6], mentions, width = 0.8)
plt.xticks(years)
plt.axis([2012, 2014.5, 0, 550])
plt.show()

# line charts
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
zipped = [i for i in zip(variance, bias_squared)]
total_error = [x + y for x, y in zipped]
xs = [i for i, _ in enumerate(variance)]

# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance,     'g-', label = 'variance')
plt.plot(xs, bias_squared, 'b-.',  label = 'bias')
plt.plot(xs, total_error,  'r:.',  label = 'total error')

#plt.plot(xs, variance, 'g-', label='variance') # green solid line
#plt.plot(xs, bias_squared, 'r-.', label='bias^2') # red dot-dashed line
#lt.plot(xs, total_error, 'b:', label='total error') # blue dotted line


# because we've assigned labels to each series
# we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()

friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)
# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
   plt.annotate(label,
                xy=(friend_count, minute_count), # put the label with its point
                xytext=(5, -5), # but slightly offset
                textcoords='offset points')
plt.title("Daily Minutes vs. Number of Friends")
plt.show()

test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]
plt.scatter(test_1_grades, test_2_grades)
plt.axis("equal")
plt.title("Axes Aren't Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.show()