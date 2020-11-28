import pprint
import sqlite3
import logging

def create_tables(conn):
      try:
          curr = conn.cursor()
          curr.execute("CREATE TABLE todos (todo varchar(255), description varchar(255), done varchar(255));")
          conn.commit()
      except sqlite3.OperationalError:
          logging.warning("One of tables already exists")

def show_all(conn):
      curr = conn.cursor()
      curr.execute("SELECT * FROM todos")
      data_todos = curr.fetchall()
      pprint.pprint(data_todos)


def create_todo(todo, description, done):
      curr = conn.cursor()
      curr.execute("INSERT INTO todos (todo, description, done) VALUES (?,?,?)", (todo, description, done))
      conn.commit()

def get_todo(todo):
    curr = conn.cursor()
    curr.execute("SELECT todo FROM todos WHERE todo = todo")
    conn.commit()
    return todo

def delete_todo(todo):
    curr = conn.cursor()
    curr.execute("DELETE FROM todos WHERE todo = todo")
    conn.commit()
    print("Deleted")

def update_todo(todo,description,done):
    curr = conn.cursor()
    curr.execute("UPDATE todos SET todo = todo, description= description, done = done WHERE todo = todo")
    conn.commit()
  
if __name__ == '__main__':
      conn = sqlite3.connect("todos.db")
      create_tables(conn)
      show_all(conn)
      create_todo("python", "nauka sqlite","True")
      update_todo("python","flask","False")
      create_todo("sql","repeating","False")
      show_all(conn)
      delete_todo("python")
      show_all(conn)
