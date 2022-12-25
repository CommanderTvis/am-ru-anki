import sqlite3

conn = sqlite3.connect("hyru.db")


def translate(word: str) -> str:
    if ";" in word:
        w, t = word.split(";")
        print(w, t)
        return t
    tl = ", ".join(map(lambda row: row[0],
                       conn.execute("select name from word where id IN ("
                                    "   select idTranslation from translation"
                                    "   where idWord == (select id from word where name == ?)"
                                    ")",
                                    (word,))))
    if tl is None or tl == "":
        print(word, "NO TRANSLATION")
    else:
        print(word, tl)
    return tl


def get_translation(words: list[str]) -> list[str]:
    tl = list()

    for idx, word in enumerate(words):
        if ";" in word:
            w, t = word.split(";")
            print(w, t)
            words[idx] = w
            tl.append(t)
        else:
            tl.append(translate(word))

    return tl
