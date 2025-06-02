from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    diagnostico = None

    if request.method == 'POST':
        r1 = request.form.get('internet')
        r2 = request.form.get('lento')
        r3 = request.form.get('estranhas')
        r4 = request.form.get('reiniciou')

             
        if r1 == 'nao':
            diagnostico = "Verifique se o cabo de rede está conectado ou tente reiniciar o modem."
        elif r2 == 'sim' and r3 == 'sim':
            diagnostico = "Pode ser vírus. Faça uma varredura com um antivírus confiável."
        elif r2 == 'sim':
            diagnostico = "Reinicie o computador e feche programas desnecessários."
        elif r4 == 'nao':
            diagnostico = "Tente reiniciar o computador. Isso resolve muitos problemas."
        else:
            diagnostico = "Não foi possível identificar o problema. Contate o suporte técnico."

    return render_template('index.html', diagnostico=diagnostico)

if __name__ == '__main__':
    app.run(debug=True)