import sqlite3

# Подключение к базе данных 'dbase.db', если её нет она создастся автоматически
db = sqlite3.connect('dbase.db')
# Внутрь пишем разные команды,
# Создаём курсор
cur = db.cursor()

# Метод execute позволяет прописать и выполнить любую команду

"""CREATE TABLE - создание таблицы"""
# cur.execute("""
# CREATE TABLE articles(
# title text,
# full_text text,
# views integer,
# avtor text
# )""")

"""INSERT INTO название талицы VALUES - добавление записи """
# cur.execute("INSERT INTO articles VALUES ('VK is cool!', 'VK is realy cool!', 50, 'Moder')")

cur.execute("SELECT * FROM articles")
print(cur.fetchall())

db.commit()

# Закрываем работу с дб, если открыл нужно закрыть
db.close()
