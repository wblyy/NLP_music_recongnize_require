#coding=utf-8
import random
import csv
import MySQLdb
import sys
import re

class Mydb(object):
    def __init__(self, user, passwd, dbname):
        self._id = 0           # use in pop function
        self.user = user
        self.passwd = passwd
        self.dbname = dbname

    @property
    def db(self):
        return MySQLdb.connect("54.223.153.21", self.user, self.passwd, self.dbname, charset='utf8')

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def _execute(self, *args, **kwargs):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args, **kwargs)
        conn.commit()

    def _query_row(self, *args):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args)
        rows = cur.fetchone()
        return rows

    def _query_rows(self, *args):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args)
        rows = cur.fetchall()
        return rows    

class NLPdb(Mydb):
    def __init__(self):
        Mydb.__init__(self, 'root', '654321', 'zhidao_whole')

    def get_sentence(self, related_word,is_required):
        return self._query_rows('select sentence from NLP where related_word=%s and is_required=%s', (related_word,is_required))

    def update_sentence_pos(self,sentence,pos,content):
        self._execute('update NLP set '+pos+'=concat('+pos+',",",%s) where sentence=%s',(content,sentence))

    def update_album_company_by_song(self,song,artist,company):
        self._query_rows("update meta set producer=%s where song=%s and artist=%s", (company,song,artist))


     

        
if __name__ == "__main__":
    mydb = NLPdb()
    