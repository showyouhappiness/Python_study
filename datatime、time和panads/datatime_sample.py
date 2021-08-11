"""
datetime模块常用的类如下：
类型	        说明
date	    日期对象，以公历形式存储日期（年、月、日）
time	    时间对象，将时间存储为：时、分、秒、毫秒
datetime	存储日期和时间
timedelta	时间间隔，表示两个datetime之间的差
附录（日期和时间的格式化符号表）

符号	说明
%y	两位数的年份表示（00-99）
%Y	四位数的年份表示（000-9999）
%m	月份（01-12）
%d	月内中的一天（0-31）
%H	24小时制小时数（0-23）
%I	12小时制小时数（01-12）
%M	分钟数（00=59）
%S	秒（00-59）
%a	本地简化星期名称
%A	本地完整星期名称
%b	本地简化的月份名称
%B	本地完整的月份名称
%c	本地相应的日期表示和时间表示
%j	年内的一天（001-366）
%p	本地A.M.或P.M.的等价符
%U	一年中的星期数（00-53）星期天为星期的开始
%w	星期（0-6），星期天为星期的开始
%W	一年中的星期数（00-53）星期一为星期的开始
%x	本地相应的日期表示
%X	本地相应的时间表示
%Z	当前时区的名称
%%	%号本身
"""

from datetime import date, time, datetime, timedelta

# date类代码演示：datetime.date(year, month, day)
# 获取当前的日期
today = date.today()
print(today)  # 2021-08-10
print(today.day)  # 10
# 也可以创建一个指定的日期对象
tomorrow = date(2021, 8, 11)
print(tomorrow)  # 2021-08-11
print(tomorrow.day)  # 11
print(today.strftime('%Y-%m-%d'))  # 相当于格式化输出

# time类代码演示：datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] )
# 创建一个time对象
t = time(14, 20, 59, 83999)
print(t)  # 14:20:59.083999
print(t.strftime('%H:%M:%S'))  # 相当于格式化输出

# datetime代码演示：datetime相当于date和time结合起来
# datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )
now = datetime.now()
print(now)  # datetime.datetime(2021, 8, 10, 15, 21, 6, 581886)
print(now.year)  # 2021
print(now.month)  # 8
print(now.day)  # 21
print(now.date())
print(now.time())
print(now.strftime('%Y-%m-%d  %H:%M:%S'))  # 格式化输出

# timedelta代码演示：使用timedelta可以很方便的在日期上做天days，小时hours，分钟，秒，毫秒，微妙的时间计算，如果要计算月份则需要另外的办法。
dt = datetime.now()
# 日期减一天,dt1和dt2都表示昨天，两种不同的操作方式
dt1 = dt + timedelta(days=-1)  # 昨天
dt2 = dt - timedelta(days=1)  # 昨天
dt3 = dt + timedelta(days=1)  # 明天
print(dt1)
print(dt2)
print(dt3)
# 也可以小时的加减
t1 = dt + timedelta(hours=1)
print(t1)

# 例子:获取指定日期月份的最后一天的日期和本月天数
date1 = datetime.now()


def eomonth(date_object):
    if date_object.month == 12:
        next_month_first_date = date(date_object.year + 1, 1, 1)
    else:
        next_month_first_date = date(date_object.year, date_object.month + 1, 1)

    return next_month_first_date - timedelta(1)


print(eomonth(date1))
print(eomonth(date1).day)
