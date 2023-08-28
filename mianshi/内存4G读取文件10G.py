def get_lines():
    l = []
    with open('file.txt', 'rb') as f:
        data = f.readlines(60000)
        l.append(data)
        yield l
