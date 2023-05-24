class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        self.__instance = None

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f'Connect: {self}')

    def close(self):
        print('close connect')

    def read(self):
        return 'data from DB'

    def write(self, data):
        print(f'write {data}')


db = DataBase('root', '123', 69)
db2 = DataBase('user', '321', 96)

