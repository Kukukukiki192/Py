import re

# 定义文件路径
input_file = "txt/source.txt"  # 输入的原始文件
output_file = "txt/processed.txt"  # 输出的处理后的文件
# 定义匹配条件的正则表达式
#pattern = r"f[\sＦ]*o[\sＯ]*z[\sＺ]*e[\sＥ]*d[\sＤ]*s[\sＳ]*"  # 匹配 "fozeds" 及其变种（忽略大小写、全角字符、空格）
# 读取文件内容并过滤
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 删除包含 "佛泽" 的行
filtered_lines = [line for line in lines if "佛泽" not in line]
# 删除匹配条件的行（忽略大小写和空格）
#filtered_lines = [line for line in lines if not re.search(pattern, line, flags=re.IGNORECASE)]

# 写入到新文件
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(filtered_lines)
print(f"处理完成！删除包含 '佛泽' 的行后，结果已保存到 {output_file}")