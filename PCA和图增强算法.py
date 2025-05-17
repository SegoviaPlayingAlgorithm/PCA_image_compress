import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
'''
trans(源图片地址,PCA降维后存储到目标地址,希望降到k维)你们用这个就行
trans基于PCA和pca_channel实现
PCA实现了对多通道分别进行主成分分析，pca_channel是对一个通道的矩阵做主成分分析
'''
def PCA(imgarr,k):#截取最大k个特征值
    if(imgarr.shape[0]<k):#k不能超过行数n，因为X*X.T是n维，就n个特征向量
        print("错误，特征不能比行数还多")
        return np.zeros_like(imgarr)
    
    n_chan=imgarr.shape[2] #获取通道数
    img_out=np.zeros_like(imgarr,dtype=np.int8) #255，8位够用
    for i in range(n_chan): #每个通道分别做PCA压缩
        img_out[:,:,i]=pca_channel(imgarr[:,:,i],k)
    return img_out

def pca_channel(img_chan,k):
    X=np.float64(img_chan)
    m=len(X)
    W=np.zeros([m,k])
    for i in range(img_chan.shape[1]):#列数
        xmean=np.mean(img_chan[:,i])
        X[:,i]-=xmean #用到了广播机制
    cov=np.dot(X,X.T)#协方差
    val,vec=np.linalg.eig(cov)
    item={}
    for i in range(len(val)):
        item[i]=[val[i],vec[i]]#W[i]是一维np数组，是个行向量，而且没法转置
    sort_by_val=sorted(item.items(),key=lambda x:x[1][0],reverse=True)#选择字典值，第0的分量即特征值做排序主键，降序排列
    for rank,big in enumerate(sort_by_val):#排名，特征
        if(rank>k-1): break #处理k个特征
        W[:,rank]=(big[1][1])#W是特征向量按照特征值从大到小排列
    return np.dot(np.dot(W,W.T),X)

def trans(file,filesave,k):
    # 在这里写入图片的路径"C:\\Users\\15694\\Pictures\\图片\\高分辨.jpg"
    image = Image.open(file)
    plt.subplot(1,2,1)
    plt.imshow(image)
    # 将图片转换为NumPy数组
    image_np = np.array(image)
 
    print("您选择的图片规格为"+str(image_np.shape))
    #降到100维
    small=PCA(image_np,k)
    image=Image.fromarray(np.uint8(small))#强制转换像素值0~255
    plt.subplot(1,2,2)
    plt.imshow(image)
    plt.show()
    image.save(filesave)
trans("高分辨.jpg","图片主成分.jpg",800)

