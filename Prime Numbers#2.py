def gcf(): #defines function that computes the Greatest Common Factor
    global number, number2, gcf #sets variables as global
    number = int(input("Enter a number: ")) #allows user to enter number
    number2 = int(input("Enter another number: ")) #allows user to enter another number
    prime_n = [] #creates empty list 
    prime_n2 = [] #creates empty list 

    for i in range(1, number+1): #loops from 1 to the first number inputted plus one
        if(number % i == 0): #if first number is divisible by i then i is added to empty list prime_n
            prime_n.append(i)
            i+=1
        else: #otherwise i is incremented 
            i+=1

    for i in range(1, number2+1): #loops from 1 to the second number inputted plus one
        if(number2 % i == 0): #if second number is divisible by i then i is added to second empty list prime_n2
            prime_n2.append(i)
            i+=1
        else: #otherwise for loop checks to see if number is divisible by next number in range
            i+=1

    gcf = [] #Creates empty list for common factors
    for i in range(len(prime_n)): #loops through the first list of prime numbers
        for j in range(len(prime_n2)): #loops through the second list of prime numbers 
            if prime_n[i] == prime_n2[j]: #if a number in the first list is the same as a number in the second list, the number is added to list gcf 
                gcf.append(prime_n2[j]) 
                i+=1 #i is incremented 
                j+=1 #j is incremented
                break #program breaks out of for loop 
            else: #otherwise only index in second list is incremented 
                j+=1
    

    print("The greatest common factor is", max(gcf)) #The largest number in the list gcf is returned in print statement 


def lcm(): #Function computes the Least Common Multiple
    gcf() #Calls the gcf function 
    lcm = int((number / max(gcf) * number2)) #Computes the Least Common Multiple from the Greatest Common Factor 
    print("The least common multiple is", lcm) #Prints the Least Common Multiple 

lcm() #Calls the lcm function 
    
