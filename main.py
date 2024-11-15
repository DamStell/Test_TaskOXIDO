
from openai import OpenAI


# Konfiguracja API
client = OpenAI(api_key="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")


# Odczytaj plik tekstowy z artykułem
with open("article.txt", "r", encoding="utf-8") as file:
    article_text = file.read()

# Przygotuj prompt
prompt = (
    "Sformatuj poniższy artykuł w HTML. Użyj odpowiednich tagów nagłówków i akapitów, "
    "wstaw miejsca na grafiki z <img src=\"image_placeholder.jpg\" alt=\"opis\"/> i podpisami "
    "pod nimi, używając tagu <figcaption>. Zwróć tylko zawartość do umieszczenia między "
    "<body> i </body>. Oto treść artykułu:\n\n" + article_text
)


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
         {"role": "user" , "content": prompt},
              ]
)

# Odbierz HTML
html_content = html_content = response.choices[0].message.content.strip()
#Zapisz wygenerowany kod HTML do artykul.html 
with open("artykul.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("Plik artykul.html został wygenerowany.")