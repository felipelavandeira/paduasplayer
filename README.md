# INSTRUÇÕES #

### Para desenvolver o programa, é necessário: ###

Instalar a lib Flask, ,com o comando:
* pip3 install flask
* pip3 install pyrebase
* pip3 install pygame

### Se estiver no Windows ###

* Abrir o Prompt do comando, e navegar até a pasta do projeto através dele (comando cd)
* Quando estiver na pasta raíz do projeto, rodar o seguinte comando:
* * set FLASK_APP=main.py
* Depois de configurar a variável de ambiente, utilizar o seguinte comando:
* * python3 -m flask run
* Seu projeto estará rodando no servidor de deploy, no endereço [http://localhost:5000](http://localhost:5000)

### Se você estiver no Linux ###

* Navegue até a pasta do projeto com o terminal
* Digite o comando:
* * export FLASK_APP=main.py
* Depois de configurar a variável de ambiente, utilizar o seguinte comando:
* * python3 -m flask run
* Seu projeto estará rodando no servidor de deploy, no endereço [http://localhost:5000](http://localhost:5000)

# Para ouvir as músicas #
Basta criar na raíz do projeto a pasta *"musics"* e colocar suas músicas no formato .mp3 dentro dela

# Para parar a reprodução  #
Basta clicar no botão limpar playlist ![](https://github.com/felipelavandeira/paduasplayer/blob/master/Views/assets/images/iconfinder_music_103634xx.png | width=100)