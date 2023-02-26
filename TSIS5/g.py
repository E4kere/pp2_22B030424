test = str(input())
 
print(test)

temp = test.split('_')

res = temp[0] + ''.join(ele.title() for ele in temp[1:])

print(res)
