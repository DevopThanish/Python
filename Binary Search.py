def Binary_Search(lst,ele):
    first=0
    last=len(lst)-1
    found=False
    while(first<=last)and(not found):
        mid=(first+last)//2
        if lst[mid]==ele:
            print("The element is found at: ",mid)
            found=True
            break
        else:
            if ele<lst[mid]:
                last=mid-1
            else:
                first=mid+1
    if(found!=True):
        print("The element not found")

lst=[12,14,16,17,18,19,20,22,44]
Binary_Search(lst,14)
