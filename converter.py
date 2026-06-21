#define the function that will convert the number to the base specified
def convert(n,b):
    #initialize the array that will store the digits of the final number
    array =[]
    #initialize the hashmap that will store the mapping from number to letter for bases greater than 10
    encoding = {}
    i = 10
    j = 65
    while(i<=35):
        encoding[i]=chr(j)
        i+=1
        j+=1

    j=97
    while(i<=61):
        encoding[i] = chr(j)
        i+=1
        j+=1


    #populate the array by dividing until the quotient goes below 1 and store the remainders
    while(n>=1):
        temp = n%b
        array+=[str(temp) if temp<10 else encoding[temp]]
        n=n//b

    #reverse the array since the remainders need to be stored in reverse order
    array.reverse()

    #return the array
    return array
