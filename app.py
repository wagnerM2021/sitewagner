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
                flex-direction: column;
                justify-content: center;
                align-items: center;
                position: relative;
                bottom: 0;
                width: 100%;
            }
            footer p {
                margin: 5px 0;
                font-size: 14px;
            }
            footer a {
                color: white;
                text-decoration: none;
                font-weight: bold;
            }
            footer a:hover {
                text-decoration: underline;
            }
            /* Botão flutuante */
            .floating-button {
                position: fixed;
                bottom: 20px;
                right: 20px;
                background-color: #0073e6;
                color: white;
                border: none;
                border-radius: 50%;
                width: 50px;
                height: 50px;
                text-align: center;
                font-size: 24px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
                cursor: pointer;
                z-index: 1000;
            }
            .floating-button:hover {
                background-color: #005bb5;
            }
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
                <p>Wagner sempre teve uma paixão natural pela tecnologia. Desde pequeno, era aquele amigo ou parente que todos procuravam quando um computador travava ou a internet caía. Movido por esse interesse, decidiu transformar seu talento em profissão: formou-se como Técnico de Informática, conquistando rapidamente seu espaço no mercado com sua dedicação e capacidade de resolver problemas de forma ágil e eficiente.</p>
                <p>Após alguns anos de atuação, Wagner sentiu a necessidade de aprofundar ainda mais seus conhecimentos. Buscando se diferenciar, concluiu uma pós-graduação, onde expandiu sua visão estratégica sobre TI, gestão de projetos e infraestrutura tecnológica.</p>
                <p>Atualmente, Wagner está cursando Desenvolvimento em Análise de Sistemas, mergulhando no universo da programação, engenharia de software e arquitetura de sistemas. Seu objetivo é claro: evoluir de técnico para um analista completo, capaz de não apenas corrigir problemas, mas de criar e planejar soluções tecnológicas inovadoras.</p>
                <p>Com uma trajetória marcada pela constante evolução, Wagner combina a experiência prática do suporte técnico com a visão analítica e de desenvolvimento de sistemas, caminhando para se tornar um profissional ainda mais completo e valorizado no setor de TI.</p>
            </div>
        </div>
        <footer>
            <p>&copy; 2025 Wagner TI. Todos os direitos reservados.</p>
            <p>Contato: <a href="mailto:wagnertimassocco@gmail.com">wagnertimassocco@gmail.com</a></p>
            <p>Endereço: Rua Centro, Nova Ubiratã - MT</p>
            <p><strong>WhatsApp:</strong> (66) 9 9982-4347</p>
        </footer>
        <!-- Botão flutuante para voltar -->
        <button class="floating-button" onclick="history.back()">&#8592;</button>
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
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                text-align: center;
                color: white;
                background-image: url('https://www.santanderopenacademy.com/pt_br/blog/Conhecimentos-de-informatica/_jcr_content/root/container/responsivegrid/image_1039111780.coreimg.jpeg/1711395641640/conhecimentos-de-informatica-2.jpeg');
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }
            .menu {
                background-color: #0073e6;
                padding: 10px 0;
                text-align: center;
                position: fixed;
                top: 0;
                width: 100%;
                z-index: 1000;
            }
            .menu a {
                color: white;
                text-decoration: none;
                margin: 0 15px;
                font-size: 18px;
            }
            .menu a:hover {
                text-decoration: underline;
            }
            .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: calc(100vh - 70px);
                padding: 20px;
                box-sizing: border-box;
                background-color: rgba(0, 0, 0, 0.5);
                margin-top: 50px;
            }
            .contact-box {
                width: 90%;
                max-width: 500px;
                background-color: rgba(255, 255, 255, 0.9);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
                text-align: left;
                color: #333;
            }
            .contact-box h1 {
                text-align: center;
                color: #0073e6;
                margin-bottom: 20px;
            }
            .contact-box p {
                font-size: 16px;
                margin: 10px 0;
            }
            footer {
                background-color: #0073e6;
                color: white;
                padding: 10px 0;
                text-align: center;
                position: relative;
                bottom: 0;
                width: 100%;
                margin-top: 20px;
            }
            footer p {
                font-size: 14px;
                margin: 5px 0;
            }
            footer a {
                color: white;
                text-decoration: none;
            }
            /* Botão flutuante */
            .floating-button {
                position: fixed;
                bottom: 20px;
                right: 20px;
                background-color: #0073e6;
                color: white;
                border: none;
                border-radius: 50%;
                width: 50px;
                height: 50px;
                text-align: center;
                font-size: 24px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
                cursor: pointer;
                z-index: 1000;
            }
            .floating-button:hover {
                background-color: #005bb5;
            }
        </style>
    </head>
    <body>
        <div class="menu">
            <a href="/">Home</a>
            <a href="/contato">Contato</a>
            <a href="/programas">Programas</a>
        </div>
        <div class="container">
            <div class="contact-box">
                <h1>Contato</h1>
                <p><strong>WhatsApp:</strong> (66) 9 9982-4347</p>
                <p><strong>Email:</strong> <a href="mailto:wagnertimassocco@gmail.com">wagnertimassocco@gmail.com</a></p>
                <p><strong>Endereço:</strong> Rua Centro, Nova Ubiratã - MT</p>
            </div>
        </div>
        <footer>
            <p>&copy; 2025 Wagner TI. Todos os direitos reservados.</p>
            <p>Contato: <a href="mailto:wagnertimassocco@gmail.com">wagnertimassocco@gmail.com</a></p>
        </footer>
        <!-- Botão flutuante para voltar -->
        <button class="floating-button" onclick="history.back()">&#8592;</button>
    </body>
    </html>
    """

@app.route("/programas")
def programas():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Programas</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; text-align: center; }
            .menu {
                background-color: #0073e6;
                padding: 10px 0;
                text-align: center;
                position: fixed;
                top: 0;
                width: 100%;
                z-index: 1000;
            }
            .menu a {
                color: white;
                text-decoration: none;
                margin: 0 15px;
                font-size: 18px;
            }
            .menu a:hover {
                text-decoration: underline;
            }
            h1 {
                color: #0073e6;
                margin-top: 70px; /* Adiciona espaço para o menu fixo */
            }
            .program-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
                padding: 20px;
            }
            .program-block {
                background-color: #ffffff;
                border: 1px solid #dddddd;
                border-radius: 8px;
                width: 300px;
                padding: 20px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                text-align: left;
            }
            .program-block h2 {
                font-size: 20px;
                color: #0073e6;
                margin-bottom: 10px;
            }
            .program-block p {
                font-size: 16px;
                color: #333333;
                margin-bottom: 10px;
            }
            .program-block a {
                color: #0073e6;
                text-decoration: none;
                font-weight: bold;
            }
            .program-block a:hover {
                text-decoration: underline;
            }
            footer {
                background-color: #0073e6;
                color: white;
                padding: 10px 0;
                text-align: center;
                margin-top: 20px;
                position: relative;
                bottom: 0;
                width: 100%;
            }
            footer p {
                font-size: 14px;
                margin: 5px 0;
            }
            /* Botão flutuante */
            .floating-button {
                position: fixed;
                bottom: 20px;
                right: 20px;
                background-color: #0073e6;
                color: white;
                border: none;
                border-radius: 50%;
                width: 50px;
                height: 50px;
                text-align: center;
                font-size: 24px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
                cursor: pointer;
                z-index: 1000;
            }
            .floating-button:hover {
                background-color: #005bb5;
            }
        </style>
    </head>
    <body>
        <div class="menu">
            <a href="/">Home</a>
            <a href="/contato">Contato</a>
            <a href="/programas">Programas</a>
        </div>
        <h1>Programas</h1>
        <div class="program-container">
            <div class="program-block">
                <h2>WinRAR</h2>
                <p>Ferramenta essencial para compactar e descompactar arquivos com eficiência.</p>
                <a href="https://www.win-rar.com/start.html?&L=10" target="_blank">Download</a>
            </div>
            <div class="program-block">
                <h2>Java Runtime Environment</h2>
                <p>Necessário para rodar aplicativos baseados em Java no seu computador.</p>
                <a href="https://www.java.com/pt-BR/download/" target="_blank">Download</a>
            </div>
            <div class="program-block">
                <h2>Google Chrome</h2>
                <p>Navegador rápido, seguro e amplamente utilizado para acessar a web.</p>
                <a href="https://www.google.com/intl/pt-BR/chrome/" target="_blank">Download</a>
            </div>
            <div class="program-block">
                <h2>Mozilla Firefox</h2>
                <p>Um navegador versátil e focado na privacidade do usuário.</p>
                <a href="https://www.mozilla.org/pt-BR/firefox/new/" target="_blank">Download</a>
            </div>
            <div class="program-block">
                <h2>Adobe Acrobat Reader</h2>
                <p>Visualize, edite e assine documentos PDF com facilidade.</p>
                <a href="https://get.adobe.com/br/reader/" target="_blank">Download</a>
            </div>
            <div class="program-block">
                <h2>AnyDesk</h2>
                <p>Conexão remota rápida e segura para assistência técnica.</p>
                <a href="https://anydesk.com/pt/downloads" target="_blank">Download</a>
            </div>
            <div class="program-block">
                <h2>Office 2019</h2>
                <p>Pacote completo de produtividade para criar documentos, planilhas e apresentações.</p>
                <a href="https://www.microsoft.com/pt-br/microsoft-365/previous-versions/microsoft-office-2019" target="_blank">Download</a>
            </div>
            <div class="program-block">
                <h2>Codec Pack</h2>
                <p>Pacote de codecs para suportar uma ampla variedade de formatos de áudio e vídeo.</p>
                <a href="https://codecguide.com/download_k-lite_codec_pack_standard.htm" target="_blank">Download</a>
            </div>
            <div class="program-block">
    <h2>Windows 10</h2>
    <p>Sistema operacional versátil e confiável para desktops e laptops.</p>
    <a href="https://www.microsoft.com/pt-br/software-download/windows10" target="_blank">Download</a>
</div>
<div class="program-block">
    <h2>Windows 11</h2>
    <p>A mais recente versão do Windows, com design moderno e novos recursos.</p>
    <a href="https://www.microsoft.com/pt-br/software-download/windows11" target="_blank">Download</a>
</div>
        </div>
        <footer>
            <p>&copy; 2025 Wagner TI. Todos os direitos reservados.</p>
            <p>Contato: <a href="mailto:wagnertimassocco@gmail.com" style="color:white; text-decoration:none;">wagnertimassocco@gmail.com</a></p>
            <p>Endereço: Rua Centro, Nova Ubiratã - MT</p>
        </footer>
        <!-- Botão flutuante para voltar -->
        <button class="floating-button" onclick="history.back()">&#8592;</button>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)