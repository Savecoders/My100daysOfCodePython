import pandas as pd


A = pd.Series([2, 3, 4, 5], index=['a', 'b', 'c', 'd'])

type(A.values)
# the type is numpy.ndarray

type(A)
# the type is:
# pandas.core.series.Series

grades_dict = {'A': 1, 'B': 2, 'C': 3}
marks_dict = {'A': 32, 'B': 12, 'C': 22}

grads = pd.Series(grades_dict)
marks = pd.Series(marks_dict)

print(grads.values)
print(marks.values)

# the atribute values return the
# values keys of the dictionary

myDataFrame = pd.DataFrame({'Marks': marks, 'Grads': grads})

print(myDataFrame)
# print the table

print(myDataFrame.T)
# invert the column

myDataFrame['ScaledMarks'] = 100*(myDataFrame['Marks'] / 90)

print(myDataFrame)
# add the column ScaledMarks
