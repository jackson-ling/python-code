#插入排序
li=[9,5,6,4,3]
n=len(li)
for i in range(1,n):
    value=li[i]
    index=0
    for j in range(i-1,-1,-1):
        if li[j]>value:
            li[j+1]=li[j]
        else:
            index=j+1
            break
    li[index]=value
print(li)


def partition(a,left,right):
    index=left+1 #基准值后面的那个位置
    for i in range(left+1,right+1):
        if li[i]<=li[left]:
            li[i],li[index]=li[index],li[i]
            index+=1
    li[left],li[index-1]=li[index-1],li[left]
    return index-1  #易错：别忘记返回基准值的位置，不同于上面，上面是放在基准值之后的位置索引

def quicksort(a,left,right):
    if left<right:
        mid=partition(a,left,right)
        quicksort(a,left,mid-1)
        quicksort(a,mid+1,right)

print(li)
li.sort(reverse=True)
print(li)