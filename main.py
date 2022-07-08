import bs4
from bs4 import BeautifulSoup
import requests
import re


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def export_data():
    print("Enter a word:")
    word = input()

    url = "https://www.merriam-webster.com/dictionary/" + f"{word}"
    page = requests.get(url)
    if page.status_code == 404:
        print("word not found!")
        return 1

    soup = BeautifulSoup(page.content, 'html.parser')
    all_info = soup.find_all('strong', class_="mw_t_bc")

    definitions = []

    for current_entry in all_info:
        definition = current_entry.nextSibling
        remainng_definition = current_entry.nextSibling.next
        if type(definition) == bs4.element.NavigableString:
            str_remaining_definition = remove_html_tags(str(remainng_definition))
            if str_remaining_definition == "\n" or str_remaining_definition == ": ":
                pass
            else:
                definition += str_remaining_definition

            definitions.append(definition)

    print(f"The definitions of {word} (according to https://www.merriam-webster.com/) are: \n")
    for i in definitions:
        print("- " + i + "\n")


if __name__ == '__main__':
    export_data()
