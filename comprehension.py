# double the array value

values = [20,23,78,100,200]
double_values = []
for value in values:
  double_values.append(value*2)
# print(double_values)

# comprehension method
double_values = [ value*2 for value in values]
# print(double_values)

# squaring numbers
nums = [1,2,3,4,5,6,7,8,9]
squar_even_nums = []
for num in nums:
    if num % 2==0:
     squar_even_nums.append(num**2)
    # print(squar_even_nums)
    
#comprehension method

squar_even_nums = [num**2 for num in nums if num % 2 == 0]  
print(squar_even_nums)