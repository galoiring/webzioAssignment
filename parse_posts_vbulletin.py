import requests
import re
import json
from datetime import datetime

# URL of the forum post
default_url = "https://forum.vbulletin.com/forum/vbulletin-3-8/vbulletin-3-8-questions-problems-and-troubleshooting/414325-www-vs-non-www-url-causing-site-not-to-login"
url = input("Please enter a vBulletin URL : ".format(
    default_url)) or default_url

# Fetching HTML content of the page
response = requests.get(url)
html_content = response.text

# Parse the HTML to find posts
post_pattern = r'<div class="b-post__userinfo-wrapper h-hide--on-preview">(.*?)<div class="b-post__footer h-hide--on-preview">'
posts = re.findall(post_pattern, html_content, re.DOTALL)

extracted_data = []

for post in posts:
    # Pattern to match title
    title_pattern = r'<h2 class="b-post__title js-post-title b-post__hide-when-deleted" itemprop="headline">\s*(.*?)\s*</h2>'
    title_match = re.search(title_pattern, post, re.DOTALL)
    title = title_match.group(1).strip() if title_match else ""

    # Pattern to match text content
    text_pattern = r'<div class="js-post__content-text restore h-wordwrap" itemprop="text">\s*(.*?)\s*<div class="h-flex-spacer h-margin-top-16">'
    text_match = re.search(text_pattern, post, re.DOTALL)
    text = re.sub(r'\s+', ' ', text_match.group(1).strip()
                  ) if text_match else ""

    # Remove the content inside <div class="bbcode_container">
    text = re.sub(r'<div class="bbcode_container">.*?</div>',
                  '', text, flags=re.DOTALL)

    # Remove the content inside <div class="bbcode_postedby">
    text = re.sub(r'<div class="bbcode_postedby">.*?</div>',
                  '', text, flags=re.DOTALL)

    # Remove any remaining HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Extract the publish date and time
    datetime_pattern = re.compile(
        r'<time itemprop="dateCreated" datetime=\'(.*?)\'>')
    datetime_match = re.search(datetime_pattern, post)
    publish_datetime = datetime_match.group(1) if datetime_match else ""

    # Format the publish date and time
    if publish_datetime:
        publish_datetime = datetime.strptime(
            publish_datetime, "%Y-%m-%dT%H:%M:%S%z")
        publish_datetime = publish_datetime.strftime("%Y/%m/%d %H:%M")
    else:
        publish_datetime = ""

    # Extract the author name
    author_pattern = re.compile(
        r'<span itemprop="name">(.*?)</span>', re.DOTALL)
    author_match = re.search(author_pattern, post)
    author_name = author_match.group(1) if author_match else ""

    extracted_info = {
        "title": title,
        "text": text,
        "published": publish_datetime,
        "author": author_name
    }

    extracted_data.append(extracted_info)

# Write the extracted data to a JSON file
with open('vbulletin_posts.json', 'w') as json_file:
    json.dump(extracted_data, json_file, indent=4)

print("\t- Extracted data has been written to extracted_data.json")
