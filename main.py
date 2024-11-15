
from openai import OpenAI
import requests

# config API
client = OpenAI(api_key="place on API KEY!!!")


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

# picture prompts
image_prompts = [
    "Ilustracja związana z głównym tematem artykułu:" + article_text,
    "Infografika przedstawiająca kluczowe dane lub fakty z artykułu:" + article_text
]

# Generate images and save them locally
image_paths = []
for i, promptImage in enumerate(image_prompts, 1):
    response_image = client.images.generate(
        model="dall-e-3",
        prompt=promptImage,
        n=1,
        size="1024x1024",
        response_format="url" 
    )
    
    image_url = response_image.data[0].url
    image_data = requests.get(image_url).content
    image_path = f"image_{i}.jpg"
    with open(image_path, "wb") as image_file:
        image_file.write(image_data)
    image_paths.append(image_path)

# Loading a template and generating a preview
with open("szablon.html", "r", encoding="utf-8") as template_file:
    template = template_file.read()

for i, image_path in enumerate(image_paths, 1):
    #replace the places of "image_placeholder.jpg" with the actual image paths
    html_content = html_content.replace(f"image_placeholder.jpg", image_path, 1)

# Save the final preview to the preview.html file
podglad_content = template.replace("<body>", f"<body>{html_content}")
with open("podglad.html", "w", encoding="utf-8") as preview_file:
    preview_file.write(podglad_content)
print("Pliki artykul.html i podglad.html zostały wygenerowane.")