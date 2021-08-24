# import requests
# from lxml import etree
# from PIL import Image
# import pytesseract
#
# if __name__ == '__main__':
#     # 或缺页面数据
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
#     }
#     url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
#     page_text = requests.get(url=url, headers=headers).text
#     # 解析出页面中图片的地址
#     tree = etree.HTML(page_text)
#     cod_img_src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
#     cod_data = requests.get(url=cod_img_src, headers=headers).content
#     with open('./code.jpg', 'wb') as fp:
#         fp.write(cod_data)
#     text = pytesseract.image_to_string(Image.open(r'./code.jpg'))
#     print(text)



import pytesseract
from PIL import Image

image = Image.open("test.jpg")
text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
print(text)
