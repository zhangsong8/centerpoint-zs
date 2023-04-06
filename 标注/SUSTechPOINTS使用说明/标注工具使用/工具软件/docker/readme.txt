1.docker load -i sustechpoints.tar
2.${YourDataPath}为你存放的数据文件路径
sudo docker run -it -d --restart=always --name STPointsSServer -p 8081:8081 -v ${YourDataPath}:/root/SUSTechPOINTS/data sustechpoints:v1.0.0 bash
3.启动程序：python main,py，根据提示在网页上打开http:://0.0.0.0:8081就可以使用软件了



