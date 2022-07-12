# author:zhangmeng  email:mrzhangm@126.com
# 2022年07月12日23时03分08秒
import numpy as np
import matplotlib.pyplot as plt

uk_file_path='./youtube_video_data/GB_video_data_numbers.csv'
t_uk=np.loadtxt(uk_file_path,delimiter=',',dtype=int)
t_uk=t_uk[t_uk[:,1]<=500000]
t_uk_comment=t_uk[:,-1]
t_uk_like=t_uk[:,1]
plt.figure(figsize=(20,8),dpi=80)
plt.scatter(t_uk_like,t_uk_comment)
plt.show()