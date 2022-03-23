def multiplier(pListNums:list):
    nResult = 1
    for n in pListNums:
        nResult*=n
    #for
    return nResult
#def multiplier
 
if (__name__=="__main__"):
    listMyNums = [1,2,3]
    theResult = multiplier(listMyNums)
    print (f"O resultado é {nResult}\n")