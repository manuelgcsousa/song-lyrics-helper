# Song Lyrics Helper

Song Lyrics Helper is a song lyrics editor that uses a similar process to Pat Pattison's methodology. It builds a list of 10 words related to the song's theme, and finds related and rhyming words.

It is available as a command line tool and a web application. Both use the same resources.

## Installation

An installation script is provided, which takes care of dependencies.

NOTE: one of the dependencies requires a manual install, as specified in the script - *wkhtmltopdf*.

```bash
./install.sh
```

After that, we can navigate to "src/cmd-app/" to use the command line app, or "src/web-app/" to start the web application using flask.

## Usage

### Command Line App

The tool, as explained executing './main.py -h', can produce different outputs which the user can extract the results from.

```bash
./main.py -h

    Programa que dada uma lista de palavras trata de construir
    um dicionário contendo rimas e palavras similares.

    => FLAGS:
       -o -> Indica o formato \do output (json || html || pdf);
       -l -> Indica a língua (pt || en);
       -w -> Indica que seguidamente se apresentam palavras.

       Ex.: ./main.py -o html -l pt -w cão gato sapato
```

- **JSON**
  
  - When the output is JSON, a dictionary is written is a JSON file, allowing the user to work with that file.

- **HTML**
  
  - When selecting HTML, static pages are generated (using stylesheets) that allow the user to navigate through the generated dictionary.

- **PDF**
  
  - Generates a document with all the information built. In this version of the tool, there is not a summary of the song (unlike the web-app).

### Web Application

The web application uses a flask server to support the incomming request from the user. With the available frontend, the user is able to write the song's summary, and from that, the tool extract keywords. After that, the user can add new words or delete existing ones. Finally, a generate button can be clicked, which takes care of generating a pdf file containing all the information extracted.

To start the web application simply type the following command inside "src/webapp/". This will start the server:

```bash
./app.py
```

## External API's

Song lyrics helper uses external API's to extract related and rhyming words (both to Portuguese and English languages).

- **Portuguese**
  
  - [Rhymit](https://www.rhymit.com)
  
  - [Lexico](https://www.lexico.pt)
  
  It is important to notice that none of this services are available as API's. The process of extracting words was done by applying *web scrapping*.

- **English**
  
  - https://api.datamuse.com/words
  
  The [Datamuse](https://www.datamuse.com/) API is a **word-finding** query engine for developers. With a simple query string, we could retrieve various information about a certain word.

&nbsp;

&nbsp;

&nbsp;

*University Project - Scripting no Processamento de Linguagem Natural, Universidade do Minho (2018-2019)*
