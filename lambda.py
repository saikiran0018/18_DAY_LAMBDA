a lambda function to clculate sum of two numbers
f = lambda x,y,z: x+y+z 
s = lambda x,y,z: x*y*z
r= f(3,10,2)
z= s(2,3,5)
print('sum =',r)                                   #15
print('mul =',z)                                   #30


m = lambda x,y : x if x>y else y
x,y= [int(n) for n in input("enter two integer:").split()]
print(m(x,y))

a= [int(x) for x in input("enter two integer:").split()]
print("bigger is",max(a))
print("smaller is",min(a))

a=20,40,50
print(max(a))                                        #50
print(min(a))                                        #20 


a=[int(x) for x in input().split()]
b= list(filter(lambda x: (x%2 == 0), a))
c= list(filter(lambda x: (x%2 != 0), a))
print(b)
print(c)


f = lambda x: x**2
value = f(7)
print('square of 4 =', value)