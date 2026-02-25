import os
from config import OUTPUT_FOLDER

def generate_metadata(topic):

    title = f"{topic} Just Changed Everything"

    description = f"""
{topic} explained in 30 seconds.

Subscribe for latest AI, geopolitics, and tech news.

Stay ahead of the world.
"""

    hashtags = "#ai #news #geopolitics #shorts #technology"

    metadata = f"""
TITLE:
{title}

DESCRIPTION:
{description}

HASHTAGS:
{hashtags}
"""

    filepath = os.path.join(OUTPUT_FOLDER, "metadata.txt")

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(metadata)

    print("Metadata generated.")

    return metadata
