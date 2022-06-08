from PIL import Image


def is_valid_image(image_path):
    try:
        Image.open(image_path).verify()
        print(Image.open(image_path).verify())
        return True
    except:
        return False


print(is_valid_image(r'D:\images_crf1\23.08.52P348573W20V6I6A0SM0N00316c09R1E0Otunde.jpg'))
