def square(number):
    return number **2
    
w =[1,2,3,4,5]
squared = map(square, w)
list(squared)

for i in squared:
    print(i.group())