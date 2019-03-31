print("Kalkulator BMI")
data=[0,0]
# def input_weight():
#     w=int(input("wprowadź swoją wagę w[kg]"+"  "))
#
#     print(w)
#     data[0]=w
# input_weight()
# print(data)
w=0
h=0
def input_weight():
    w=int(input("wprowadź swoją wagę w[kg]"+"  "))
    try:
        w=float(w)
        w=int(w)

        if w<10:
            print("Chyba się pomyliłeś. To niemożliwe, że tyle ważysz!\nChcesz poprawić wprowadzoną wartość? ")
            d=input("T/N"+ " ")
            if d=="t":
                input_weight()
            elif d=="n":
                print("as u wish")
                input_height(h)
        elif w>175:
            print("To nie możliwe, żeś taki olbrzym")
        else:
            print("Twoja waga to", w)
        data[0]=w
    except:
        print("wprowadzona wartość jest nieprawidłowa")
        input_weight()

def input_height():
    h=input("wprowadź swój wzrost w [cm]"+"  ")
    try:
        h=float(h)
        h=int(h)
        if h<120:
            print("Chyba się pomyliłeś!\nChcesz poprawić wprowadzoną wartość? ")
            d=input("T/N"+ " ")
            if d=="t":
                input_height()
            elif d=="n":
                print("as u wish")
                count(r)
        elif h>215:
            print("To nie możliwe, żeś taki olbrzym")
        else:
            print("Twój wzrost to", h)
        data[1]=h
    except:
        print("wprowadzona wartość jest nieprawidłowa")
        input_height()

input_weight()
input_height()

# print(data)
# print(data[1])
w=data[0]
h=data[1]
# print(w,h)
r=(w/((h/100)**2))

print("Twoje BMI to:"+" ",r)

# if r<18.5:
#     print("masz niedowagę")
# elif r>=24.99:
#     print("masz poważną nadwagę")
# else:
#     print("dobrze się prowadzisz")