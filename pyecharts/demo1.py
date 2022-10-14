import re

from pyecharts.charts import Bar, Page
from pyecharts import options as opts
import os
import re
import collections
import pandas as pd

defect_list = ["缩松", "缩松2", "气孔", "气孔2", "钉子", "夹渣", "浇不足", "缩孔", "裂纹", "裂纹1"]
os.chdir(r'C:\Users\Public\Nwt\cache\recv\LeonZhuPC\dbToExcel\crf_line3')
df1 = pd.read_excel(r'line.3_3_report_2022-10-13_15_27_21.xlsx')
data6 = df1.iloc[:, [0, 1, 2, 3, 5]].values  # 读取指定列的所有行数据：读取第一列所有数据
wheel_type_list = []
defect_name = []
all_defect_1 = {}
all_defect_2 = {}
all_defect_dict_OK = collections.OrderedDict()
all_defect_dict_Fail = collections.OrderedDict()
manual_result = ''
i = 0
page = Page(layout=Page.DraggablePageLayout)


def echarts(title, yAxis, xAxis, index, classify):
    index = Bar()
    index.add_xaxis(xAxis)
    index.add_yaxis(classify, yAxis)
    index.set_global_opts(title_opts=opts.TitleOpts(title=title))
    page.add(index)


def defect_10(key, value, index, classify):
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
    cats = pd.cut(value, bins)
    echarts(key, pd.value_counts(cats).tolist(), bins, str(index), classify)
    # print(key, '\n', pd.value_counts(cats))  # 按区间计数


def defect_5(key, value, index, classify):
    bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
    cats = pd.cut(value, bins)
    echarts(key, pd.value_counts(cats).tolist(), bins, str(index), classify)
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
    if defect_data[-2] in ['裂纹', '裂纹2', '浇不足', '缩松2']:
        defect_10(k1, v1, i, 'AI过检')
    else:
        defect_5(k1, v1, i, 'AI过检')

for k2, v2 in all_defect_dict_Fail.items():
    i += 1
    defect_data = k2.split('_')
    if defect_data[-2] in ['裂纹', '裂纹2', '浇不足', '缩松2']:
        defect_10(k2, v2, i, '人工废品')
    else:
        defect_5(k2, v2, i, '人工废品')

page.render("result.html")
