import os
import shutil
import webbrowser
import tkinter as tk
from tkinter import messagebox
import base64
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# 作者名称
AUTHOR_NAME = "安尘,WWNNL"

# 将提供的 base64 字符串提取为纯编码部分
icon_data = "AAABAAEAQEAAAAEAIAAoQgAAFgAAACgAAABAAAAAgAAAAAEAIAAAAAAAAAAAAMQOAADEDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABlkf+AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Bmj//AZo//wGaP/8Blkf+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZpH+cGaR//9mkf//YoXm/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/VWGY/1VhmP9VYZj/YoXm/2aR//9mkf//ZpH+cAAAAAAAAAAAAAAAAAAAAAAAAAAAZI/90GaR//9HPUv/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/Rz1L/2aR//9kj/3QAAAAAAAAAAAAAAAAZo//UGaR//9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/ZpH//2aP/1AAAAAAAAAAAGaR//9KQ1j/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0pDWP9mkf//AAAAAAAAAABmkf//QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/ZpH//wAAAABmkf5wZIvz/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/2SL8/9mkf5wZo//wFdnpf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/zoqKv82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/86Kir/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9ZbbL/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/OCkp/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/84KSn/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zsrK/82Jyf/Nicn/zYnJ/82Jyf/Nicn/z87UP9CQl3/QkJd/0JCXf9CQl3/QkJd/0JCXf9CQl3/QkJd/0JCXf9CQl3/QkJd/0JCXf9CQl3/QkJd/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/87Kyv/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/OS41/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Y4vy/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9Uaq//Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0JCXf9OXJP/VGqv/0tWhv82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/85LjX/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9RY6H/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//WnfK/2CE5f9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Y4vy/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//z87UP82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//0VIa/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9dfdf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/zYnJ/9FSGv/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//PztQ/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//zkuNf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/1Rqr/9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9OXJP/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//0hPeP82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/V3C8/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/1dwvP9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//QkJd/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/1p3yv9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//05ck/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9dfdf/ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9OXJP/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9FSGv/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//PDRC/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/WnfK/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9ji/L/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/OS41/2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0JCXf9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2OL8v82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//1191/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/OS41/2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Y4vy/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//1191/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2CE5f8/O1D/Nicn/zYnJ/9IT3j/XX3X/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9IT3j/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2OL8v82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2CE5f9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2OL8v9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//88NEL/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Y4vy/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PDRC/2OL8v9mkf//ZpH//2aR//9mkf//YITl/05ck/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/WnfK/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zkuNf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9IT3j/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//YITl/zkuNf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PztQ/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9Uaq//Nicn/zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PDRC/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2CE5f82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/WnfK/2aR//9mkf//ZpH//2aR//9mkf//ZpH//0hPeP82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9FSGv/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9ad8r/UWOh/2OL8v9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9Uaq//Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//1Fjof88NEL/Nicn/zYnJ/82Jyf/VGqv/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/85LjX/Y4vy/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/VGqv/2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//SE94/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9ghOX/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//1Rqr/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/z87UP9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9CQl3/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9OXJP/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9ad8r/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/TlyT/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//WnfK/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/0JCXf9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//85LjX/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Y4vy/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//XX3X/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/85LjX/ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//1Fjof82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/TlyT/2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9FSGv/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//XX3X/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PztQ/2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zkuNf9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2OL8v8/O1D/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9mkf//ZpH//2aR//9mkf//ZpH//2aR//9ji/L/OS41/zYnJ/82Jyf/Nicn/zYnJ/88NEL/VGqv/2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/OS41/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//1p3yv82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9FSGv/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2OL8v82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PztQ/0hPeP9CQl3/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/9OXJP/ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/1p3yv9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//2aR//9mkf//ZpH//zYnJ/82Jyf/Nicn/zYnJ/82Jyf/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGaP/8BVYZj/QzEx/0MxMf9DMTH/QzEx/0MxMf88Kyv/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/PCsr/0MxMf9DMTH/QzEx/0MxMf9DMTH/VWGY/2aP/8Bmj//AVWGY/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/1VhmP9mj//AZo//wFVhmP9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf87Kyv/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zYnJ/82Jyf/Nicn/zsrK/9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9VYZj/Zo//wGWP/bBbc7//QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf89LS3/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/OSkp/zkpKf85KSn/PS0t/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/W3O//2WP/bBkkv9gZpH//0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/2aR//9kkv9gAAAAAGaR//9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9mkf//AAAAAAAAAABmkf//Tk9y/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9OT3L/ZpH//wAAAAAAAAAAZI//MGaR//9FNz7/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9FNz7/ZpH//2SP/zAAAAAAAAAAAAAAAABmkf2QZpH//1BVf/9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9DMTH/QzEx/0MxMf9QVX//ZpH//2aR/ZAAAAAAAAAAAAAAAAAAAAAAAAAAAGSP/zBmkf//ZpH//2aR//9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/115zP9decz/XXnM/2aR//9mkf//ZpH//2SP/zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABnj/9AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Blkf+AZZH/gGWR/4Bnj/9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////wAAAAAAAAD+AAAAAAAAAHwAAAAAAAAAOAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABgAAAAAAAAAGAAAAAAAAAAYAAAAAAAAABwAAAAAAAAAPgAAAAAAAAB/AAAAAAAAAP//////////8="

# 获取用户的PixelComposer路径
def get_user_path():
    # 使用动态路径，适用于所有用户
    return os.path.join(os.path.expanduser("~"), "AppData", "Local", "PixelComposer")

# 获取用户的PixelComposer Locale路径
def get_user_locale_path():
    # 使用动态路径，适用于所有用户
    return os.path.join(os.path.expanduser("~"), "AppData", "Local", "PixelComposer", "Locale")

# 复制汉化文件夹
def copy_localization_folder():
    locale_path = get_user_locale_path()  # 用户的Locale路径
    en_folder = os.path.join(locale_path, 'en')  # 检查en文件夹是否存在
    zh_folder = os.path.join(locale_path, 'zh')  # 目标zh文件夹路径

    # 检查Locale路径是否存在
    if not os.path.exists(locale_path):
        messagebox.showerror("错误", "请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)")
        return

    # 检查en文件夹是否存在
    if not os.path.exists(en_folder):
        messagebox.showerror("错误", "请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)")
        return

    # 检查目标目录zh文件夹是否存在，不存在则创建
    if not os.path.exists(zh_folder):
        os.makedirs(zh_folder)

    source_folder = os.path.join(os.getcwd(), 'zh')  # 汉化文件夹路径

    # 检查源文件夹zh是否存在
    if not os.path.exists(source_folder):
        messagebox.showerror("错误", "汉化文件夹 'zh' 未找到，请确保它在工具同目录下！")
        return

    try:
        # 使用copytree复制整个文件夹，并覆盖已有文件
        shutil.copytree(source_folder, zh_folder, dirs_exist_ok=True)
        messagebox.showinfo("成功", "汉化完成！")
    except Exception as e:
        messagebox.showerror("错误", f"汉化过程中出现错误：{e}")

# 递归删除文件夹内文件
def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path,i)  #取文件绝对路径
        print(path_file)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)
            shutil.rmtree(path_file)

def copy_tutorial_folder():
    lib_path = get_user_path()  # 用户的Locale路径
    Welcome_files_folder = os.path.join(lib_path, 'Welcome files')  # 检查Welcome files文件夹是否存在
    
    # 检查PixelComposer路径是否存在
    if not os.path.exists(lib_path):
        messagebox.showerror("错误", "请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)")
        return

    # 检查源文件夹Welcome files是否存在
    if not os.path.exists(Welcome_files_folder):
        messagebox.showerror("错误", "请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)")
        return

    # 删除目标目录Welcome files文件夹内容
    del_file(Welcome_files_folder)

    source_folder = os.path.join(os.getcwd(), 'Welcome files')  # 汉化文件夹路径

    # 检查源文件夹是否存在
    if not os.path.exists(source_folder):
        messagebox.showerror("错误", "汉化教程文件夹 'Welcome files' 未找到，请确保它在工具同目录下！")
        return

    try:
        # 使用copytree复制整个文件夹，并覆盖已有文件
        shutil.copytree(source_folder, Welcome_files_folder, dirs_exist_ok=True)
        messagebox.showinfo("成功", "教程汉化完成！")
    except Exception as e:
        messagebox.showerror("错误", f"教程汉化过程中出现错误：{e}")

# 打开浏览器进入特效交流群
def open_communication_group():
    url = "https://qm.qq.com/q/Vu9GTC4mw8"  # 修复URL格式
    webbrowser.open(url)

# 创建主窗口
root = ttk.Window(themename="superhero")
root.title("PixelComposer 汉化工具")

# 获取当前脚本的路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 设置窗口居中
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (400 / 2))
y_cordinate = int((screen_height / 2) - (160 / 2) - 80)
root.geometry(f"400x160+{x_cordinate}+{y_cordinate}")

# 设置窗口图标
try:
    icon_bytes = base64.b64decode(icon_data)
    with open('temp.ico', 'wb') as f:
        f.write(icon_bytes)
    root.iconbitmap('temp.ico')
    os.remove('temp.ico')
except Exception as e:
    print(f"设置图标时出现错误: {e}")

# 添加标题标签
title_label = ttk.Label(root, text="PixelComposer 汉化工具", font=("SimHei", 16, "bold"))
title_label.pack(expand=True)

# 创建按钮框架
button_frame = ttk.Frame(root)
button_frame.pack(expand=True)

# 创建一键汉化按钮
localize_button = ttk.Button(button_frame, text="一键汉化软件", command=copy_localization_folder, style="primary.TButton", width=15)
localize_button.pack(side=LEFT, padx=4, pady=1, fill=X, expand=True)

# 创建一键汉化教程按钮
tutorial_button = ttk.Button(button_frame, text="一键汉化教程", command=copy_tutorial_folder, style="primary.TButton", width=15)
tutorial_button.pack(side=LEFT, padx=4, pady=1, fill=X, expand=True)

# 创建一个空的Frame来作为新的一行
empty_frame = ttk.Frame(root)
empty_frame.pack(expand=True)

# 创建加入交流群按钮
group_button = ttk.Button(empty_frame, text="加入特效交流群", command=open_communication_group, style="secondary.TButton", width=15)
group_button.pack(side=LEFT, padx=1, pady=1, fill=X, expand=True)

# 添加作者名称标签
author_label = ttk.Label(root, text=f"作者:{AUTHOR_NAME}", font=("SimHei", 12))
author_label.pack(expand=True)

messagebox.showinfo("注意", "一键汉化工具请在PixelComposer第一次运行后使用，请保证zh和Welcome files文件夹与本程序在同一目录")

# 运行主循环
root.mainloop()