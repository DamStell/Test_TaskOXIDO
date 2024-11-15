# Projekt OpenAI HTML
## PL
## Opis 
Ten projekt łączy się z API OpenAI, aby przetworzyć tekst artykułu na HTML, zgodnie z wymaganiami strukturalnymi. Aplikcję rozszerzono o generację przy pomocy OpenAI obrazków powiązanych z tematyką artykułu

## Pliki
- `main.py`: Główny skrypt aplikacji.
- `article.txt`: Plik tekstowy z treścią artykułu.
- `artykul.html`: Wygenerowany plik HTML z kodem przetworzonym przez OpenAI.
- `szablon.html`: Szablon wykorzystwany przy tworzeniu podglądu artykułu
- `podglad.html`: podglad artyklu wraz z wygenerowanymi obrazkami
- `image_1` i `image_2`: wygenerowane obrazki
  
## Wymagania
- Python 3.x
- Biblioteka `openai`
- Biblioteka `requests`

## Instalacja
Zainstaluj bibliotekę OpenAI:
```bash
pip install openai
```
Zainstaluj bibliotekę Requests:
```bash
pip install requests
```
w pliku `main.py` w linii 6 `client = OpenAI(api_key="place on API KEY!!!")` wstaw swój API Key


## ENG
## Description
This project connects to the OpenAI API to process an article's text into HTML, following structural requirements. The application has been extended to include the generation of images related to the article's topic using OpenAI.
## Files
- `main.py`: The main application script.
- `article.txt`: A text file containing the article's conten
- `artykul.html`: The generated HTML file processed by OpenAI.
- `szablon.html`: The template used for creating the article preview.
- `podglad.html`:A preview of the article along with the generated images.
- - `image_1` i `image_2`: generated images.

## Requirements
- Python 3.x
- Biblioteka `openai`
- Biblioteka `requests`

## Instalation
Install the OpenAI library:
```bash
pip install openai
```
Install the Requests library:
```bash
pip install requests
```
in the file `main.py` on line 6 `client = OpenAI(api_key="place on API KEY!!!")` insert your API Key
