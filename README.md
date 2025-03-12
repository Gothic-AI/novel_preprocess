# Novel Text Preprocessing

This project focuses on preprocessing a raw text file (such as a novel) for use in natural language processing (NLP) tasks. The preprocessing pipeline includes several cleaning steps like removing metadata, splitting by chapters, removing special characters, and splitting the text into chunks for tokenization.

## Features
- **Remove Metadata**: Optionally removes metadata (e.g., Project Gutenberg metadata).
- **Split by Chapters**: Optionally splits the text into chapters and preserves chapter headings.
- **Remove Special Characters**: Removes non-ASCII characters from the text.
- **Text Chunking**: Splits the text into chunks based on a specified maximum word length, useful for NLP model training.
- **Text Normalization**: Optionally converts the entire text to lowercase.
- **Paragraph and Line Handling**: Maintains appropriate spacing between paragraphs, with no more than one empty line between them.

## Requirements

Ensure you have the following installed on your machine:

- Python 3.x
- `pip` (for installing Python packages)

### Required Libraries
- `PyYAML` for reading configuration files
- `re` for regular expression-based text processing (included with Python)

You can install the required libraries by running:

```bash
pip install -r requirements.txt
```

## Project Structure
.
├── config
│   └── config.yaml       # Configuration file for preprocessing
├── data
│   ├── raw
│   │   └── pg345.txt     # Raw text file (e.g., a novel)
│   └── processed
│       └── dracula_cleaned.txt   # Cleaned output after preprocessing
├── src
│   ├── preprocess.py     # Main preprocessing script
│   ├── utils.py          # Helper functions for text processing
│   └── config.yaml       # Configuration file (can be copied from config folder)
└── README.md             # Project documentation

## Configuration

The configuration for preprocessing is stored in a YAML file (`config/config.yaml`). The configuration file controls various preprocessing options such as cleaning and tokenization settings.

### Example `config.yaml`

```yaml
# Configuration for the preprocessing script
input_file: "data/raw/pg345.txt"  # Path to the raw text file
output_file: "data/processed/dracula_cleaned.txt"  # Path to save the cleaned text file
```

# Preprocessing settings
cleaning:
  remove_metadata: false  # Set to true to remove Project Gutenberg metadata
  split_by_chapters: true  # Set to true to split the text by chapters
  remove_special_characters: true  # Set to true to remove special characters
  lower_case: true  # Set to true to convert all text to lowercase
  split_paragraphs: true  # Set to true to split the text into paragraphs

# Tokenization settings
tokenization:
  max_length: 512  # Max word count per chunk
  batch_size: 8    # Batch size for tokenization
