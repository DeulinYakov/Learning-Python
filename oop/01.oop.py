class Image:
    def __init__(self, width=0, heiqht=0, type='lpg'):
        self.width = width
        self.heiqht = heiqht
        self.type = type

    def resize(self, w, h):
        self.width = w
        self.heiqht = h

    def show_size(self):
        print(f'new width: {self.width} \nnew heiqht: {self.heiqht}')


images = Image()
images.resize(300, 400)
images.show_size()
