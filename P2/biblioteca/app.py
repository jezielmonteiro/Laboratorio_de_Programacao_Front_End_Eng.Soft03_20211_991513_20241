from flask import Flask, render_template
from livro import Livro
from artigo import Artigo
from revista import Revista

app = Flask(__name__)

diario = Livro("Diário de um Banana 1", "/static/img/diario.png", "Autor(a): Jeff Kinney", "Categoria: Literatura e Ficção", "Indisponível", "https://www.amazon.com.br/Di%C3%A1rio-Um-Banana-Jeff-Kinney/dp/8576831309/ref=asc_df_8576831309/?tag=googleshopp00-20&linkCode=df0&hvadid=379792161032&hvpos=&hvnetw=g&hvrand=16550936599402866733&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001660&hvtargid=pla-811355936313&psc=1&mcid=af1c45e2538a3761a2e1ebac9272c1eb")

hp = Livro("Harry Potter e a Pedra Filosofal", "/static/img/hp.png", "Autor(a): J.K. Rowling", "Categoria: Fantasia, Literatura e Ficção", "Disponível", "https://www.amazon.com.br/Harry-Potter-Pedra-Filosofal-Rowling/dp/8532530788/ref=asc_df_8532530788/?tag=googleshopp00-20&linkCode=df0&hvadid=379795242161&hvpos=&hvnetw=g&hvrand=16550936599402866733&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001660&hvtargid=pla-569630960550&psc=1&mcid=c01261251f5d3ec6a254ec15d8074843")

principe = Livro("O Pequeno Príncipe", "/static/img/principe.png", "Autor(a): Antoine de Saint-Exupéry", "Categoria: Fantasia", "Disponível", "https://www.amazon.com.br/Pequeno-Pr%C3%ADncipe-Original-Tradu%C3%A7%C3%A3o-aquarelas/dp/8595081514/ref=asc_df_8595081514/?tag=googleshopp00-20&linkCode=df0&hvadid=379738402701&hvpos=&hvnetw=g&hvrand=9165173195747992057&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001660&hvtargid=pla-811743528218&psc=1&mcid=eeac449bf8be37bda5da451ae3d6b413")

livro_detalhes = [diario, hp, principe]


artigo1 = Artigo("Fluidodinâmica computacional da descarga marinha de solução hipersalina", "Autores: Levi de Brito Ximenes, Silvano Porto Pereira e Iran Eduardo Lima Neto", "Visando a uma alternativa ao abastecimento público de água, a Companhia de Água e Esgoto do Ceará lançou edital para implantação de uma planta de dessalinização. A solução hipersalina, rejeito do processo de dessalinização, será despejada no mar. Pela diferença de densidade entre os fluidos, o escoamento se divide em duas regiões: jato ascendente, com grande quantidade de movimento; e fonte descendente, onde o fluxo é governado pelo empuxo negativo.", "https://www.scielo.br/j/esa/a/d4FttzD5zyKysjdthkdkBVy/?lang=pt&format=pdf")

artigo2 = Artigo("Equações adimensionais para determinação de vazões máximas para diferentes tempos de retorno em regiões semiáridas", "Autores: Jefferson Sousa Rocha e Iran Eduardo Lima Neto", "Este trabalho elaborou modelos de regionalização para a obtenção de vazões máximas para períodos de retorno de 1.000 e 10.000 anos em barragens localizadas no Ceará. As variáveis empregadas nas equações foram: área de drenagem da bacia, comprimento do rio principal, tempo de concentração, precipitação com duração de uma hora e diferença de cota entre o exultório e o ponto mais remoto da bacia.", "https://www.scielo.br/j/esa/a/QxYhRYF7xmKyfH7JB6ZCLDb/?lang=pt&format=pdf")

artigo3 = Artigo("Aplicativo móvel: intervenções fisioterapêuticas à idosos frágeis", "Autores: Wagner Elias de Melo Moreira, Gustavo Detomi Rodrigues e Jorge Luiz de Carvalho Mello", "O objetivo deste estudo foi construir e validar um algoritmo e desenvolver um software do tipo aplicativo móvel para o diagnóstico multidimensional da vulnerabilidade clínico funcional e tratamento fisioterapêutico em idosos.", "https://www.scielo.br/j/fp/a/KbZj5PDmQVDqjXcmRsfQtyj/?lang=pt&format=pdf")

artigo_detalhes = [artigo1, artigo2, artigo3]


minecraft = Revista("Minecraft em Quadrinhos - Pro Games", "/static/img/minecraft.png", "Revista em quadrinhos do Minecraft.", "Data: 05/24", "Disponível", "https://revistasja.com.br/revista.php?id=47014&magazine_id=517")

guias = Revista("Guias de Guerras", "/static/img/guias.png", "Guias dedicados a contar a história das guerras que marcaram a história, bem como os assuntos relacionados.", "Data: 06/2024", "Disponível", "https://revistasja.com.br/revista.php?id=47715&magazine_id=502")

jornal = Revista("Plantio de milho nos EUA alcança 95% da área; 74% da safra tem condição boa ou excelente", "/static/img/jornal.png", "O plantio de milho nos Estados Unidos atingiu no último domingo 95% da área total prevista, avanço de 4 pontos porcentuais ante a semana anterior, informou o Departamento de Agricultura do país (USDA), em seu relatório semanal de acompanhamento de safra.", "Data: 11/06/2024", "Disponível", "https://www.jb.com.br/economia/agropecuaria/2024/06/1050430-plantio-de-milho-nos-eua-alcanca-95-da-area-74-da-safra-tem-condicao-boa-ou-excelente.html")

revistas_detalhes = [minecraft, guias, jornal]


@app.route("/")
def livros():
    return render_template("livros.html", livros = livro_detalhes)

@app.route("/artigos-científicos")
def artigos():
    return render_template("artigos.html", artigos = artigo_detalhes)

@app.route("/revistas-e-jornais")
def revistas():
    return render_template("revistas.html", revistas = revistas_detalhes)
