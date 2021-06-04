import copy

list = [
    'E:/workImages/test_image/23.04.51P348570W20V1I1A0SM0N00316c09R1E0Otunde.jpg',
    'E:/workImages/test_image/23.04.52P348570W20V1I2A0SM0N00316c09R1E0Otunde.jpg',
    'E:/workImages/test_image/23.04.52P348570W20V1I3A0SM0N00316c09R1E0Otunde.jpg',
    'E:/workImages/test_image/23.04.53P348570W20V1I4A0SM0N00316c09R1E0Otunde.jpg',
    'E:/workImages/test_image/23.04.54P348571W20V1I5A0SM0N00316c09R1E0Otunde.jpg',
    'E:/workImages/test_image/23.04.56P348571W20V2I1A0SM0N00316c09R1E0Otunde.jpg',
    'E:/workImages/test_image/23.04.56P348571W20V2I2A0SM0N00316c09R1E0Otunde.jpg',
    'E:/workImages/test_image/23.04.57P348571W20V2I3A0SM0N00316c09R1E0Otunde.jpg',
    'E:/workImages/test_image/23.04.58P348572W20V2I4A0SM0N00316c09R1E0Otunde.jpg',
    'E:/workImages/test_image/23.04.58P348572W20V2I5A0SM0N00316c09R1E0Otunde.jpg',
    'E:/workImages/test_image/23.05.03P348572W20V3I1A0SM0N00316c09R1E0Otunde.jpg',
    'E:/workImages/test_image/23.05.04P348572W20V3I2A0SM0N00316c09R1E0Otunde.jpg'
]

P_number = None
detailfile = None
P_numbers = []
grouplist_parent = []
grouplist = []

for list_one in list:
    '''获取流水号'''
    P_index = list_one.find('P')  # 获取P所在的index
    P_number = list_one[int(P_index):int(P_index) + 7]  # 截取检测步骤和图片序号
    if P_number not in P_numbers:
        P_numbers.append(P_number)
print(P_numbers)

for index, value in enumerate(P_numbers):
    grouplist.clear()
    for detail_file in list:
        if value in detail_file:
            grouplist.append(detail_file)
    grouplist_parent.append(copy.deepcopy(grouplist))
print(len(grouplist_parent), grouplist_parent)
