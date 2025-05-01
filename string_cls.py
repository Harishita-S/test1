#Strings can be represented between " " , ' ',"""""
S1='Python'
S2="Python"
S3="""Python"""
print(type(S1),type(S2),type(S3))
#S4="I am studying " Python " " #invalid syntax has python should be inside string
S4='I am studying "Python" ' #this will work  
print(S4) 

S5="I am studying, \"Python\"."  #\inside backlash\ if giving any String it will work
print(S5)

S5="I am studying 'Python'"  
print(S5)

#multiline string used with 3 double quotes """  """ and ''' '''
S9 = """My name is Alice     
I am handling python session
for DBDA students """
print(S9)

S6='''CDAC Chennai offering
Two courses
PG-DAC and PG-DBDA'''
print(S6)


#S1[0]='M' #string is immutable so cannot add


# operations of the string
# length of the string
print("Length of the string 3 is ",len(S3))
print("Length of string 6 is " , len(S6))

# Array of string
print(S6[3]) #3
print(S6[5:10]) # Chenn
print(S6[-39:-30]) #offering

S7="01234-PQRST-678039"
#find the individual string using slicing
#positive
print(S7[0:5])  # 01234
print(S7[6:11])  #PQRST
print(S7[12:])  # 678039

#negative 
print(S7[-18:-13]) # "01234"
print(S7[-12:-7])  # "PQRST"
print(S7[-6:])  #678039

# compare two string
s1='Python'
s2="Python"
s3='python'
print(s1==s2) #True -> strings does not matter the variable is imp
print(s1==s3) #False -> small letter p

# join two or more strings
name='Prema'
greet =' Welcome '
print(greet + name) # Welcome Prema

# Membership test
print('e' in name) #True
print(' ' in greet) #True
print('c' not in greet) #False

# String Methods
# Strip to remove the whitespaces or other strings
print(greet)
print(greet.strip()) #remove space ' Welcome ' became 'Welcome'
s4='Hello World ???'
print(s4)
print(s4.rstrip('?')) #rigth side stripped, can also use left strip to remove from left side
s5='taj mahal'
print(s5)
print(s5.capitalize()) # Taj mahal
print(name)
print(name.lower())  #prema
print(greet)
print(greet.upper()) #WELCOME

# startswith , endswith -> output ->tue/False
print(s4.startswith('Hello')) #True
print(name.startswith('Hi')) #False
print(s4.endswith('?')) #True
print(name.endswith('.')) #False

# find
print(s4.find('World')) # returns value from which index it is starting,i.e 6 which is index of W

print(greet.find('e')) # returns index of 1st occurence of e i.e 2

# replace
print(name.replace('Prema','John'))
print(s4.replace('World','Pratap'))
print(greet.replace('e','ee'))
print(greet.replace('e','ee',1)) #changes e in first occurence e as ee
print(greet.replace('e','ee',0)) #0 no change

# split
print(S9)
print(S9.split(' '))
print(S9.split(' ',2))

# isalpha,isalnum -> checks presence of alphabets and numerbers and space and digit
S8='Hi 930'
print(S7,S7.isalpha()) #False-> as digits are also present , true-> will be aplha
print(name)#Prema
print(name.isalpha()) #True
print(name.isalnum()) #True-> returns true, it checks strings,alpha,num
print(name.isspace()) #false
print(greet)
print(greet.isalnum()) #False-> 
print(greet.isspace())  #false-> as it has alpha too, only if space present it will be true
S8='  '
print(S8.isspace())
print(S7.isdigit()) #False -> as it has both alpha nd numer, will be true only is 
print(S7.isalnum())

#join
text=['Python','Java','C','MySQL']
print(' '.join(text))
print('/'.join(text))

txt1='123'
txt2='abc'
#1abc2abc3
print('txt2.join(txt1):',txt2.join(txt1))

s='>>'
print(s.join(txt1)) #1>>2>>3
print(txt1+txt2) # using concat, 123abc

