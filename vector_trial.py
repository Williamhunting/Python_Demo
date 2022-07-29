from vectormodule import Vector

def main():
    v = Vector(19)
    v[3] = 12   #用v[n]对Vector对象赋值不能直接完成，因为它只能用于python已有的数据类型（列表、字典、元组）
                      #需要重载__setitem__特殊方法，
    v[-2] = 32
    print(v[3])
    u = v+v  #这里是Vecter对象相加，必须要在类定义中重载定义__add__，才可以使用+直接加
    print(u)
    total = 0
    for entry in v:
        total += entry
        
if __name__ == '__main__':
    main()
