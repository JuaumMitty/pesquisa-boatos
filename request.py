import requests
from bs4 import BeautifulSoup
import html_to_json

pesquisa = input("O que deseja pesquisar? ").replace(" ", "+")
request = requests.get('https://www.boatos.org/?s=' + pesquisa)
print(pesquisa)
html = request.text

def remove_tags(html):

    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):
        # remove tags
        data.decompose()

    return soup.find_all("h2")


format_html = str(remove_tags(html))

json_archive = html_to_json.convert(format_html)

count = 0
arquivo = ""

for i in range(0,10):
    count = count + 1
    arquivo += "\n\n" + json_archive['h2'][count]['a'][0]['_attributes']['href']
    arquivo += "\n" + json_archive['h2'][count]['a'][0]['_value']

    print('\n\nnoticia: ' + json_archive['h2'][count]['a'][0]['_attributes']['href'])
    print('\ntitulo: ' + json_archive['h2'][count]['a'][0]['_value'])


with open('noticias.txt', 'w', encoding='utf-8') as f:
    f.write(str(arquivo))
