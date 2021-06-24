# rsa

This is a project from one of my first undergraduate-level computer science classes (discrete structures).
I have not yet optimized the code beyond its original form.
This program utilizes fundamental concepts from discrete mathematics to encrypt and decrypt text using the RSA algorithm. 

Program commands: 
- create public and private keys
- encrypt a message
- decrypt a message
- codebreak

Ex): 
---------------------
MENU:
1. Get keys (enter'1')
2. Encode (enter '2')
3. Decode (enter '3')
4. Codebreak (enter '4')

Which action would you like to perform?  1

Enter first prime number:  179

Enter second prime number:  191

Public key (e,n):  (181, 34189)

Private key (d,n):  (21301, 34189)

Perform another action? (y/n):  y

---------------------
MENU:
1. Get keys (enter'1')
2. Encode (enter '2')
3. Decode (enter '3')
4. Codebreak (enter '4')

Which action would you like to perform?  2

Message to encrypt:  Almost time for a nap

Enter public key e (e,n):  181

Enter n:  34189

[22235, 268, 29141, 34081, 31237, 13083, 727, 13083, 24018, 29141, 10538, 727, 31600, 34081, 33792, 727, 30382, 727, 8727, 30382, 31461]
 
Perform another action? (y/n):  y

---------------------
MENU:
1. Get keys (enter'1')
2. Encode (enter '2')
3. Decode (enter '3')
4. Codebreak (enter '4')

Which action would you like to perform?  3

Coded message:  [22235, 268, 29141, 34081, 31237, 13083, 727, 13083, 24018, 29141, 10538, 727, 31600, 34081, 33792, 727, 30382, 727, 8727, 30382, 31461]

Enter n from public key (e,n):  34189

Enter private key d:  21301

Decrypted message: 'Almost time for a nap'
 
Perform another action? (y/n):  y

---------------------
MENU:
1. Get keys (enter'1')
2. Encode (enter '2')
3. Decode (enter '3')
4. Codebreak (enter '4')

Which action would you like to perform?  4

Enter public key e (e,n):  113

Enter public key n:  28794290241716387

p =  160481219

q =  179424673

Private key (d,n):  (23697955405914833, 28794290241716387)
 
Perform another action? (y/n):  y

---------------------
MENU:
1. Get keys (enter'1')
2. Encode (enter '2')
3. Decode (enter '3')
4. Codebreak (enter '4')

Which action would you like to perform?  3

Coded message:  [2579706886152660, 1506880588871094, 25824199538612172, 12324506914914625, 3910629358746840, 19942730250851363, 12407119628852595, 20436916271957116, 22358653510094960, 22358653510094960, 18133059900110149, 19942730250851363, 18350208408879280, 12324506914914625, 27102085920647667, 28009467377098228, 19348565858364802, 19942730250851363, 8479118201845191, 28009467377098228, 27102085920647667, 19348565858364802, 8302426957980714, 19270259444554612, 19942730250851363, 8302426957980714, 13211641791567831, 25824199538612172, 19942730250851363, 8097851867855643, 20436916271957116, 3910629358746840, 18133059900110149]

Enter n from public key (e,n):  28794290241716387

Enter private key d:  23697955405914833

Decrypted message: 'Every Fall, Orion points the way,'
 
Perform another action? (y/n):  n


Bye!




