def bubblesort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i]=alist[i+1]
                alist [i+1] = temp
            else:
                pass
        def stop(blist):

            sorted = False
            length = len(blist) - 1

            while not sorted:
                sorted = True
                for i in range(0,length):
                    if blist[i] > blist [i + 1]:
                        sorted = False
                        blist[i], blist [i+1] = blist[i+1],blist[i]

alist =[1,2,3,4,5]
bubblesort(alist)
print(alist)