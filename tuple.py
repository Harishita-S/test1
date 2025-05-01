T1=()
T2=(2,3,'Apple',9.87,[2,3,4])
print(type(T2))
#T2.append("Olive)#tuple cannot be appended as it is immutable so cannot add or change 
#print(T2)

print(T2[2]) #o/p -> Apple
T3="hello"
print(type(T3))

T4="hello",
print(type(T4))

print(T2[2][1]) # 2nd index is Apple and 1stindex value in apple is p,so p will be printed
print(T2[2][3]) # l
print(T2[4][1]) # 3
print(T2[4][1:3]) #3,4

# tuple cannot insert, append,remove as it is immutable 
#T2.append('Hello')
#print(T2)

#T2.remove('Apple')

# can delete entire Tuple alone but cannot remove items inside tuple
#del T2
#print(T2)

# within a tuple if list present then items can be added 
T2[4][1]=50
print(T2)

# convert whole tuple as list and insertion can be done
#and later again change it using tuple

L1=list(T2)
L1.insert(2,"Hello")
T2=tuple(L1)
print(T2)

# tuple methods index and count
T3=(3,5,6,7,6,5,4,6)
print(T3.count(6)) #3(frequency of 6)
print(T3.index(6)) #2(1st occurenece of the value index is taken)

#packing, unpacking 
T4=(20,30,'Prathik','Anbu')
#unpacking -> each below variables are assigned the values inside tuple
a,b,c,d=T4 #only char and string be used to assign 
print(a) #20
print(b) #30
print(c) #Pratik
print(d) #Anbu

print('a' in T4) #false
print('a' in T4[2]) # true
print('Anbu' in T4) #true
print(20 not in T4) #False


