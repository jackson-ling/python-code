# 插入排序
li=[9,5,8,6,2,1]
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

# 快速排序
def partition(a,left,right):
    index=left+1
    for i in range(left+1,right+1):
        if li[i]<=li[left]:
            li[i],li[index]=li[index],li[i]
            index+=1
    li[left],li[index-1]=li[index-1],li[left]
    return index-1

def quicksort(a,left,right):
    if left<=right:
        mid=partition(a,left,right)# 这里是调用第一个函数，找出中间那个数，之后分两半使用递归求解
        quicksort(a,left,mid-1)
        quicksort(a,mid+1,right)

print(li)

