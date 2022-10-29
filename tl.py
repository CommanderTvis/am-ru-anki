"""Module for automatic generation of TSV-files for vocabulary cards."""

import re
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup


class TranslatorError(Exception):
    pass


def translate(word: str) -> str:
    url = "https://bararanonline.com/" + quote(word)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find(id="translation")


def get_translation(words: list[str]) -> list[str]:
    translations = []
    for word in words:
        translations.append(re.sub(r"[а-яА-Я]", "", str(translate(word))))

    return translations


