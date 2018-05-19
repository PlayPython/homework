# - 文件过滤，显示一个文件的所有行，忽略以#开始的行
# - 比较文件，写一个比较文件的程序，如果不同，给出第一个不同处的行号和列号
# - 统计一个文本中每个单词出现个数

import codecs


def show_lines():
    with codecs.open('string.py', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip().startswith("#"):
                print(line)


def compare_files():
    with codecs.open('file.py', 'r', encoding='utf-8') as f:
        f1_lines = f.readlines()

    with codecs.open('string.py','r',encoding='utf-8') as f:
        f2_lines=f.readlines()

    if f1_lines != f2_lines:
        line_numbers = min(len(f1_lines), len(f2_lines))
        for i in range(0, line_numbers):
            line = i
            if f1_lines[i] != f2_lines[i]:
                letter_numbers = min(len(f1_lines[i]), len(f2_lines))
                for j in range(0, letter_numbers):
                    column = j
                    if f1_lines[i][j] != f2_lines[i][j]:
                        return line, column
                if len(f2_lines[i]) != len(f1_lines[i]):  # 如果同一行字符串出现包含关系，则返回更长字符串第一个
                    return line, column + 1
        if len(f2_lines) != len(f1_lines):  # 如果两文件出现包含关系，则返回更长文件下一行第一个
            return line + 1, 0
    else:
        return "equal"
    # return line, column


if __name__ == '__main__':
    # show_lines()
    print(compare_files())
