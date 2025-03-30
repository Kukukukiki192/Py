'''
功能说明
1. 删除多余空行：
    连续多行空行会被压缩为一行
    全文中的所有空白行都被去掉，只保留必要的空行
2. 章节标题格式化：
    确保章节标题的格式符合 第X章 的模式
    如果 第X章 开头的标题不是单独一行，脚本会将其拆分为单独一行
    确保 第X章 标题前始终有一个空行
3. 普通段落处理：
    段落之间的多余空行会被清理，保留简洁的结构
source.txt:
    第2章   旅程的开始
    这一段继续描述情节。
    
    
    第3章结尾
    ...
processed.txt:
    第2章 旅程的开始
    这一段继续描述情节。

    第3章 结尾
    ...
'''
import re
# 定义文件路径
input_file = "txt/source.txt"  # 输入的原始文件
output_file = "txt/processed.txt"  # 输出的处理后的文件

# # 定义正则表达式
# chapter_pattern = r"^(第\d+章.*)$"  # 匹配章节标题，如“第1章 标题”
#
# # 读取文件内容
# with open(input_file, "r", encoding="utf-8") as f:
#     lines = f.readlines()
#
# # 删除多余空行并格式化章节标题
# processed_lines = []
# previous_line_blank = True  # 用于判断上一行是否为空，避免重复空行
#
# for line in lines:
#     stripped_line = line.strip()
#
#     # 如果是章节标题
#     if re.match(chapter_pattern, stripped_line):
#         # 确保章节标题前有一个空行
#         if processed_lines and processed_lines[-1] != "\n":
#             processed_lines.append("\n")
#         processed_lines.append(f"{stripped_line}\n")
#         previous_line_blank = False
#     elif stripped_line:  # 如果是普通非空行
#         if not previous_line_blank:
#             processed_lines.append(f"{stripped_line}\n")
#         else:
#             processed_lines.append(f"{stripped_line}\n")
#         previous_line_blank = False
#     else:  # 如果是空行
#         if not previous_line_blank:  # 只保留一个空行
#             processed_lines.append("\n")
#         previous_line_blank = True
#
# # 写入到新文件
# with open(output_file, "w", encoding="utf-8") as f:
#     f.writelines(processed_lines)
#
# print(f"处理完成！结果已保存到 {output_file}")

# 匹配“第X章”的正则表达式
chapter_pattern = r"^第\d+章.*$"

# 读取文件内容
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 处理文件内容，删除标题行后的空行
processed_lines = []
skip_next_line = False  # 标记是否跳过下一行

for i, line in enumerate(lines):
    stripped_line = line.strip()

    if skip_next_line:
        # 如果上一行是标题行且当前行是空行，则跳过
        if stripped_line == "":
            skip_next_line = False  # 只跳过一行空行
            continue

    # 检查是否是章节标题
    if re.match(chapter_pattern, stripped_line):
        processed_lines.append(line)  # 保留章节标题行
        skip_next_line = True  # 标记需要跳过下一行的空行
    else:
        processed_lines.append(line)  # 保留非章节标题行

# 写入到新文件
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(processed_lines)

print(f"处理完成！结果已保存到 {output_file}")