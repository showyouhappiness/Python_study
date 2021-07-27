import filetype

address1 = r'C:\Users\Administrator\algorithm.log'
address = r'C:\Users\Administrator\.crf-config.pkl'


def main():
    kind = filetype.guess(address1)
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)


if __name__ == '__main__':
    main()
