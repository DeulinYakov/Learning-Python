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


# print(cur.fetchall()) - вывод
# print(cur.fetchmany(1)) - вывод 1 записи
# print(cur.fetchone()) - вывод первой записи
# print(cur.fetchone()[1]) - вывод первой записи первый столбец

# Удаление данных
# cur.execute("DELETE FROM articles WHERE rowid = 2")

# Изменение данных
cur.execute("UPDATE articles SET avtor='Moder', views = 1 WHERE title = 'Yandex is cool!'")

# Выборка данных
cur.execute("SELECT rowid, * FROM articles WHERE rowid < 5 ORDER BY views DESC")
items = cur.fetchall()
for el in items:
    print(el[1] + "\n" + el[4])

db.commit()

# Закрываем работу с дб, если открыл нужно закрыть
db.close()
