# TASK LIST SINGLE PAGE APPLICATION
Applicazione web, single page, dove l'utente può loggarsi con email e password e vedere i task assegnatogli. 
L' uttente può unicamente visualizzare i propri task e cliccando su un singolo task può vederne le note realtive.

### Tecnologie

* Python/Flask
* Vanilla JavaScript
* Css
* SQlite3

### Installazione e utilizzo

1. Installare Python.3 https://www.python.org/downloads/release/python-396/
2. Eseguire i seguenti step per Windows o macOS/Linux:
    * #### Windows
        1. Scaricare repository oppure clonarla
        2. cd repository
        3. py -3 -m venv venv
        4. venv\Scripts\activate
    
    * #### macOS/Linux
        1. Scaricare repository oppure clonarla
        2. $ cd repository
        2. $ python3 -m venv venv
        3. $ . venv/bin/activate

3. Ora vi troverete in un virtual environment dove potere installare Flask

4. Eseguire i seguenti comandi:
    * pip install Flask
    * pip install Flask-Session

5. Per eseguire l'applicazione eseguire ora il comando:
    * flask run

6. Potete controllare le funzionalità eseguendo il login con un utente. Per eseguire il login leggere la sezione Database.

7. Per uscire dal virtual environment basta eseguire il comando:
    * deactivate

## Database

Al momento ci sono presenti 10 utenti registrati con le seguenti email:

* prova@gmail.com
* pippo@gmail.com
* ciccio@gmail.com
* pluto@gmail.com
* paolo@gmail.com
* pietro@gmail.com
* giacomo@gmail.com
* paola@gmail.com
* federica@gmail.com
* felice@gmail.com

Le password d'accesso, sono la parte dello username della mail dell'utente, ripetuto 2 volte:

* Esempio:

    * email: pippo@gmail.com   password: pippopippo

    * email: federica@gmail.com   password: federicafederica


Per fare query al database, all'interno del virtual environment, eseguire: 

* sqlite3 db_users_tasks

Successivamente per vedere come è stato creato eseguire:

* .schema

Per uscire dal database eseguire:

* .quit



