'''
思想：找到一个基准值（假设是数组第一个元素），从基准值后面的那一个数开始遍历，
小于基准值放到前面（当前遍历元素和基准值后面的那个元素交换位置），大于的放到后面（不动）
之后把小于基准值的最后一个元素和基准值调换位置，这样就实现了
（小于基准值的数）基准值（大于基准值的数），这样就把一个大的问题拆分成子问题
之后对左右两边使用递归就可以了
'''
# 说明：左端点为left，右端点为right

def partition(a,left,right):# 我们认为a[left]就是基准值（也就是第一个元素）
    #首先记录需要放到基准值后面位置的下标(小于基准值就放到基准值的后面)
    index=left+1
    #先遍历元素，进行比较
    for i in range(left+1,right+1):#左闭右开，这里的值都是数组下标
        if a[i]<=a[left]:  #注意有等于
            a[i],a[index]=a[index],a[i]
            index+=1 # 交换一次，就得往后挪一个位置

    # 现在执行和基准值交换位置，实现分成三部分

    # 因为小于基准值的数放到前面来之后，index就会+1，现在index-1就是最后一个基准值的位置
    a[left],a[index-1]=a[index-1],a[left]
    return index-1 #返回基准值最终所在的位置

def quicksort(a,left,right):
    if left<=right:
        mid=partition(a,left,right)
        quicksort(a,left,mid-1)
        quicksort(a,mid+1,right)

li=[1,9,5,6,3]
quicksort(li,0,4)
print(li)