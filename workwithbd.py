import sqlite3


class Bd:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(name, check_same_thread=False)
        self.conn.cursor()
        self.create(name)

    def add_user(self, login, password, name, family):
        c = self.conn.cursor()
        c.execute("SELECT login FROM "+self.name+" WHERE login='"+login+"';")
        log = c.fetchone()
        print(log)
        if log is not None or len(login) <= 6 or len(password) <= 6:
            c.close()
            return False
        else:
            c.execute("INSERT INTO "+self.name+" (login,password,name,family) VALUES (?,?,?,?)", (login, password, name, family))
            self.conn.commit()
            c.close()
            return True

    def print_database(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM "+self.name+";")
        row = c.fetchone()
        while row is not None:
            print(row)
            row = c.fetchone()
        c.close()

    def clear(self):
        c = self.conn.cursor()
        c.execute("    DELETE FROM "+self.name+";")
        self.conn.commit()
        c.close()

    def delete(self, name):
        c = self.conn.cursor()
        c.execute("DROP TABLE IF EXISTS " + name+";")
        self.conn.commit()
        c.close()

    def create(self, name):
        c = self.conn.cursor()
        c.execute(" CREATE TABLE if not exists "+name+" (login TEXT, password TEXT, name TEXT, family TEXT) " + ";")

    def user_exist_in_table(self, login, password):
        c = self.conn.cursor()
        c.execute("SELECT login FROM " + self.name + " WHERE login='" + login + "';")
        log = c.fetchone()
        c.execute("SELECT password FROM " + self.name + " WHERE password='" + password + "';")
        pas = c.fetchone()
        if log is not None and pas is not None:
            return True
        return False