from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Wagner TI</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }
            .menu { background-color: #0073e6; padding: 10px 0; text-align: center; }
            .menu a { color: white; text-decoration: none; margin: 0 15px; font-size: 18px; }
            .menu a:hover { text-decoration: underline; }
            .container { text-align: center; padding: 50px 20px; }
            h1 { color: #0073e6; }
            p { font-size: 18px; text-align: justify; }
            .main-content { margin: 40px auto; font-size: 16px; line-height: 1.5; width: 80%; max-width: 800px; text-align: justify; }
            footer {
                background-color: #0073e6;
                color: white;
                padding: 20px 10px;
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
            footer p { margin: 5px 0; font-size: 14px; }
        </style>
    </head>
    <body>
        <div class="menu">
            <a href="/">Home</a>
            <a href="/contato">Contato</a>
            <a href="/programas">Programas</a>
        </div>
        <div class="container">
            <h1>Bem-vindo ao Wagner TI</h1>
            <div class="main-content">
                <p>História de Wagner - Técnico de Informática e Futuro Analista de Sistemas</p>
                <p><a href="/contato" style="color: #0073e6; text-decoration: none;">Clique aqui para visitar a página de Contato!</a></p>
            </div>
        </div>
        <footer>
            <p><strong>WhatsApp:</strong> (66) 9 9982-4347</p>
            <p><strong>Endereço:</strong> Rua Centro, Nova Ubiratã - MT</p>
        </footer>
    </body>
    </html>
    """

@app.route("/contato")
def contato():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contato</title>
    </head>
    <body>
        <h1>Página de Contato</h1>
        <p>Entre em contato conosco:</p>
        <p>WhatsApp: (66) 9 9982-4347</p>
        <p>Email: wagnertimassocco@gmail.com</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)