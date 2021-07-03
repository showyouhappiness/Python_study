import threading, time


def download(n):
    images = ['1.png', '2.png', '3.png', '4.png']
    for image in images:
        print('正在下载：{}'.format(image))
        time.sleep(n)
        print('下载完成：{}！'.format(image))


def listenMusic(n):
    musics = ['1', '2', '3', '4']
    for music in musics:
        time.sleep(n)
        print('正在听{}歌'.format(music))


if __name__ == '__main__':
    t = threading.Thread(target=download, args=(1,))
    t.start()
    t1 = threading.Thread(target=listenMusic, args=(.5,))
    t1.start()
