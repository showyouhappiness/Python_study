# 必须保证带有缺省（默认）参数都放在参数列表的最后面
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值
def print_info(name, title="", gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("[%s]%s是%s" % (title, name, gender_text))


# 在调用函数时，如果有多个缺省参数，需要指定参数名，这样解释器才能够知道参数的对应关系
print_info("小明")
print_info("小美", gender=False)
