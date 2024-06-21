#    numpy    
##    基本操作    
np.reshape(m,n)      
np.shape    
np.ndim    维度    
np.dtype.name    'int64'    
np.itemsize    '8'返回的是该类型所需字节数    
np.size    
np.arange(start,end,step)    
np.linespace(start,end,num)    也是生成等差数列，num为其中个数，
np.zeros()
np.ones()
np.empty()
```
为什么np.empty()要选择随机数,而不是全部放0呢，随机生成不是会更耗时吗？  
1.np.empty()的随机数不是通过随机生成的，而是内存中存在的数据，就是分配内存并返回内存中的数据，因此看起来是随机数，但是过程不涉及随机数的开销。  
2.np.empty()中元素不需要进行初始化，np.zeros()元素需要初始化，因此np.enpty()会比np.zeros()速度快  
```
```
>>> A = np.array( [[1,1],
...             [0,1]] )
>>> B = np.array( [[2,0],
...             [3,4]] )
>>> A * B                       # elementwise product
array([[2, 0],
       [0, 4]])
>>> A @ B                       # matrix product
array([[5, 4],
       [3, 4]])
>>> A.dot(B)                    # another matrix product
array([[5, 4],
       [3, 4]])
```
np.exp(num)    返回的是e的num次方    
axis = 0    列    
axix = 1    行    
A.flat    flat是数组所有元素的迭代器
```
for element in b.flat:
...     print(element)
```
A.ravel()    压缩flatten至一维    
A.flatten()
```
ravel大多返回视图，flatten只能返回副本    
视图即对视图进行修改后，原数组也会发生变化    
副本即修改后，原数组不会发生变化
```
A.T()    转置transposed    
###    数组堆叠
```
>>> a = np.floor(10*np.random.random((2,2)))
>>> a
array([[ 8.,  8.],
       [ 0.,  0.]])
>>> b = np.floor(10*np.random.random((2,2)))
>>> b
array([[ 1.,  8.],
       [ 0.,  4.]])
>>> np.vstack((a,b))
array([[ 8.,  8.],
       [ 0.,  0.],
       [ 1.,  8.],
       [ 0.,  4.]])
>>> np.hstack((a,b))
array([[ 8.,  8.,  1.,  8.],
       [ 0.,  0.,  0.,  4.]])
```

