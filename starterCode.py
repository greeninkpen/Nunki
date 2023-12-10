from openai import OpenAI
import requests
from PIL import Image
import io
import random

# Replace YOUR_API_KEY with your OpenAI API key
client = OpenAI(api_key="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")

size = "1024x1024"
quality = "standard"
sentence_template = "A {} cat with a hat on."
word_choices = ["cute", "a", "cat", "black"]
log_filename = "image_log.txt"

with open(log_filename, "w") as log_file:
    log_file.write("Image Log:\n")

    correct_word = random.choice(word_choices)
    user_choices = random.sample(word_choices, k=len(word_choices))
    random.shuffle(user_choices)

    print(f"Complete the sentence: '{sentence_template}'")
    print("Choose the correct word order:")
    for i, choice in enumerate(user_choices, start=1):
        print(f"{i}. {choice}")

    user_selection = input("Put the words in the correct order (e.g., '1234'): ")

    if user_selection.isdigit() and len(user_selection) == len(user_choices):
        selected_words = [user_choices[int(index) - 1] for index in user_selection]
        completed_sentence = sentence_template.format(" ".join(selected_words))

        response = client.images.generate(
            model="dall-e-3",
            prompt=completed_sentence,
            size=size,
            quality=quality,
            n=1,
        )

        if response.data:
            image_content = requests.get(response.data[0].url).content
            image_filename = f"image.png"
            Image.open(io.BytesIO(image_content)).save(image_filename)
            print(f"Image saved to '{image_filename}'")

            log_file.write(f"{completed_sentence}\t{image_filename}\n")
        else:
            print("Error generating image.")
    else:
        print("Invalid input. Please enter the correct numbers for word order.")