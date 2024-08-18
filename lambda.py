# def square(num): return num**2

# numbers = [1,3,5,9]

# result = list(map(square, numbers))
# print(result)

# for item in map(square, numbers):
#     print(item)

numbers = [2,4,6,8]
result = list(map(lambda num: num**2, numbers))
print(result)