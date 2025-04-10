name = '泽言'
age = 25
zhiye = 'python讲师'
age2 = 14

# f    底层会直接强转
print(f'名字:{name},年龄:{age},职业:{zhiye}')

# format
print('名字:{},年龄:{},职业:{}'.format(name, age, zhiye))  # 在format里面{}定要等于后面参数的数量

# %s
print('名字:%s,年龄:%s,职业:%s' % (name, age, zhiye))

