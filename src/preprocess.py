import re
import os
from pathlib import Path
from utils import load_config, clean_metadata, split_by_chapters, remove_special_characters, split_paragraphs, chunk_text


# Preprocess the text based on configuration
def preprocess_text(input_file, output_file, config):
    # Read the raw text
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Clean the text based on the config
    if config['cleaning'].get('remove_metadata', False):
        text = clean_metadata(text)

    if config['cleaning'].get('split_by_chapters', False):
        chapters = split_by_chapters(text)  # This might return a list
        text = "\n\n".join(chapters)  # Join the list back into a single string

    if config['cleaning'].get('remove_special_characters', False):
        text = remove_special_characters(text)

    if config['cleaning'].get('lower_case', False):
        text = text.lower()

    if config['cleaning'].get('split_paragraphs', False):
        text = split_paragraphs(text)

    # Chunk text based on max_length
    max_length = config['tokenization'].get('max_length', 512)
    text = chunk_text(text, max_length)

    # Save the cleaned text
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"Preprocessing complete. Cleaned text saved to {output_file}")



if __name__ == "__main__":
    # Load configuration
    config = load_config('config/config.yaml')

    # Preprocess the novel text
    preprocess_text(config['input_file'], config['output_file'], config)
