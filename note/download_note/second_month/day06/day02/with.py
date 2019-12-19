"""
with示例
"""

with open('file') as f:    # f = open('file')
    data = f.read()
    print(data)

# with语句块结束 则f自动销毁