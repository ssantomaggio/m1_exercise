#scrivere un programma in cui si fanno inserire dei valori all utnte e appena 
#inserisce lo 0 si calcola la media dei valori inseriti
numbers=[]
while 0 not in numbers:
    number=int(input("inserisci un valore diverso da 0:"))
    if number==0 and len(numbers)==0:
        print ("error")
    elif number ==0:
       average= sum(numbers)/len(numbers)
       print ("The average is:", average)
    numbers.append(number)
    
