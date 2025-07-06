# 硬編碼
password = "123456"

# Eval
user_input = input("Enter a Python expression: ")
result = eval(user_input)

# 未檢查輸入
file_name = input("Enter the file name: ")
with open(file_name, "r") as file:
    print(file.read())