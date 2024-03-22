# 小美拿到了一个
# 的矩阵，其中每个元素是0或者1。

# 小美认为一个矩形区域是完美的，当且仅当该区域内0的数量好等于1的数量现在，小美希望你回答有多少个
# 的完美矩形区域。你需要回答
# 的所有答案

# 输入描述
# 第一行输入一个正整数
# ，代表矩阵大小
# 接下来的
# 行，每行输入一个长度为
# 的01串，用来表示矩阵

# 输入
# 4
# 1010
# 0101
# 1100
# 0011

# 输出
# 0
# 7
# 0
# 1


n = int(input())
a = [input() for _ in range(n)]
s = [[0] * (n + 1) for _ in range(n + 1)]


def query(x1, y1, x2, y2):
    return s[x2][y2] - s[x2][y1 - 1] - s[x1 - 1][y2] + s[x1 - 1][y1 - 1]


for i in range(1, n + 1):  # 二位前缀和预处理
    for j in range(1, n + 1):
        s[i][j] = (
            s[i][j - 1]
            + s[i - 1][j]
            - s[i - 1][j - 1]
            + (1 if a[i - 1][j - 1] == "1" else 0)
        )

for length in range(1, n + 1):
    count = 0
    for x in range(1, n - length + 2):
        for y in range(1, n - length + 2):
            summation = query(x, y, x + length - 1, y + length - 1)
            # print(summation,length)
            if summation * 2 == length**2:
                count += 1

    print(count)
