# No need to declare any type of variable

i=10
print(i)
i=i+.1
print(i)
i="test"
print(i)

x=50
y=x
print(id(x)) # print identity of x
print(id(y)) # print identity of y

min_bal=100
print(min_bal)

number_of_months=12
print(number_of_months)

a=b=c=4
print(a,b,c)
a,b,c=10,3,"Saurabh"
print(a,b,c)

s1="Hello World"
print(s1)
print(s1[0])
print(s1[2:6])
print(s1[3:])
print(s1*3)
print(s1+"My Dear Friend")