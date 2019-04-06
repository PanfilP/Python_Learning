# w=float(0)
# h=float(0)
# d=[]
#
# def num():
#     x = 0
#     while x<2:
#         z=input("?")
#         d.append(z)
#         x+=1
# num()
#
# print(d)
d=[]
t=[0]
c=[0]
def input_num():
    x=input("?")
    t[0]=x
    print(t[0])
    check_value()
def check_value():

    if "."in t[0]:
        d.append(t[0])
    elif ","in t[0]:
        t[0].replace(",",".")
        d.append(t[0])
    elif t[0].isdigit():
        d.append(t[0])
    else:
        while c[0]<3:
            print("let us think")
            c[0] += 1
            print(c[0])
            input_num()


print("weight")
input_num()
input_num()

print(d)