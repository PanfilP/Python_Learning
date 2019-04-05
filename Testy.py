x=(input("input number"))

c = 0
def end():
    print(x,type(x))
def input_number():
    if "," in x:
        x=x.replace(",",".")
        x = float(x)
        end()
    elif "." in x:
        x=float(x)
        end()
    elif x.isdigit():
        x=float(x)
        end()
    else:
        x = str(x)
        print("you have entered wrong value")
        while c<3:

            # l = 3 - c
            # print(type(l))
            x = (input("input number, {} chance left".format(3-c)))
            c+=1
            try:
                x=float(x)
                print("at last")
                end()
            except:
                if c==3:
                    print("bye bye")
                else:
                    print("one more time")

