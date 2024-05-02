from flask import Flask, render_template
from lanche import Lanche

app = Flask(__name__)

pizza = Lanche(1, "Pizza", "R$18,00 reais", "2 ovos; 1 colher de chá rasa de sal; 1 colher de chá de fermento para bolo; 1/2 de xícara de chá de oléo de soja (100ml); 2 xícaras de chá de leite; 2 xícaras de chá de farinha de trigo sem fermento (240 gramas); 150g de molho de tomate; 250g de queijo mussarela; 200g de linguiça calabresa; orégano; azeitonas pretas;", "/static/img/pizza.jpg")

hamburguer = Lanche(2, "Hamburguer", "R$12,00 reais", "3kg de carne moída; 1 ovo; 30ml de água gelada; 300g de bacon; 3 colheres de sopa de farinha de trigo; 3 colheres de sopa de tempero caseiro;", "/static/img/hamb.jpg")

torta = Lanche(3, "Torta de Limão", "R$15,00 reais", "200g de biscoito de maisena; 150g de margarina; 1 lata de leite condensado (395g); 1 caixa de creme de leite (200g); suco de 4 limões; raspas de 2 limões; 3/4 claras de ovo; 3 colheres de sopa de açúcar; raspas de 2 limões para decorar;", "/static/img/torta.jpg")

lanche_catalogo = [pizza, hamburguer, torta]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/lanche-catalogo")
def catalogo_lanche():
    return render_template("catalogo-lanche.html", 
                            lanches = lanche_catalogo)

@app.route("/lanche/<int:id>")
def lanche(id:int):
    for lanche_do_catalogo in lanche_catalogo:
        if lanche_do_catalogo.id == id:
            return render_template("lanche.html", lanche = lanche_do_catalogo)
    return "<h1>Ops! Lanche não encontrado!</h1>"