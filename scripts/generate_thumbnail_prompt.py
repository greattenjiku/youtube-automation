import os
from config import OUTPUT_FOLDER

def generate_thumbnail_prompt(topic):

    prompt = f"""
Create a realistic YouTube Shorts thumbnail.

Topic: {topic}

Requirements:
– vertical 9:16
– shocked facial expression
– dramatic lighting
– bold large text
– breaking news style
– cinematic look
– high contrast
– ultra realistic
– high CTR design
"""

    filepath = os.path.join(OUTPUT_FOLDER, "thumbnail_prompt.txt")

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(prompt)

    print("Thumbnail prompt generated.")

    return prompt
