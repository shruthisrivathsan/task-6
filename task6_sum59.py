#initialise 3 variables num_list containing list, n containing lenght of list and total containing sum.

num_list = [10,20,30,9]
n=len(num_list)
total = 59

#define function called findtriplet containing the arguments num_list, n and total
def findtriplet(num_list, n, total):
    #iterate variable i in range n-2
    for i in range(0,n-2):
        #iterate variable j in range n-1
        for j in range (i+1,n-1):
            #iterate variable k in range n
            for k in range(j+1 , n):
                #check if sum of 3 variables is equal to the total
                if num_list[i]+ num_list[j]+ num_list[k]==total:
                    print("Triplet is",num_list[i],",",num_list[j],",", num_list[k])
                    return True
#call function
findtriplet(num_list, n, total)
