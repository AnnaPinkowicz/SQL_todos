import pprint
import sqlite3
import logging


class Todos:

    def __init__(self, conn):
        self.conn = conn
        self.create_tables(show_warning=False)

    def create_tables(self, show_warning=True):
        try:
            curr = self.conn.cursor()
            curr.execute("CREATE TABLE todos (todo varchar(255), description varchar(255), done bool);")
            self.conn.commit()
        except sqlite3.OperationalError:
            if show_warning:
                logging.warning("One of tables already exists")

    def get_all(self):
        curr = self.conn.cursor()
        curr.execute("SELECT * FROM todos")
        return curr.fetchall()

    def create_todo(self, todo, description, done):
        curr = self.conn.cursor()
        curr.execute("INSERT INTO todos (todo, description, done) VALUES (?,?,?)", (todo, description, done))
        conn.commit()

    def get_todo(self, todo_name):
        curr = self.conn.cursor()
        curr.execute("SELECT * FROM todos WHERE todo = ?", (todo_name,))
        return curr.fetchone()

    def delete_todo(self, todo_name):
        curr = self.conn.cursor()
        curr.execute("DELETE FROM todos WHERE todo = ?", (todo_name,))
        conn.commit()
        # TODO:

    def update_todo(self, todo, description=None, done=None):
        curr = self.conn.cursor()
        if description is not None:
            curr.execute("UPDATE todos SET description= ? WHERE todo = ?", (description, todo,))
        if done is not None:
            curr.execute("UPDATE todos SET done = ? WHERE todo = ?", (done, todo,))
        conn.commit()


if __name__ == '__main__':
    import os

    database_path = "todos.db"

    if os.path.isfile(database_path):
        os.remove(database_path)

    conn = sqlite3.connect(database_path)
    todos = Todos(conn=conn)

    # Tworzenie
    todos.create_todo("1", "d1", True)
    todos.create_todo("2", "d2", True)
    todos.create_todo("3", "d3", True)
    assert len(todos.get_all()) == 3

    # Wybieranie
    assert todos.get_todo("1") == ("1", "d1", True)
    assert todos.get_todo("2") == ("2", "d2", True)
    assert todos.get_todo("3") == ("3", "d3", True)

    # Modyfikacja
    todos.update_todo("1", description="m1")
    todos.update_todo("2", done=False)
    todos.update_todo("3", description="m3", done=False)
    assert todos.get_todo("1") == ("1", "m1", True)
    assert todos.get_todo("2") == ("2", "d2", False)
    assert todos.get_todo("3") == ("3", "m3", False)

    # Usuwanie
    todos.delete_todo("1")
    assert len(todos.get_all()) == 2