from scripts.generate_script import generate_script
from scripts.generate_thumbnail_prompt import generate_thumbnail_prompt
from scripts.generate_metadata import generate_metadata

def run_automation():

    topic = input("Enter topic: ")

    generate_script(topic)
    generate_thumbnail_prompt(topic)
    generate_metadata(topic)

    print("\nAutomation complete.")
    print("Check output folder.")

if __name__ == "__main__":
    run_automation()
