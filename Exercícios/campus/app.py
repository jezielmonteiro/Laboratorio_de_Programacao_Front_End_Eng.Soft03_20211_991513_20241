from flask import Flask, render_template
from evento import Evento
from instalacao import Instalacao
from organizacao import Organizacao
from servico import Servico
from lanche import Lanche
from acesso import Acesso


app = Flask(__name__)

jornada_severino_sombra = Evento("XI Jornada Severino Sombra", "/static/img/jornada.png", "Data: 20/05/2024 - 24/05/2024", "Local: Universidade de Vassouras", "Palestrante: Jeziel Monteiro", "https://univassouras.edu.br/extensao/jornada-severino-sombra/")

gameficada = Evento("Gameficada", "/static/img/gameficada.png", "Data: 25/05/2024 - 29/05/2024", "Local: Arena Sombrão", "Palestrante: Felipe Soares", "https://linktr.ee/gameficada")

psicologia = Evento("Psicologia", "/static/img/psicologia.png", "Data: 30/05/2024 - 03/06/2024", "Local: Arena Sombrão", "Palestrante: Luiz Henrique", "https://univassouras.edu.br/graduacoes/psicologia/")

evento_detalhes = [jornada_severino_sombra, gameficada, psicologia]


biblioteca = Instalacao("Biblioteca Central", "/static/img/biblioteca.png", "Horário: 08:00 - 22:30", "Disponível", "Contato: (24) 2471-8200")

laboratorio = Instalacao("Laboratório de Programação Front-End", "/static/img/laboratorio.png", "Horário: 19:00 - 22:00", "Ocupado às terças-feiras", "Contato: (24) 2471-8200")

area_de_lazer = Instalacao("Cantina UniVassouras", "/static/img/cantina.png", "Horário: 08:00 - 22:30", "Disponível", "Contato: (24) 2471-8200")

instalacao_detalhes = [biblioteca, laboratorio, area_de_lazer]


aauev = Organizacao("AAUEV", "/static/img/aauev.png", "Associação Atlética Universitária das Engenharias de Vassouras", "28/04 (13:00) - Handebol Masculino (Med x Eng)", "04/05 (13:00) - Amistoso Vôlei (Barões x Famipe)", "05/05 (13:00) - Copa Náutico", "https://linktr.ee/atleticaengvassouras", "Novidade na área, lançamento no pedaço!!! O queridinho dos Barões, só que diferente… NOVO CORTA-VENTO DA ENGENHARIA!!!")

gameficada = Organizacao("Gameficada", "/static/img/gameficada.png", "Atlética de E-Sports da Universidade de Vassouras", "19/01 - Gameficada Kids", "10/03 - E-Sports Experience", "26/07 - Colônia de Férias (Gameficada Kids)", "https://linktr.ee/gameficada", "Para os alunos da Universidade de Vassouras dos cursos de Engenharia de Software e Análise e Desenvolvimento de Sistemas, oportunidade estágio presencial na Gameficada Univassouras. Interessados no estágio enviar currículo até Segunda-feira(04/03) para o e-mail: alvaro.leiroz@univassouras.edu.br")

unificada = Organizacao("Atlética Unificada UniVassouras Sombrão", "/static/img/unificada.png", "Unindo paixões, superando limites. Bem-vindo à nossa Atlética Unificada!", "24/04 - Vôlei Masculino", "07/05 - Super Copa", "20/07 - Futsal Feminino", "https://linktr.ee/atleticasombrao", "Continuamos firmes com a nossa ação em prol das vítimas das enchentes no Rio Grande do Sul, uma parceria do CAFF, das Atléticas da Universidade de Vassouras e da Prefeitura de Vassouras, para todos os que necessitam.")

organizacao_detalhes = [aauev, gameficada, unificada]


alimentacao = Servico("Alimentação", "/static/img/cantina.png", "Localização: Cantina UniVassouras", "Horário: 07:00 - 22:00", "http://127.0.0.1:5000/lanche-catalogo")

saude = Servico("Hospital Universitário de Vassouras", "/static/img/huv.jpg", "Localização: Rua Vicente Celestino, nº 201 - Madruga, Vassouras", "Horário: Aberto 24h por dia", "https://huv.univassouras.edu.br/")

segurança = Servico("Cadastro de Biometria", "/static/img/seguranca.jpg", "Localização: Laboratório 6 (Laboratório de Águas), Bloco 7, Térreo", "Horário: 08 a 19 de Abril - 08:30 às 21:30", "https://univassouras.edu.br/noticias/alunos-facam-o-cadastro-de-biometria-para-acesso-ao-campus-vassouras/")

servico_detalhes = [alimentacao, saude, segurança]


pizza = Lanche(1, "Pizza", "R$18,00 reais", "2 ovos; 1 colher de chá rasa de sal; 1 colher de chá de fermento para bolo; 1/2 de xícara de chá de oléo de soja (100ml); 2 xícaras de chá de leite; 2 xícaras de chá de farinha de trigo sem fermento (240 gramas); 150g de molho de tomate; 250g de queijo mussarela; 200g de linguiça calabresa; orégano; azeitonas pretas;", "/static/img/pizza.jpg")

hamburguer = Lanche(2, "Hamburguer", "R$12,00 reais", "3kg de carne moída; 1 ovo; 30ml de água gelada; 300g de bacon; 3 colheres de sopa de farinha de trigo; 3 colheres de sopa de tempero caseiro;", "/static/img/hamb.jpg")

torta = Lanche(3, "Torta de Limão", "R$15,00 reais", "200g de biscoito de maisena; 150g de margarina; 1 lata de leite condensado (395g); 1 caixa de creme de leite (200g); suco de 4 limões; raspas de 2 limões; 3/4 claras de ovo; 3 colheres de sopa de açúcar; raspas de 2 limões para decorar;", "/static/img/torta.jpg")

lanche_catalogo = [pizza, hamburguer, torta]


onibus = Acesso("Ônibus", "/static/img/onibus.png", "Horário: 18:30", "https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d3688.5414991909192!2d-43.66518012470431!3d-22.40863587960881!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e3!4m5!1s0x9924a8e645a585%3A0xc1280623a8e0d817!2sVassouras%2C%20Rio%20de%20Janeiro!3m2!1d-22.407650699999998!2d-43.6612124!4m5!1s0x9930cf7c22de05%3A0xc63f64f24c89cbf6!2sUniversidade%20de%20Vassouras%2C%20Av.%20Expedicion%C3%A1rio%20Osvaldo%20de%20Almeida%20Ramos%2C%20280%20-%20Centro%2C%20Vassouras%20-%20RJ%2C%2027700-000!3m2!1d-22.4092606!2d-43.664022599999996!5e0!3m2!1spt-BR!2sbr!4v1718121241536!5m2!1spt-BR!2sbr")

bicicletas = Acesso("Sistema de Compartilhamento de Bicicletas", "/static/img/bicicletas.png", "Horário: 18:30", "https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d3688.5135076824663!2d-43.665785175893866!3d-22.409690320292302!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e1!4m5!1s0x9924a8e645a585%3A0xc1280623a8e0d817!2sVassouras%2C%20Rio%20de%20Janeiro!3m2!1d-22.407650699999998!2d-43.6612124!4m5!1s0x9930cf7c22de05%3A0xc63f64f24c89cbf6!2sUniversidade%20de%20Vassouras%2C%20Av.%20Expedicion%C3%A1rio%20Osvaldo%20de%20Almeida%20Ramos%2C%20280%20-%20Centro%2C%20Vassouras%20-%20RJ%2C%2027700-000!3m2!1d-22.4092606!2d-43.664022599999996!5e0!3m2!1spt-BR!2sbr!4v1718122151320!5m2!1spt-BR!2sbr")

estacionamento = Acesso("Estacionamento 24h", "/static/img/estacionamento.png", "Horário: Aberto 24h", "https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d3688.5884331665166!2d-43.66370497589402!3d-22.40686777019369!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x9924a8e645a585%3A0xc1280623a8e0d817!2sVassouras%2C%20Rio%20de%20Janeiro!3m2!1d-22.407650699999998!2d-43.6612124!4m5!1s0x9930c6a9729b59%3A0xa69545d269e26856!2sRua%20Acad%C3%AAmica%20Eliete%20Nunes%20Barbosa%2C%2020%20-%20Centro%2C%20Vassouras%20-%20RJ%2C%2027700-000!3m2!1d-22.4060067!2d-43.661308299999995!5e0!3m2!1spt-BR!2sbr!4v1718122466015!5m2!1spt-BR!2sbr")

acesso_detalhes = [onibus, bicicletas, estacionamento]


@app.route("/")
def eventos():
    return render_template("eventos.html", eventos = evento_detalhes)

@app.route("/instalacoes")
def instalacoes():
    return render_template("instalacoes.html", instalacoes = instalacao_detalhes)

@app.route("/organizacoes")
def organizacoes():
    return render_template("organizacoes.html", organizacoes = organizacao_detalhes)

@app.route("/servicos")
def servicos():
    return render_template("servicos.html", servicos = servico_detalhes)

@app.route("/lanche-catalogo")
def catalogo_lanche():
    return render_template("catalogo-lanche.html", lanches = lanche_catalogo)

@app.route("/lanche/<int:id>")
def lanche(id:int):
    for lanche_do_catalogo in lanche_catalogo:
        if lanche_do_catalogo.id == id:
            return render_template("lanche.html", lanche = lanche_do_catalogo)
    return "<h1>Ops! Lanche não encontrado!</h1>"

@app.route("/transporte-e-acesso")
def acessos():
    return render_template("acesso.html", acessos = acesso_detalhes)