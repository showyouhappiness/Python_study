import xlrd
from xlrd import xldate_as_tuple
import datetime

# 读取Excel文件
file = u"test.xls"  # 注意读中文文件名稍微处理一下
data = xlrd.open_workbook(file)

# Sheet1
table = data.sheet_by_index(0)  # 按照索引读Excel文件
firstrows = table.row_values(0)
print("读取第一行:" + str(firstrows))

totalRows = table.nrows  # 行
totalCols = table.ncols  # 列
print("总行数" + str(totalRows), "总列数" + str(totalCols))

nowDate = '2020-12-05'
targetCol = 0
# 读取第0行 第i列的数据：
for i in range(0, totalCols):
    cType = table.cell_type(0, i)  # 读取第0行，第i列的单元格数据类型
    '''
       根据cType判断单元格的数据类型： 
       0 empty,
       1 string, 
       2 number, 
       3 date, 
       4 boolean, 
       5 error
    '''
    if cType == 3:
        result = table.cell_value(0, i)  # 读取第0行，第i列的单元格数据
        date = datetime.datetime(*xldate_as_tuple(result, 0)).strftime('%Y-%m-%d')
        if (nowDate <= date):
            targetCol = i
            break
excelMap = {}
for i in range(0, totalRows):
    rowList = []
    # 读取第一列
    cellValueZero = table.cell_value(i, 0)
    rowList.append(cellValueZero)
    for j in range(targetCol, totalCols):
        cType = table.cell_type(i, j)
        cellValue = table.cell_value(i, j)

        if cType == 3:
            cellValue = datetime.datetime(*xldate_as_tuple(cellValue, 0)).strftime('%Y-%m-%d')
        rowList.append(cellValue)
    excelMap[str(i) + "行"] = rowList
print(excelMap)
print(table.merged_cells)
# print(table.cell_value(1, 3))
# print(table.cell_value(4, 3))
# print(table.cell_value(6, 2))
