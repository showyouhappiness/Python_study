import collections

dict2 = {'001375_Lef_0_resultNG.jpg': 'Lef_0_result',
         '001375_Lef_2_resultNG.jpg': 'Lef_2_result',
         '001375_Top_1_resultNG.jpg': 'Top_1_result',
         '001375_Top_2_resultNG.jpg': 'Top_2_result',
         '001375_Btm_0_resultNG.jpg': 'Btm_0_result',
         '001375_Btm_2_resultNG.jpg': 'Btm_2_result',
         '001375_Top_0_resultOK.jpg': 'Top_0_result',
         '001375_Btm_1_resultOK.jpg': 'Btm_1_result',
         '001375_Lef_1_resultOK.jpg': 'Lef_1_result',
         }

dict_new = {key: value for key, value in sorted(dict2.items(), key=lambda x: x)}
print(dict_new)
