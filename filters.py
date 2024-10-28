 
#  filter(function , data)

grades = ['A','D','C','F','A','F','B']
# def remove_fails(grade):
#     return grade!='F'

# print(list(filter(remove_fails,grades)))  
#  BTW(by the way) list() is type casting when you remove this it returns object


#  we can also use for loop 

filterd_grades = []
for grade in grades:
    if grade != 'F':
      filterd_grades.append(grade)
# print(filterd_grades)

# also use comprehension method 

print([grade for grade in grades if grade!='F'])