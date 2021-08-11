"""
object转日期时间类型

原有数据类型（object）和展示形式      想得到的格式	                  代码
2021-08-10	                     2021-08-10	              pd.to_datetime(data['time_object'])
08/10/21	                     2021-08-10	              pd.to_datetime(data['time_object'],format='%m/%d/%y')
2021-08-10 14:20:59	             2021-08-10 14:20:59	  pd.to_datetime(data['time_object'])
2021年08月	                     2021-08-01	              pd.to_datetime(data['time_object'],format='%Y年%m月')
"""

"""
日期转固定格式的

原有数据类型（datetime64）和展示形式	 想得到的格式	                   代码
2021-08-10 14:20:59	             2021-08-10	               data['datetime_col'].dt.date 或者pd.to_datetime(data['datetime_col'].dt.strftime('%Y-%m-%d'))
2021-08-10 14:20:59	             2021-08-10 00:00:00	   data['datetime_col'].dt.strftime('%Y-%m-%d 00:00:00')
"""

"""
提取日期类型的年月日

原有数据类型（datetime64）和展示形式	  想得到的格式	               代码
2021-08-10 14:20:59	              2021	                   data['datetime_col'].dt.year
2021-08-10 14:20:59	              8	                       data['datetime_col'].dt.month
2021-08-10 14:20:59	              10	                   data['datetime_col'].dt.day
2021-08-10 14:20:59	              14	                   data['datetime_col'].dt.hour
2021-08-10 14:20:59	              20	                   data['datetime_col'].dt.minute
2021-08-10 14:20:59	              59	                   data['datetime_col'].dt.second
"""

"""
时间差的计算

startdate	             enddate	              difference	      代码
2018-02-14 12:20:36	     2019-02-28 13:38:41	  379.054225	      (data['datetime_col']-data['datetime_col'])/np.timedelta64(1,'D')
"""
