import random

def Convert_Text(_string):
    s = _string
    integer_list = []
    for c in s:
        integer_list.append((ord(c)))
    return integer_list

def Convert_Num(_list): #using list input from user
    _string = ''
    for i in _list:
        _string += chr(i)
    print(_string)
    return _string

def FME( b, n, m): #b**n mod m 
    x = 1
    while (n>0): # while the exponent is greater than 0 
        if (n%2 == 1):
            x = (x * b) % m
        n = n >> 1 #shifting bits to right by 1 place
        b = (b * b) % m #new base value 
    return x

def Euclidean_Alg(a, b):
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x #return resulting x when y = 0

def Find_Public_Key_e(p, q):
    e = 0
    #check to make sure p and q are prime
    #essentially just returning false if p or q are divisible by any numbers other than themselves
    #^because that would indicate they're composite 
    for i in range(2,p):
        if p % i == 0:
            print(p,"is not prime")
            return False
    for i in range(2,q):
        if q % i == 0:
            print(q,"is not prime")
            return False
    
    n = p*q
    l = (p-1)*(q-1)
    
    #list of primes to use for e
    e_lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977]
    e = random.choice(e_lst) #using choice function from random module to (pseudo) randomly select an e 

    return (e, n)

def Find_Private_Key_d(p,q): 
    #finding d (inverse of e mod(p-1)(q-1) )
    #intialize s_one, t_one, s_two, t_wo
    s_one = 1 
    t_one = 0
    s_two = 0
    t_two = 1
    l = (p-1)*(q-1)
    j = e
    t_l = l

    while t_l > 0:
        k = j % t_l
        w = j // t_l
        j = t_l
        t_l = k
        sh_one = s_two
        th_one = t_two
        sh_two = s_one - w*s_two
        th_two = t_one - w*t_two
        s_one = sh_one
        t_one = th_one
        s_two = sh_two
        t_two = th_two
        if s_one > 0:
            d = s_one
        elif s_one < 0: #otherwise, elif statement for dealing with negative inverse
            a = l + s_one
            d = a
    return d,n #return value of d (inverse) and n 

def Encode(n, e, message): #using public key info and message to be encoded as parameters
    m = Convert_Text(message)
    cipher_text = []
    for i in m:
        c = FME(i,e,n)
        cipher_text.append(c)
    return cipher_text

def Decode(n, d, cipher_text): #use n and private key d values input from user, as well as cipher_text from user as parameters
    message = ''
    msg_list = []
    for i in cipher_text:
        m = FME(i,d,n)
        msg_list.append(m)
    message = Convert_Num(msg_list)
    return message #return final message  

def factorize(n): #factorize function to find the two prime factors of n 
    for p in range(2,n-1):
        if n%p == 0:
            q = n//p
            return p,q
    return False

if __name__ == '__main__':
    choice = "y"
    while choice.lower() == "y" or choice.lower() == "Y":
        print("---------------------")
        print("MENU:") #setting up menu for selecting commands 
        print("1. Get keys (enter'1')")
        print("2. Encode (enter '2')")
        print("3. Decode (enter '3')")
        print("4. Codebreak (enter '4')") #codebreak function just gives private key from info input by user
        a = input("Which action would you like to perform? ")
        if a == "1": #if user types "1", ask for input relevant to get keys 
            p = input("Enter first prime number: ")
            q = input("Enter second prime number: ")
            p = int(p)
            q = int(q)
            e,n = Find_Public_Key_e(p,q)
            print("Public key (e,n): ", (e,n))
            d,n = Find_Private_Key_d(p,q)
            print("Private key (d,n): ",(d,n))
            print(" ")
        if a == "2":
            message = input("Message to encrypt: ")
            e = input("Enter public key e (e,n): ")
            n = input("Enter n: ")
            n = int(n)
            e = int(e)
            cipher_text = Encode(n,e,message) #call Encode function using n,e,and message and assign return value to cipher_text
            print(cipher_text)
            print(" ")
        if a == "3":
            cipher_text = input("Coded message: ")
            cipher_text = cipher_text.replace("[","")
            cipher_text = cipher_text.replace("]","")
            n = int(input("Enter n from public key (e,n): "))
            d = int(input("Enter private key d: "))
            cipher_text = [int(i) for i in cipher_text.split(',')]
            Decode(n,d,cipher_text)
            print(" ")
        if a == "4":
            e = int(input("Enter public key e (e,n): "))
            n = int(input("Enter public key n: "))
            p,q = factorize(n)
            print("p = ",p)
            print("q = ",q)
            d,n = Find_Private_Key_d(p,q)
            print("Private key (d,n): ",(d,n))
            print(" ")
        choice = input("Perform another action? (y/n): ") 
        print()
    print("Bye!") 
