import pandas as pd
import plotly.express as px

# 读取数据
data = pd.read_csv('temp_data.csv', parse_dates=['date'])
data.set_index('date', inplace=True)

# 准备数据用于绘制日历图
data = data.reset_index()
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['day'] = data['date'].dt.day

# 创建一个新的列，用于显示悬停信息
data['hover_text'] = data['date'].dt.strftime('%Y-%m-%d') + '<br>Temperature: ' + data['temperature'].astype(str)

# 绘制日历图
fig = px.density_heatmap(
    data,
    x='day',
    y='month',
    z='temperature',
    text_auto=True,
    hover_name='hover_text',
    title='Temperature Calendar Heatmap',
    labels={'day': 'Day', 'month': 'Month'},
    color_continuous_scale='RdBu_r'
)

fig.update_layout(
    yaxis={'categoryorder': 'category ascending'},
    xaxis_title='Day of Month',
    yaxis_title='Month'
)

# 显示图表
fig.show()

# 保存图表为HTML文件
# fig.write_html('temp_cal.html')