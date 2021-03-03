
password = 'a123456'
try_num = 3
while try_num >= 0:
    user_try = input('Please input password: ')
    if user_try == password:
        print('登入成功')
        break
    elif user_try != password and try_num >= 1: 
        print('密碼錯誤! 還有', try_num, '次機會')
        try_num = try_num - 1
    elif user_try != password and try_num < 1:
        print('請重新開啟程式輸入密碼') 
        break



