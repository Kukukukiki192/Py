'''
脚本逻辑详解
1. current_chapter 变量：
    用来保存当前的章节编号，初始化为 0
    每当识别到明确的章节（如 “第X章” 或 “X、” 等），更新为最新章节号
2. 自动递增序号：
    当遇到 “☆、标题” 时，将 current_chapter 加 1，并生成新的章节标题
source.txt:
    第1章 第一章标题
    第2章
    3
    4、
    5、第五章标题
    ☆、特别章节
    普通文本内容
processed.txt:
    第1章 第一章标题
    第2章
    第3章
    第4章
    第5章 第五章标题
    第6章 特别章节
    普通文本内容
'''
import re
# 定义文件路径
input_file = "txt/source.txt"  # 输入的原始文件
output_file = "txt/processed.txt"  # 输出的处理后的文件

# 初始化章节编号
current_chapter = 0

def process_line(line):
    global current_chapter
    line = line.strip()  # 去除多余的空格或换行符

    # 1. 匹配 "第X章 标题"
    if re.match(r"^第\d+章 .+", line):
        current_chapter = int(re.match(r"^第(\d+)章", line).group(1))
        return line

    # 2. 匹配 "第X章"
    if re.match(r"^第\d+章$", line):
        current_chapter = int(re.match(r"^第(\d+)章", line).group(1))
        return line

    # 3. 匹配 "X" （数字单独一行）
    if re.match(r"^\d+$", line):
        current_chapter = int(line)
        return f"第{current_chapter}章"

    # 4. 匹配 "X、"
    if re.match(r"^\d+、$", line):
        current_chapter = int(re.match(r"^(\d+)", line).group(1))
        return f"第{current_chapter}章"

    # 5. 匹配 "X、标题"
    if re.match(r"^\d+、.+", line):
        match = re.match(r"^(\d+)、(.+)", line)
        current_chapter = int(match.group(1))
        title = match.group(2)
        return f"第{current_chapter}章 {title}"

    # 6. 匹配 "☆、标题"
    if re.match(r"^☆、.+", line):
        title = re.match(r"^☆、(.+)", line).group(1)
        current_chapter += 1  # 按上一章节递增
        return f"第{current_chapter}章 {title}"

    # 其他情况保持不变
    return line

# 读取文件内容
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 处理每一行
processed_lines = [process_line(line) for line in lines]

# 写入到新文件
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(processed_lines))

print(f"章节标题已处理完成！输出文件为 {output_file}")

'''
eg
source.txt:
第1章 第一章标题
第2章
3
4、
5、第五章标题
☆、特别章节
普通文本内容
processed.txt:
第1章 第一章标题
第2章
第3章
第4章
第5章 第五章标题
第6章 特别章节
普通文本内容
'''
