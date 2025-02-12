import os
import shutil
import webbrowser
import customtkinter as ctk
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkFrame
import json
from CTkMessagebox import CTkMessagebox  # 确保导入 CTkMessagebox
import base64

# 作者名称
AUTHOR_NAME = "安尘,WWNNL"

# base64 图标数据留空
icon_data = "AAABAAEAQEAAAAEAIAAoQgAAFgAAACgAAABAAAAAgAAAAAEAIAAAAAAAAAAAAMQOAADEDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABlkf+AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Blkf+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZpH+cGaR//9mkf//YoXm/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/YoXm/2aR//9mkf//ZpH+cAAAAAAAAAAAAAAAAAAAAAAAAAAAZI/90GaR//9HPUv/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/Rz1L/2aR//9kj/3QAAAAAAAAAAAAAAAAZo//UGaR//9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/ZpH//2aP/1AAAAAAAAAAAGaR//9KQ1j/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0pDWP9mkf//AAAAAAAAAABmkf//QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/ZpH//wAAAABmkf5wZIvz/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/2SL8/9mkf5wZo//wFdnpf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/zoqKv82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/86Kir/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9ZbbL/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/OCkp/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/84KSn/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zsrK/82Jyf/Nicn/zYnJ/82Jyf/Nicn/z87UP9CQl3/QkJd/0JCXf9CQl3/QkJd/0JCXf9CQl3/QkJd/0JCXf9CQl3/QkJd/0JCXf9CQl3/QkJd/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/87Kyv/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/OS41/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Y4vy/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9Uaq//Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0JCXf9OXJP/VGqv/0tWhv82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/85LjX/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9RY6H/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//WnfK/2CE5f9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Y4vy/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//z87UP82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//0VIa/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9dfdf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/zYnJ/9FSGv/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//PztQ/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//zkuNf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/1Rqr/9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9OXJP/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//0hPeP82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/V3C8/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/1dwvP9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//QkJd/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/1p3yv9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//05ck/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9dfdf/ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9OXJP/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9FSGv/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//PDRC/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/WnfK/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9ji/L/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/OS41/2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0JCXf9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2OL8v82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//1191/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/OS41/2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Y4vy/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//1191/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2CE5f8/O1D/Nicn/zYnJ/9IT3j/XX3X/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9IT3j/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2OL8v82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2CE5f9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2OL8v9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//88NEL/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Y4vy/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PDRC/2OL8v9mkf//ZpH//2aR//9mkf//YITl/05ck/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/WnfK/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zkuNf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9IT3j/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//YITl/zkuNf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PztQ/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9Uaq//Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PDRC/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2CE5f82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/WnfK/2aR//9mkf//ZpH//2aR//9mkf//ZpH//0hPeP82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9FSGv/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9ad8r/UWOh/2OL8v9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9Uaq//Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//1Fjof88NEL/Nicn/zYnJ/82Jyf/VGqv/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/85LjX/Y4vy/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/VGqv/2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//SE94/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9ghOX/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//1Rqr/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/z87UP9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9CQl3/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9OXJP/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9ad8r/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/TlyT/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//WnfK/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/0JCXf9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//85LjX/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Y4vy/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//XX3X/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/85LjX/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//1Fjof82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/TlyT/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9FSGv/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//XX3X/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PztQ/2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zkuNf9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2OL8v8/O1D/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9ji/L/OS41/zYnJ/82Jyf/Nicn/zYnJ/88NEL/VGqv/2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/OS41/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//1p3yv82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9FSGv/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2OL8v82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PztQ/0hPeP9CQl3/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9OXJP/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/1p3yv9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf88Kyv/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PCsr/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf87Kyv/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zsrK/9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGWP/bBbc7//QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf89LS3/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/PS0t/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/W3O//2WP/bBkkv9gZpH//0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/2aR//9kkv9gAAAAAGaR//9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9mkf//AAAAAAAAAABmkf//Tk9y/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9OT3L/ZpH//wAAAAAAAAAAZI//MGaR//9FNz7/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9FNz7/ZpH//2SP/zAAAAAAAAAAAAAAAABmkf2QZpH//1BVf/9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9QVX//ZpH//2aR/ZAAAAAAAAAAAAAAAAAAAAAAAAAAAGSP/zBmkf//ZpH//2aR//9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/2aR//9mkf//ZpH//2SP/zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABnj/9AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Bnj/9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////wAAAAAAAAD+AAAAAAAAAHwAAAAAAAAAOAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABwAAAAAAAAAPgAAAAAAAAB/AAAAAAAAAP//////////8="  # 留空，后续自行填充

# 设置外观模式和默认颜色主题
ctk.set_appearance_mode("Dark")  # 设置为 Dark 模式
ctk.set_default_color_theme("dark-blue")  # 设置为 dark-blue 主题

# 获取用户的PixelComposer路径
def get_user_path():
    return os.path.join(os.path.expanduser("~"), "AppData", "Local", "PixelComposer")

# 获取用户的PixelComposer Locale路径
def get_user_locale_path():
    return os.path.join(get_user_path(), "Locale")

# 获取用户的Preferences路径
def get_preferences_path():
    return os.path.join(get_user_path(), "Preferences", "1171")

# 修改keys.json文件中的local字段
def modify_keys_json(locale="zh"):
    keys_path = os.path.join(get_preferences_path(), "keys.json")
    try:
        with open(keys_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if data.get("local") != locale:
            data["local"] = locale
            with open(keys_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            CTkMessagebox(
                title="成功", 
                message=f"汉化完成！已成功修改语言设置为 {locale}", 
                icon="check",
                button_color="#FF9166",  # 设置按钮颜色
                button_hover_color="#FF9166",  # 设置按钮悬停颜色
                font=("Microsoft YaHei", 14, "bold")
            )
            return True
        else:
            CTkMessagebox(
                title="成功", 
                message="汉化完成！但语言设置无需修改", 
                icon="check",
                button_color="#FF9166",
                button_hover_color="#FF9166",
                font=("Microsoft YaHei", 14, "bold")
            )
            return False
    except FileNotFoundError:
        CTkMessagebox(
            title="错误", 
            message=f"未找到keys.json文件：{keys_path}", 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )
        return False
    except json.JSONDecodeError:
        CTkMessagebox(
            title="错误", 
            message="JSON文件格式错误，请检查文件内容", 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )
        return False
    except PermissionError:
        CTkMessagebox(
            title="错误", 
            message="没有文件写入权限，请用管理员权限运行", 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )
        return False
    except Exception as e:
        CTkMessagebox(
            title="未知错误", 
            message=str(e), 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )
        return False

# 复制汉化文件夹
def copy_localization_folder(locale="zh"):
    locale_path = get_user_locale_path()
    en_folder = os.path.join(locale_path, 'en')
    target_folder = os.path.join(locale_path, locale)

    if not os.path.exists(locale_path):
        CTkMessagebox(
            title="错误", 
            message="请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)", 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )
        return

    if not os.path.exists(en_folder):
        CTkMessagebox(
            title="错误", 
            message="请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)", 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )
        return

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    source_folder = os.path.join(os.getcwd(), locale)

    if not os.path.exists(source_folder):
        CTkMessagebox(
            title="错误", 
            message=f"汉化文件夹 '{locale}' 未找到，请确保它在工具同目录下！", 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )
        return

    try:
        shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
        modify_keys_json(locale)
    except Exception as e:
        CTkMessagebox(
            title="错误", 
            message=f"汉化过程中出现错误：{e}", 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )

# 递归删除文件夹内文件
def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)
            shutil.rmtree(path_file)

# 复制教程文件夹
def copy_tutorial_folder():
    lib_path = get_user_path()
    welcome_files_folder = os.path.join(lib_path, 'Welcome files')
    
    if not os.path.exists(lib_path):
        CTkMessagebox(
            title="错误", 
            message="请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)", 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )
        return

    if not os.path.exists(welcome_files_folder):
        CTkMessagebox(
            title="错误", 
            message="请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)", 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )
        return

    del_file(welcome_files_folder)

    source_folder = os.path.join(os.getcwd(), 'Welcome files')

    if not os.path.exists(source_folder):
        CTkMessagebox(
            title="错误", 
            message="汉化教程文件夹 'Welcome files' 未找到，请确保它在工具同目录下！", 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )
        return

    try:
        shutil.copytree(source_folder, welcome_files_folder, dirs_exist_ok=True)
        CTkMessagebox(
            title="成功", 
            message="教程汉化完成！", 
            icon="check",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )
    except Exception as e:
        CTkMessagebox(
            title="错误", 
            message=f"教程汉化过程中出现错误：{e}", 
            icon="cancel",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
        )

# 打开浏览器进入特效交流群
def open_communication_group():
    url = "https://qm.qq.com/q/Vu9GTC4mw8"
    webbrowser.open(url)

# 创建主窗口
root = CTk()
root.title("PixelComposer 汉化工具")

# 设置窗口居中
def center_window(width=500, height=230):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (width / 2))
    y_cordinate = int((screen_height / 2) - (height / 2))
    root.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")

center_window()  # 调用窗口居中函数

# 设置窗口图标
try:
    if icon_data:
        icon_bytes = base64.b64decode(icon_data)
        with open('temp.ico', 'wb') as f:
            f.write(icon_bytes)
        root.iconbitmap('temp.ico')
        os.remove('temp.ico')
except Exception as e:
    print(f"设置图标时出现错误: {e}")

# 添加标题标签
title_label = CTkLabel(root, text="PixelComposer 汉化工具", font=("Microsoft YaHei", 28, "bold"))
title_label.pack(pady=10)

# 创建输入框框架
input_frame = CTkFrame(root)
input_frame.pack(pady=5)

# 创建输入框和标签
locale_var = ctk.StringVar(value="zh")
locale_label = CTkLabel(input_frame, text="输入汉化名（默认为zh）:", font=("Microsoft YaHei", 16))
locale_label.pack(side=ctk.LEFT, padx=5)
locale_entry = CTkEntry(input_frame, textvariable=locale_var, width=100, font=("Microsoft YaHei", 16, "bold"), text_color="#FF9166")
locale_entry.pack(side=ctk.LEFT, padx=5)

# 创建按钮框架
button_frame = CTkFrame(root)
button_frame.pack(pady=5)

# 创建一键汉化按钮
def on_localize_button_click():
    locale = locale_var.get().strip() or "zh"
    copy_localization_folder(locale)

localize_button = CTkButton(button_frame, text="一键汉化软件", command=on_localize_button_click, width=150, font=("Microsoft YaHei", 14, "bold"), text_color="#191925", fg_color="#FF9166", hover_color="#FF9166")
localize_button.pack(side=ctk.LEFT, padx=5)

# 创建一键汉化教程按钮
tutorial_button = CTkButton(button_frame, text="一键汉化教程", command=copy_tutorial_folder, width=150, font=("Microsoft YaHei", 14, "bold"), text_color="#191925", fg_color="#FF9166", hover_color="#FF9166")
tutorial_button.pack(side=ctk.LEFT, padx=5)

# 创建一个空的Frame来作为新的一行
empty_frame = CTkFrame(root)
empty_frame.pack(pady=5)

# 创建加入交流群按钮
group_button = CTkButton(empty_frame, text="加入特效交流群", command=open_communication_group, width=150, font=("Microsoft YaHei", 14, "bold"), text_color="#191925", fg_color="#FF9166", hover_color="#FF9166")
group_button.pack(pady=5)

# 添加作者名称标签
author_label = CTkLabel(root, text=f"作者:{AUTHOR_NAME}", font=("Microsoft YaHei", 16))
author_label.pack(pady=5)

# 显示初始提示
CTkMessagebox(
        title="注意", 
        message="请在PixelComposer第一次运行后使用，请保证汉化文件夹与本程序在同一目录", 
        icon="info",
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
)

# 运行主循环
root.mainloop()