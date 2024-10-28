nums = [1,2,3,4,5,6,7]

# def squere(n):
#     return n*n

# print(list(map(squere,nums)))

# instead of this we can use lambda function  (it is inline anonymos function)
print(list(map(lambda n: n*n, nums))) 