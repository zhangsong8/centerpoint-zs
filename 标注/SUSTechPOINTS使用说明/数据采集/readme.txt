数据采集需要三部分：
1.点云数据：4个激光融合的pcd点云数据，点x,y,z分别是激光坐标系下的值。（pcd格式）
2.前后左右四个相机采集的图片数据（jpg格式）（每帧点云和图像的命名要一样）
3.从三个相机坐标系到激光雷达坐标系的标定数据，每个标定数据包含内参和外参两个旋转矩阵，内参大小是3*3，外参大小是4*4.

组织形式案例可以参考example文件夹
## Data preparation

````
   +- data
       +- scene1
          +- lidar
               +- 0000.pcd
               +- 0001.pcd
          +- camera
               +- front
                    +- 0000.jpg
                    +- 0001.jpg
               +- left
                    +- ...
               +- right
                    +- ...
          +- calib
               +- camera
                    +- front.json
                    +- left.json
                    +- right.json
          +- label          
               +- 0000.json
               +- 0001.json
       +- scene2

````
