import re

from pyecharts.charts import Bar, Page
from pyecharts import options as opts
import os
import re
import collections
import pandas as pd

defect_list = ["缩松", "缩松2", "气孔", "气孔2", "钉子", "夹渣", "浇不足", "缩孔", "裂纹", "裂纹1"]
os.chdir(r'D:\Nwt\cache\recv\LeonZhuPC\dbToExcel\crf_mengwei\1409')
df1 = pd.read_excel(r'line.mengwei_8_report_2023-07-05_11_23_07.xlsx')
data6 = df1.iloc[:, [0, 1, 2, 3, 5]].values  # 读取指定列的所有行数据：读取第一列所有数据
wheel_type_list = []
defect_name = []
all_defect_1 = {}
all_defect_2 = {}
all_defect_dict_OK = collections.OrderedDict()
all_defect_dict_Fail = collections.OrderedDict()
manual_result = ''
i = 0
page = Page()


def echarts(title, yAxis1, yAxis2, xAxis, classify1, classify2):
    index = Bar()
    index.add_xaxis(xAxis)
    index.add_yaxis(classify1, yAxis1)
    index.add_yaxis(classify2, yAxis2)
    index.set_global_opts(title_opts=opts.TitleOpts(title=title))
    page.add(index)


def defect_10(key, value, value2, index, classify, classify2):
    # for i in range(10, 180, 10):
    #     bins.append(i)
    bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]
    yAxis1 = pd.value_counts(pd.cut(value, bins)).tolist()
    yAxis2 = pd.value_counts(pd.cut(value2, bins)).tolist()
    echarts(key, yAxis1, yAxis2, bins, classify, classify2)
    # print(key, '\n', pd.value_counts(cats))  # 按区间计数


def defect_5(key, value, value2, index, classify, classify2):
    bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
    yAxis1 = pd.value_counts(pd.cut(value, bins)).tolist()
    yAxis2 = pd.value_counts(pd.cut(value2, bins)).tolist()
    echarts(key, yAxis1, yAxis2, bins, classify, classify2)
    # print(key, '\n', pd.value_counts(cats))  # 按区间计数


for data in data6:
    if isinstance(data[2], str):
        if data[-1] in ['OK', 'Fail']:
            manual_result = data[-1]
        if ',' in data[2]:
            defect_name = data[2].split(',')
        else:
            defect_name = data[2].split(' ')
        if data[-2] and isinstance(data[-2], str) and data[1] == 'Fail':
            N_index = data[0].find('N')
            R_index = data[0].find('R')
            V_index = data[0].find('V')
            wheel_type = data[0][int(N_index):int(R_index)]
            wheel_type_list.append(wheel_type)
            step_type = data[0][int(V_index):int(V_index) + 2]
            defect_max_area = re.findall(r"\d+\.?\d*", data[-2])
            if '1' in defect_max_area:
                defect_max_area = list(filter(lambda x: x != '1', defect_max_area))
            if '2' in defect_max_area:
                defect_max_area = list(filter(lambda x: x != '2', defect_max_area))
            if '疑似网偏' in defect_name:
                defect_name = list(filter(lambda x: x != '疑似网偏', defect_name))
            try:
                for i, k in enumerate(defect_name):
                    v = float(defect_max_area[i * 3])
                    key_name = wheel_type + '_' + step_type + '_' + k
                    if manual_result == 'OK':
                        all_defect_dict_OK.setdefault(key_name, []).append(v)
                    else:
                        all_defect_dict_Fail.setdefault(key_name, []).append(v)
            except Exception as e:
                pass

for k1, v1 in all_defect_dict_OK.items():
    i += 1
    defect_data = k1.split('_')
    if k1 in all_defect_dict_Fail.keys():
        v2 = all_defect_dict_Fail.get(k1)
        if defect_data[-1] in ['裂纹', '裂纹2', '浇不足', '缩松2']:
            defect_10(k1, v1, v2, i, 'AI过检', '人工判废')
        else:
            defect_5(k1, v1, v2, i, 'AI过检', '人工判废')
    else:
        if defect_data[-1] in ['裂纹', '裂纹2', '浇不足', '缩松2']:
            defect_10(k1, v1, [], i, 'AI过检', '人工判废')
        else:
            defect_5(k1, v1, [], i, 'AI过检', '人工判废')

page.render("result.html")
