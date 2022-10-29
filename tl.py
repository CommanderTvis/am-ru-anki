import re
import sqlite3

conn = sqlite3.connect("hyru.db")


def translate(word: str) -> str:
    return ", ".join(map(lambda row: row[0],
                         conn.execute("select name from word where id=("
                                      "   select idTranslation from translation"
                                      "   where idWord == (select id from word where name == ?)"
                                      ")",
                                      (word,))))


def get_translation(words: list[str]) -> list[str]:
    return [re.sub(r"[а-яА-Я]", "", str(translate(word))) for word in words]
