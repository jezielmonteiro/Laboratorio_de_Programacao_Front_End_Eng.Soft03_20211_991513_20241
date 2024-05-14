from flask import Flask, render_template
from palestrante import Palestrante
from sessao import Sessao

app = Flask(__name__)

psicologia = Sessao(1, "Psicologia", "/static/img/psi.png", "Sessão dedicada a área da Psicologia.", "12:00 - 14:00", "Universidade de Vassouras", "João: 'Adorei a palestra do Jeziel sobre psicologia! Foi muito esclarecedora.'")

fisioterapia = Sessao(2, "Fisioterapia", "/static/img/fisio.png", "Sessão dedicada a área da Fisioterapia.", "14:30 - 16:30", "Universidade de Vassouras", "Maria: 'Maravilhosa a palestra do Felipe sobre fisioterapia! Amei!!!'")

nutricao = Sessao(3, "Nutrição", "/static/img/nutri.png", "Sessão dedicada a área da Nutrição.", "17:00 - 19:00", "Universidade de Vassouras", "Pedro: 'Ótima palestra do Luiz sobre nutrição.'")

sessao_detalhes = [psicologia, fisioterapia, nutricao]


jeziel = Palestrante(1, "Jeziel Monteiro", "/static/img/palestrante.png", "Aluno de Engenharia de Software na Universidade de Vassouras", "Desenvolvedor de Software", "https://www.linkedin.com/in/jezielmonteiro/", "https://github.com/jezielmonteiro", "https://www.instagram.com/jzlmntro_/", "Psicologia", "João: Adorei a palestra do Jeziel sobre psicologia! Foi muito esclarecedora.")

felipe = Palestrante(2, "Felipe Alves", "/static/img/palestrante.png", "Aluno de Engenharia de Software na Universidade de Vassouras", "Desenvolvedor de Jogos", "https://www.linkedin.com/in/felipe-alves-soares/", "https://github.com/felipes-alves-soares", "https://www.instagram.com/felipe.alvessoares.35/", "Fisioterapia", "Maria: 'Maravilhosa a palestra do Felipe sobre fisioterapia! Amei!!!")

luiz = Palestrante(3, "Luiz Henrique", "/static/img/palestrante.png", "Aluno de Engenharia de Software na Universidade de Vassouras", "Administrador de Sistemas", "https://www.linkedin.com/in/luiz-henrique-souza-abb058255/", "https://github.com/luizzsouza__", "https://www.instagram.com/luizzsouza__/", "Nutrição", "Pedro: 'Ótima palestra do Luiz sobre nutrição.")

palestrante_detalhes = [jeziel, felipe, luiz]

@app.route("/")
def home():
    return render_template("home.html",
                        sessoes = sessao_detalhes, 
                        palestrantes = palestrante_detalhes)

@app.route("/sessao/<int:id>")
def sessao(id:int):
    for sessao_detalhada in sessao_detalhes:
        if sessao_detalhada.id == id:
            return render_template("sessao.html", sessao = sessao_detalhada)
    return "<h1>Ops! Sessão não encontrada!</h1>"

@app.route("/palestrante/<int:id>")
def palestrante(id:int):
    for palestrante_detalhado in palestrante_detalhes:
        if palestrante_detalhado.id == id:
            return render_template("palestrante.html", palestrante = palestrante_detalhado)
    return "<h1>Ops! Palestrante não encontrado!</h1>"
