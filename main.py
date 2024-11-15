
from openai import OpenAI


# config API
client = OpenAI(api_key="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")


# Read the text file with the article
with open("article.txt", "r", encoding="utf-8") as file:
    article_text = file.read()

# create prompt
prompt = (
    "Sformatuj poniższy artykuł w HTML. Użyj odpowiednich tagów nagłówków i akapitów, "
    "wstaw miejsca na dwie grafiki z <img src=\"image_placeholder.jpg\" alt=\"opis\"/> i podpisami "
    "pod nimi, używając tagu <figcaption>. Zwróć tylko zawartość do umieszczenia między "
    "<body> i </body>. Oto treść artykułu:\n\n" + article_text
)


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
         {"role": "user" , "content": prompt},
              ]
)

# Receive HTML and save to file
html_content = html_content = response.choices[0].message.content.strip()

with open("artykul.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

#Load template content
with open("szablon.html", "r", encoding="utf-8") as template_file:
    template = template_file.read()

#Insert the generated article content into the template inside <body>
podglad_content = template.replace("<body>", f"<body>\n{html_content}\n")

#Save the full preview to the preview.html file
with open("podglad.html", "w", encoding="utf-8") as preview_file:
    preview_file.write(podglad_content)

print("Pliki artykul.html i podglad.html zostały wygenerowane.")