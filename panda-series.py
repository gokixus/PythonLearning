import pandas
import numpy

numbers = [20,30,40,50]
letters = ["a", "b", "c", "d", "e"]
pandas_series1 = pandas.Series(numbers)
pandas_series2 = pandas.Series(letters)
pandas_series3 = pandas.Series(5, [0,1,2,3,4])
pandas_series4 = pandas.Series(numbers, ["a","b","c","d"])
dict = {"a":10, "b":20, "c":30, "d":40}
pandas_series5 = pandas.Series(dict)
print(pandas_series1)
print(pandas_series2)
print(pandas_series3)
print(pandas_series4)
print(pandas_series5)

random_numbers = numpy.random.randint(10, 100, 6)
pandas_series6 = pandas.Series(random_numbers)
print(pandas_series6)
numbers_array = numpy.array([20,30,40,50])
pandas_series7 = pandas.Series(numbers_array, ["a", "b","c","d"])
print(pandas_series7)

