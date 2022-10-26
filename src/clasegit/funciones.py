#x =  ['mariana', 'ricardo', 'gerardo']
#y = [ 'ramirez', 'cortes', 'ortiz']

#for i in range(len(x)):
#    print(x[i], y[i])

import sys

def main():
    x =  ['mariana', 'ricardo', 'gerardo']
    y = [ 'ramirez', 'cortes', 'ortiz']

    ver1(x,y)
    #ver2(x,y)
    #ver3(x,y)
    #ver4(x,y)
    #ver5(x,y)
    #ver6(x,y)

    

def ver1(x,y):
    for i in range(len(x)):
        print(x[i], y[i])
        



def ver2(x, y):
    print("version 2")
    z = ['laguna', 'morales', '']
    for i, j ,k in zip(x, y, z):
        print(i, j, k)

def ver3(x, y):
    print("version 3")
    n = 1
    for i in x:
        print(n, i)
        n += 1

def ver4(x, y):
    print("version 4")
    for n, i in enumerate(x, 1):
        print(n, i)

def ver5(x, y):
    print("version 5")
    for n, (i, j) in enumerate(zip(x, y), 1):
        print(n, i, j)

def ver6(x, y):
    print("version 6")
    for n, (i, j) in enumerate(zip(x, y), 1):
        #text ="{}. {} {}".format(n, i, j)
        text = f"{n}. {i.title()} {j.title()}"
        print(text)



if __name__ == '__main__':
    main()
