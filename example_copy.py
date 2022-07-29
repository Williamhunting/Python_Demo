from ctypes import *
import os.path  
import sys

import copy

l1 = [11, 12]
l2 = [21, 22]
num = 555

allOne = [l1, l2,num]


# 浅拷贝，创建出一个对象，并把旧对象元素的 引用地址 拷贝到新对象当中。
# 也就是说，两个对象里面的元素通过浅拷贝指向的还是同一个地址
allOne2 = copy.copy(allOne)
print(id(allOne))
for i in range(0,3):
    print(id(allOne[i]))


l1[0] = 16 # 此处修改，会使得 allOne 和 allOne2的第0个元素的值都发生改变，因为l1是List，是可变对象
allOne[2] = 666 # 此处修改，只会改变allOne的num的值，因为不可变对象一旦重新复制，地址就会发生改变。（不可变嘛）

num = 777 # 此处不会改变 allOne 和 allOne2的值，因为相当于 777 复制给一个全新的地址，这个num跟其他num已经没关系了

print(allOne)
print(allOne2)

print("id allOne:"+str(id(allOne)))
print("id allOne[0]:"+str(id(allOne[0])))
print("id allOne[1]:"+str(id(allOne[1])))
print("id allOne[2]:"+str(id(allOne[2])))

print("===")
print("id allOne2:"+str(id(allOne2)))
print("id allOne2[0]:"+str(id(allOne2[0])))
print("id allOne2[1]:"+str(id(allOne2[1])))
print("id allOne2[2]:"+str(id(allOne2[2])))
