def sdvig_4(list, i=1,):
    if i>4:
        return list

    p=len(list)-2
    x=list[-1]
    list[-1]=""
    while p>=0:
        list[p+1]=list[p]
        p-=1
    list[0]=x

    return sdvig_4(list,i+1)

list=[1,2,3,4,5]
print("Ваш массив: ", list, sep="\n")
print("\n")
sdvig_4(list)
print("Ваш массив со сдвигом: ", list, sep="\n")
