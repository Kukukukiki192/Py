import pandas as pd
import calmap
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('temp_data.csv', parse_dates=['date'])
data.set_index('date', inplace=True)

# 生成日历图
plt.figure(figsize=(20, 8))
calmap.calendarplot(data['temperature'],
                    cmap='coolwarm',  # 使用冷暖色调
                    fillcolor='white',
                    linewidth=0,
                    daylabels='MTWTFSS',
                    dayticks=[0, 2, 4, 6],
                    yearlabel_kws={'color': 'black', 'fontsize': 16})

plt.show()

# 保存为PNG文件
# plt.savefig('temperature_calendar.png', dpi=300, bbox_inches='tight')
# plt.close()  # 关闭图像