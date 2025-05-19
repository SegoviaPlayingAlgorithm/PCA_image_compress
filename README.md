数学原理和代码的对应关系：
![微信图片_20250517171403](https://github.com/user-attachments/assets/262a1e4d-9e8e-4f84-8b14-2394a3253962)

PCA低纬度重构的效果：

![屏幕截图 2025-05-17 154755](https://github.com/user-attachments/assets/bb924a26-937b-4427-952f-d391566bf416)

原图片
![高分辨](https://github.com/user-attachments/assets/71041956-4c28-482d-92c1-1ea3d85f011a)

重构向量没有修正分布：
意思是，PCA会归一化X之后，重构X，因为归一化，每一列色彩的分布被改变了，如下图所示，和原图像相比丢失了色彩分布的信息
![PCA输出（未考虑主成分）](https://github.com/user-attachments/assets/ed9b35ee-1f27-43c5-8a06-190d37b4b23b)

修正分布：
把X每一列的均值记录下来加到重构的X上，色彩的分布就被重现了
![PCA(考虑主成分)](https://github.com/user-attachments/assets/64093b70-4d34-4185-a263-d9e9cf67c5ae)

PCA什么时候做归一化？分类任务中，一般认为不同色彩同一形状是相同物体，归一化图像，使得数据分布在0附近，以sigmoid函数为例，不容易
发生梯度消失，当你只是想要压缩图片不进行下游处理任务，其实不用归一化
