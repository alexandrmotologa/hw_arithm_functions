# def add( a, b ):
#     result = a + b
#     print(result)
# add()


def add(a=None, b=None):
        while True:
            try:
                a = float(input("Introduceti prima cifra intreaga sau zecimala : "))
                b = float(input("Introduceti a doua cifra intreaga sau zecimala : "))
                if a != int(a):
                    result = a + b
                    print(result)
                    break
                else:
                    result = int(a) + int(b)
                    print(result)
                    break
            except:
                print("That's not a valid option!")
add()
