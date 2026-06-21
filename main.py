#import the required functions 
from converter import convert
from sig import signature
dict = {}
def shorten(url,counter,key = 'my_secret_key'):
        count = convert(counter,62)
        si = signature(key,str(counter))
        short = "".join(count) + "." + "".join(convert(si,62))
        dict[short] = url


def print_dict():
    for key in dict:
        print(key,dict[key])

counter = 0
while True:
    print("enter 1 to shorten a url")
    print("enter 2 to print the dictionary")
    print("enter 3 to exit")
    c = int(input("enter your choice: "))
    if(c==1):
        url = input("enter the url: ")
        shorten(url,counter)
        counter+=1
    elif(c==2):
        print_dict()
    elif(c==3):
        break



