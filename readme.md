# Webzio Assignment

# Web Forum Post Extractor

This project provides Python scripts to extract posts from web forums, specifically vBulletin and phpBB forums. The scripts parse the HTML content of the forum pages and extract relevant information such as post titles, text content, published date and time, and author names. The extracted data is then saved in JSON format for further processing or analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [vBulletin Post Extractor](#vbulletin-post-extractor)
  - [phpBB Post Extractor](#phpbb-post-extractor)
- [Output](#output)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/webzioAssignment.git
   ```

2. Navigate to the project directory:

   ```
   cd webzioAssignment
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### vBulletin Post Extractor

1. Run the `parse_posts_vbulletin.py` script:

   ```
   python parse_posts_vbulletin.py
   ```

2. Enter the URL of the vBulletin forum thread when prompted. If no URL is provided, the default URL will be used.

3. The script will fetch the HTML content of the forum page, extract the relevant post information, and save it in the `vbulletin_posts.json` file.

### phpBB Post Extractor

1. Run the `parse_posts_phpbb.py` script:

   ```
   python parse_posts_phpbb.py
   ```

2. Enter the URL of the phpBB forum thread when prompted. If no URL is provided, the default URL will be used.

3. The script will fetch the HTML content of the forum page, extract the relevant post information, and save it in the `phpbb_posts.json` file.

## Output

The extracted post information will be saved in JSON format in the respective output files:

- `vbulletin_posts.json` for vBulletin forum posts
- `phpbb_posts.json` for phpBB forum posts

Each JSON file will contain an array of post objects with the following properties:

- `title`: The title of the post
- `text`: The text content of the post
- `published`: The published date and time of the post
- `author`: The author name of the post

## Dependencies

The project relies on the following dependencies:

- `requests`: For making HTTP requests to fetch the forum pages
- `re`: For using regular expressions to parse the HTML content
- `json`: For saving the extracted data in JSON format
- `datetime`: For handling date and time formatting

These dependencies are listed in the `requirements.txt` file and can be installed using `pip`.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
