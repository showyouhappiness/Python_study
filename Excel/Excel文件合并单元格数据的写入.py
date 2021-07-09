import xlwt


# 设置表格样式
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


# 写Excel
def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('学生与老师', cell_overwrite_ok=True)
    row0 = ["姓名", "分数", "备注", "老师"]
    name = ["张飞", "刘备", "关羽", "赵云", "黄忠"]
    fraction = [80, 99, 100, 100, 90]
    Remarks = ['鲁莽', '爱哭', '忠心']
    # 写第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    # 写第一列
    for i in range(0, len(name)):
        sheet1.write(i + 1, 0, name[i])
    # 写第二列
    for i in range(0, len(fraction)):
        sheet1.write(i + 1, 1, fraction[i])
    # 写第三列
    for i in range(0, len(Remarks)):
        sheet1.write(i + 1, 2, Remarks[i])

    sheet1.write_merge(1, 3, 3, 3, '诸葛亮')  # 合并列单元格
    sheet1.write_merge(4, 4, 2, 3, '有勇有谋')  # 合并行单元格
    sheet1.write_merge(5, 5, 2, 3, '射的一手好箭')  # 合并行单元格

    f.save('test1.xls')


if __name__ == '__main__':
    write_excel()
