import requests
import csv
from datetime import datetime, timedelta

# OpenWeatherMap API Key
api_key = 'VQHQF49R3ZADVKS9CD63FX3K6'

# 城市和时间范围设置
city_name = 'Hangzhou'
start_date = '2024-05-17'
end_date = '2024-07-19'

# 转换日期格式
start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.strptime(end_date, '%Y-%m-%d')

# 准备 CSV 文件
csv_file = open('hangzhou_weather.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Date', 'High (°C)', 'Low (°C)'])

# 获取每天的天气数据
date = start_date
while date <= end_date:
    timestamp = int(date.timestamp())
    url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=30.2741&lon=120.1551&dt={timestamp}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    # 检查请求是否成功
    if response.status_code == 200 and 'hourly' in data:
        # 获取最高温和最低温
        temps = [hour['temp'] for hour in data['hourly']]
        high_temp = max(temps)
        low_temp = min(temps)
        
        # 写入 CSV 文件
        csv_writer.writerow([date.strftime('%Y-%m-%d'), high_temp, low_temp])
    else:
        print(f"Failed to retrieve data for {date.strftime('%Y-%m-%d')} - Status Code: {response.status_code}")
    
    # 下一天
    date += timedelta(days=1)

csv_file.close()
