L1=[]
L2=[2,3,434,'Apple','Poonam',7.90,8.34]

# inserting elements into the list

L1.append('Goa')
L1.append('Grapes')
L1.append('Orange')
print("L1 list",L1)
print("L2 list",L2)

# inserting elements by using insert method

L1.insert(1,"Jack Fruit")
print("After inserting Jack fruit",L1)
L1[2:4]=("Pine Apple","Strawberry","Watermelon")
print(L1)
L1.insert(3,"Kiwi")
print(L1)

# accessing elements from the list using positive index
print(L1[0])
print(L2[3])
print(L2[2:5])
print(L2[:4])
print(L2[:])
print("Length of tbe list 2 is ",len(L2))

# accessing elements from the list using negative index
print(L2[-1]) # 8.34
print(L2[-7]) # 2
print(L2[-7:-4])# 2,3,434
print(L2[:-1]) # before -1 elements will be printed

# membership test
print("Apple" in L2)
print('Kiwi' in L2)
print('Kiwi' not in L2)
print(434 in L2)

# how to delete elements from the list
# del,remove,pop
print(L2)
del(L2[1])
print("L2 after deletion: ",L2)
del L2[2:4]
print(L2)
# del L2- will delete the list
# deleting elements from the list using remove method
L2.remove(434)
print(L2)

print("Before removing List 1",L1)
L1.remove('Kiwi')
print("After deleting",L1)

# deleting elements from the list using pop method
print(L1)
L1.pop() #works like stack last in First out if no index is mentioned
print(L1)
L1.pop(3)
print("After removing index 3",L1)
L1.pop(0)
print("After removing index 0",L1)

#list method (append,insert,del, remove, pop,in,not in
# count, index,max,min,sum,len,clear)
#count method
L3=[2,3,4,2,6,5,7,2,3,4]
print("counting 2 element in the list",L3.count(2)) #number 2 frequency is counted

# index method
print("Inex value of element 6 in the list is",L3.index(6)) # the value of number 6 index value is given

#extend
L4 = [9,10,11]
L3.extend(L4)# adding the L4 elements after the L3 values
print("List 3 extends with list 4",L3)

#max
print("Maximum value in the list is",max(L3)) #returns maximum value in the list

#min
print("Minimum value in the list is",min(L3)) #returns minimum value in the list

#sum
print("total value in from the list is",sum(L3))

#clear method
#L3.clear()
print(L3)
L5=['Python']
print(L5*4) # 4 times it will print python

#sort method
#L3.sort()
#print(L3) 

#reverse
#print("Reverse order",L3[::-1])

#L3.sort(reverse=True)
#print("Reverse",L3)

#print("Sorting in Ascending order",sorted(L3))
L6=reversed(L3)
print("Reversing",list(L6))# if not working use the below method
#L3.reverse()
#print("Sorting in Descending order",L3 )

#list comprehension

L7=[x*x for x in L3]
print("Squared the element of list L3",L7)
pow2=[2**x for x in L3] # creating power of the elementslist i.e 2^1,2^2,2^3
print("Powered list",pow2)

#even_num=[x%2==0 for x in L3]
#print("even number:",even_num)
even_num=[x for x in L3 if x%2==0]
print("even numbers",even_num)

odd_num=[x for x in L3 if x%2!=0]
print("Odd number",odd_num)

#without list comprehension to find even and odd numbers
L9=[]
for x in L3:
    L9.append(x*x)
print(L9)

el=[]
ol=[]
for x in L3:
    if x%2==0:
        el.append(x)
    else:
        ol.append(x)
print("Even number",el)
print("Odd number",ol)
