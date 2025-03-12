import re
import yaml

# Load configuration from YAML
def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


# Example cleanup functions
def clean_metadata(text):
    # Remove Project Gutenberg metadata or other unwanted text
    return text.split("***")[0]

def split_by_chapters(text):
    # Split text by chapter markers like 'CHAPTER I', 'CHAPTER II', etc.
    # Ensure chapter markers are preserved as-is
    chapters = re.split(r'(CHAPTER [IVXLCDM]+)', text)  # Match "CHAPTER" followed by Roman numerals
    # Filter out any empty strings and join the chapters back
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]
    return chapters

def remove_special_characters(text):
    # Remove special characters but preserve chapter markers like 'CHAPTER I', 'CHAPTER II', etc.
    # We need to be careful not to remove the "CHAPTER" word and its Roman numeral
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII characters
    return text

def split_paragraphs(text):
    # Split text into paragraphs by detecting double newlines
    return text.split("\n\n")

def chunk_text(text, max_length):
    # Ensure that text is a string and not a list
    if isinstance(text, list):
        # Join the list back into a string
        text = "\n\n".join(text)
    
    # Split the text into paragraphs by double newlines
    paragraphs = split_paragraphs(text)
    
    chunks = []
    
    # Process each paragraph
    for para in paragraphs:
        para = re.sub(r'\s+', ' ', para).strip()  # Replace multiple spaces with a single space and trim
        
        # Split the paragraph into words
        words = para.split()
        
        current_chunk = []
        
        for word in words:
            current_chunk.append(word)
            # Check if the chunk exceeds the max_length (by word count)
            if len(current_chunk) >= max_length:
                # If it exceeds, push the current chunk and start a new one
                chunks.append(" ".join(current_chunk))
                current_chunk = []  # Start a new chunk
        
        # Add the last chunk if it has any remaining words
        if current_chunk:
            chunks.append(" ".join(current_chunk))
    
    # Join all chunks with exactly one empty line between paragraphs
    return "\n\n".join(chunks).strip()
