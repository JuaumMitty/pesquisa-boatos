from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from bs4 import BeautifulSoup
import html_to_json

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    # if incoming_msg:
    #     msg.body("Seja bem vindo ao BoatoBot, digite alguma notícia que irei pesquisar se é um boato")
    #     return str(resp)

    search = incoming_msg.replace(" ", "+")
    requestSite = requests.get('https://www.boatos.org/?s=' + search)
    html = requestSite.text  

    def remove_tags(html):
        # parse html content
        soup = BeautifulSoup(html, "html.parser")

        for data in soup(['style', 'script']):
        # remove tags
            data.decompose()

        return soup.find_all("h2", attrs={'class':'entry-title'})
    
    format_html = str(remove_tags(html))
    json_archive = html_to_json.convert(format_html)
    count = 0
    archive = f"Você pesquisou sobre: *{incoming_msg}*"
    archive += "\n\nOlha o que encontrei sobre este assunto"

    try:
        for i in json_archive['h2']:
            count += 1
            try:
                archive += "\n\n*Notícia:* " + json_archive['h2'][count]['a'][0]['_value']
                archive += "\n*Link:* " + json_archive['h2'][count]['a'][0]['_attributes']['href']
                # print('\n\nnoticia: ' + json_archive['h2'][count]['a'][0]['_attributes']['href'])
                # print('\ntitulo: ' + json_archive['h2'][count]['a'][0]['_value'])
            except:
                archive+= ('\n\nOh não! não encontramos mais boatos relacionados a este assunto')
                break

            if count == 5:
                break
    except:
        msg.body("Não encontrei nenhum boato sobre este assunto, visite o site: https://www.boatos.org/ para uma pesquisa mais aprofundada")
        responded = True
        return str(resp)
    
    archive += "\n\nCaso não tenha encontrado o que gostaria, visite o site: https://www.boatos.org/ para mais notícias"

    msg.body(archive)
    responded = True

    if not responded:
        msg.body("Não encontrei nada relacionado")


    return str(resp)


if __name__ == '__main__':
    app.run()