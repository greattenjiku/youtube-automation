import os
from config import OUTPUT_FOLDER, SCRIPT_STYLE, VIDEO_DURATION

def generate_script(topic):

    script = f"""
HOOK:
This just changed everything about {topic}.

BODY:
Here is what’s happening.
{topic} is creating massive global impact right now.
Most people don’t know the real reason behind this.

This could affect millions.

ENDING:
The next few days are critical.
Follow now to stay ahead.

STYLE: {SCRIPT_STYLE}
DURATION: {VIDEO_DURATION}
"""

    filepath = os.path.join(OUTPUT_FOLDER, "script.txt")

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(script)

    print("Script generated successfully.")

    return script
