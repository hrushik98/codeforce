number = int(input())
 
for i in range(number+1, 10000):
    
    
    x = 0
    for m in range(0, len(str(i))):
        k = str(i)[m]
        
        for b in range(0, len(str(number))):
            if k == str(i)[b]:
                x = x+1
                
                
    if x == 4:
        print(i)
        break
    

            