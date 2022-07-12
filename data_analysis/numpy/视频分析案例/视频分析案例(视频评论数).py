# author:zhangmeng  email:mrzhangm@126.com
# 2022年07月12日23时00分23秒
import numpy as np
import matplotlib.pyplot as plt

us_file_path='./youtube_video_data/US_video_data_numbers.csv'
t_us=np.loadtxt(us_file_path,delimiter=',',dtype='int')
t_us_comments=t_us[:,-1]
t_us_comments=t_us_comments[t_us_comments<=5000]
d=100
bin_nums=(t_us_comments.max()-t_us_comments.min())//d
plt.figure(figsize=(20,8),dpi=80)
plt.hist(t_us_comments,bin_nums)
plt.show()
