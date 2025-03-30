import re
'''
脚本功能
1.章节标题检测：
    使用正则表达式 ^第\d+章(.*)$ 匹配章节标题
    \d+ 匹配数字部分
    (.*) 捕获章节标题后面的内容（例如章节名或省略号）
    捕获的内容用 match.group(1) 提取
2.重新编号：
    使用变量 chapter_number 从 1 开始计数
    将章节标题改为 第{chapter_number}章，后跟原来的标题内容
3.保留原文格式：
    非章节标题的行保持不变
'''
# 定义文件路径
input_file = "txt/source.txt"  # 输入的原始文件
output_file = "txt/processed.txt"  # 输出的处理后的文件

# 匹配章节标题的正则表达式
chapter_pattern = r"^第\d+章(.*)$"  # 匹配“第X章...”并捕获后续内容

# 读取文件内容
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 处理章节标题，重新编号
new_lines = []
chapter_number = 1  # 起始编号

for line in lines:
    match = re.match(chapter_pattern, line.strip())
    if match:
        # 如果匹配到章节标题，替换章节编号
        new_title = f"第{chapter_number}章{match.group(1)}"
        new_lines.append(new_title + "\n")
        chapter_number += 1
    else:
        # 非章节标题行保持原样
        new_lines.append(line)

# 写入到新文件
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"处理完成！章节标题已重新编号，结果保存到 {output_file}")