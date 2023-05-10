# centerpoint-zs
此代码是centerpoint 3D目标检测算法整套pipeline，包含标注、训练等。
# 一、CenterPoint-master_zs
1.det3d/datasets/nuscenes文件夹是根据原作者det3d/datasets/nuscenes_bak代码,再结合自己标注的数据形式，适配修改了一下的。
2.det3d/datasets/pipelines文件夹是根据原作者det3d/datasets/pipelines_bak代码,再结合自己标注的数据形式，适配修改了一下的。
3.configs/nusc/pp/nusc_centerpoint_pp_02voxel_two_pfn_10sweep_zs.py   是根据自己数据类别适配的，这里只有车辆、行人两类。
4.训练自己的数据集就运行python tools/train_zs.py命令

# 二、data
data文件夹中保存的是训练数据，其中lidar文件夹是激光雷达传感器采集的点云，label是标注的标签。

# 三、标注
这个文件存放了标注软件的使用以及标注规范。


