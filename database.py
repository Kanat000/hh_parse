import sqlite3
from config import db_name


class Sqlite:
    __con = sqlite3.connect(db_name)
    __cur = __con.cursor()

    def create_company_table(self):
        self.__cur.execute('Create table if not exists companies('
                           'id integer PRIMARY KEY AUTOINCREMENT NOT NULL,'
                           'company_name varchar(255),'
                           'description Text,'
                           'link Text,'
                           'logo_link Text,'
                           'count_of_active_vacancy int)')
        self.__con.commit()

    def insert_company(self, data):
        self.__cur.execute('Insert into companies(company_name, description, link, '
                           'logo_link, count_of_active_vacancy) values(?,?,?,?,?)',
                           (data['name'], data['description'], data['link'], data['logo'],
                            data['active_vacancy_count']))
        self.__con.commit()

    def exists_company(self, link):
        self.__cur.execute(f'Select count(*) from companies where link = "{link}"')
        return self.__cur.fetchone()[0]>0
