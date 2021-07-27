# 方法一：
import IPy


def is_ip1(address):
    try:
        result = IPy.IP(address)
        print(result)
        return True
    except Exception as e:
        print(e)
        return False


is_ip1('172.16')


# 方法二：
def is_ip(ip):
    num_list = ip.split(".")
    if len(num_list) != 4:
        print(ip)
        return False
    check_num = 0
    for num in num_list:
        if num.isdigit() and 0 <= int(num) <= 255 and str(int(num)) == num:
            check_num = check_num + 1
    if check_num == 4:
        print(ip, 'True')
    else:
        print(ip, 'False')


is_ip('172.16.1.255')
