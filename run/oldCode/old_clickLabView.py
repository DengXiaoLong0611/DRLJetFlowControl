import pyautogui
import shutil
import os
import time
def clickLabView():
    print("开始启动抓取服务")
    pyautogui.sleep(5)

    first = True
    while True:
        ########################### 3
        pyautogui.sleep(5)
        if first:
            first =False
        else:
            #拷贝 文件到预定目录 拷贝的路径src_file  拷贝道的路径dst_dir
            src_file = r'C:\qianghuafile\ForceCollection\1.csv'
            dst_dir = r'C:\qianghuafile\res'
            ###当前时间
            timestamp = int(time.time())
            dst_file = f"file_{timestamp}.csv"
            shutil.copy2(src_file, os.path.join(dst_dir, dst_file))

        pyautogui.click(x=710,y=848)
        x, y = pyautogui.position()
        print(f"当前鼠标坐标为：{x}, {y}")
clickLabView()