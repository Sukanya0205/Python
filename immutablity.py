
# ========== immutable =========

# a=10
# b=10
# c=34
# print("a",a)
# print("b",b)
# print("c",c)
# print("Address of a:",id(a))
# print("Address of b:",id(b))
# print("Address of c:",id(c))

# c=43
# print("Address of a:",id(a))
# print("Address of b:",id(b))
# print("Address of c:",id(c))


# a="Python"
# b="Python"
# c="Java"
# print("a",a)
# print("b",b)
# print("c",c)
# print("Address of a:",id(a))
# print("Address of b:",id(b))
# print("Address of c:",id(c))

# c="C++"
# print("Address of a:",id(a))
# print("Address of b:",id(b))
# print("Address of c:",id(c))


# a=5.6
# b=1.1
# c=5.6
# print("a",a)
# print("b",b)
# print("c",c)
# print("Address of a:",id(a))
# print("Address of b:",id(b))
# print("Address of c:",id(c))

# b=5.6
# print("Address of a:",id(a))
# print("Address of b:",id(b))
# print("Address of c:",id(c))



# ======= mutable =======

# l1=[10,20,30]
# l2=[10,20,30]
# print("l1:",l1)
# print("l2",l2)

# print("Address of l1:",id(l1))
# print("Address of l2:",id(l2))

# l1[2]='Hiii'
# print("l1:",l1)
# print("l2",l2)

# print("Address of l1:",id(l1))
# print("Address of l2:",id(l2))


# datatypes
# byte and bytarray

# byte = immutable
# bytearray = mutable

# 1]byte 

# x=[10,20,30]
# print("type(x):",type(x))
# b=bytes(x)
# print("type(b):",type(b))
# b[0]=100


# 2]bytearray
# x=[10,20,30]
# print("type(x):",type(x))
# b=bytearray(x)
# print("b=",b)
# print("type(b):",type(b))
# b[0]=100
# print("b=",b)
# for i in b:
#     print("i=",i)


# =============== list ===============

# l1=[10,20,30,"python",True]
# print(l1)
# print(type(l1))
# print(l1[2])
# print(l1[2:])

# l1.append(100)
# print(l1)


# l1.remove("Python")
# print(l1)


# l=[]
# print(l)
# print(type(l))


# =========== Tuple ===========

# t=(10,30,40,"Python",2.34,10)
# print(t)
# print(type(t))

# t=(10,)
# print(t)
# print(type(t))

# t=10
# print(t)
# print(type(t))

# t=10,20,30
# print(t)
# print(type(t))


# ============ Range ============

# for i in range(1,21,2):
#     print(i)

# for i  in range(10,0,-1):
#     print(i)


# ============== Set ===============

# s={10,20,"Sukanya"}
# print(s)
# print(type(s))


# s1={}
# print(s1)
# print(type(s1))


# s={10,20,"Sukanya",10}
# s={10,20,"Sukanya",10}

# print(s[2])
# print(type(s))
# s.add("java")
# print(s)


# ======== Frozen Set =immutable ========

# s={10,20,"OM"}
# print(s)
# print(type(s))
# fs=frozenset(s)
# print(fs)
# print(type(fs))


# ======= Dict= mutable ========

# d={1:"Python",2:"Java", 2:"Datascience" ,'a':10 , "Fname":"OMAAA"}
# print(d['fname'])
# print(d)
# print(type(d))


