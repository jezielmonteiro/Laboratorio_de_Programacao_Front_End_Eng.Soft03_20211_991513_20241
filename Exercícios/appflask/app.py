from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2>SKRILLEX</h2>'

@app.route('/biografia')
def biografia():
    return '<h2>BIOGRAFIA</h2>' '<p>SONNY JOHN MOORE, MAIS CONHECIDO PELO NOME ARTÍSTICO SKRILLEX, É UM DJ, PRODUTOR MUSICAL, CANTOR E COMPOSITOR NORTE AMERICANO.</p>'

@app.route('/discografia')
def discografia():
    return '<h2>DISCOGRAFIA</h2>' '<br>' '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/album/7tWP3OG5dWphctKg4NMACt?utm_source=generator&theme=0" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>' '<br>' '<br>' '<br>' '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/album/5XJ2NeBxZP3HFM8VoBQEUe?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>' '<br>' '<br>' '<br>' '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/album/7rf1qZJ6hGSlPN7K9ShsVV?utm_source=generator&theme=0" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>' '<br>' '<br>' '<br>' 

@app.route('/turnes')
def turnes():
    return '<h2>TURNÊS</h2>' '<u1>AUCKLAND<br>22/09/23</u1>' '<br>' '<br>' '<br>' '<u1>BRISBANE, AUSTRÁLIA<br>23/09/23</u1>' '<br>' '<br>' '<br>' '<u1>JOONDALUP, AUSTRÁLIA<br>24/09/23</u1>' '<br>' '<br>' '<br>' '<u1>FINNS BEACH CLUB<br>BALI, INDONÉSIA<br>12/05/23</u1>' '<br>' '<br>' '<br>' '<u1>MELBOURNE, AUSTRÁLIA<br>29/09/23</u1>' '<br>' '<br>' '<br>' '<u1>SYDNEY, AUSTRÁLIA<br>30/09/23</u1>' '<br>' '<br>' '<br>' '<u1>AUCKLAND, NOVA ZELÂNDIA<br>01/10/23</u1>' '<br>' '<br>' '<br>' '<u1>PORTOLA MUSIC FESTIVAL<br>São Francisco, CA<br>01/10/23</u1>' '<br>' '<br>' '<br>' '<u1>III POINTS FESTIVAL<br>MIAMI, FL<br>20/10/23</u1>' '<br>' '<br>' '<br>' '<u1>HIJINX<br>FILADÉLFIA, PA<br>29/12/23</u1>' '<br>' '<br>' '<br>' '<u1>LIGHTS ALL NIGHT<br>DALLAS, TX<br>30/12/23</u1>' '<br>' '<br>' '<br>'

@app.route('/contato')
def contato():
    return '<h2>CONTATE-ME</h2>' '<label for="nome">NOME:</label>' '<input type="text" id="nome" name="nome">' '<label for="email">E-MAIL:</label>' '<input type="email" id="email" name="email">' '<label for="mensagem">MENSAGEM:</label>' '<textarea id="mensagem" name="mensagem"></textarea>' '<input type="submit" value="ENVIAR">'

@app.route('/redes-sociais')      
def redes_sociais():
    return '<h2>REDES SOCIAIS</h2>' '<a href="https://www.facebook.com/skrillex">FACEBOOK</a>' '<br>' '<br>' '<a href="https://twitter.com/Skrillex">TWITTER</a>' '<br>' '<br>' '<a href="https://www.instagram.com/skrillex">INSTAGRAM</a>' '<br>' '<br>' 
