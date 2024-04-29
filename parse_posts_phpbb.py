import re
import requests
from datetime import datetime


default_url = "http://www.phpbb.com/community/viewtopic.php?f=46&t=2159437"
url = input("Please enter a phpbb URL (default: {}): ".format(
    default_url)) or default_url

response = requests.get(url)
html_content = response.text

# Pattern to match post divs
post_pattern = r'<div class="postbody.*?">(.*?)<div class="back2top">'
posts = re.findall(post_pattern, html_content, re.DOTALL)
output = []

for post in posts:
    # Pattern to match title
    title_pattern = r'<a\b[^>]*>(.*?)</a>'
    title_match = re.search(title_pattern, post)
    title = title_match.group(1) if title_match else ""

    # Pattern to match text content
    text_pattern = r'<div class="content">\s*(.*)\s*'
    text_match = re.search(text_pattern, post)
    text = text_match.group(1).strip() if text_match else ""

    # Remove <img> tag from the text
    text = re.sub(r'<img[^>]*>', '', text)

    # text = re.sub(r'<blockquote>.*?</blockquote>',
    #               '', text, flags=re.DOTALL)
    text = re.sub(r'<.*?>', '', text)

    # Pattern to match published date and time
    datetime_pattern = r'<time datetime="(.*?)\+.*?">(.*?)</time>'
    datetime_match = re.search(datetime_pattern, post, re.DOTALL)
    published_datetime = datetime_match.group(1) if datetime_match else ""
    published = datetime.strptime(
        published_datetime, "%Y-%m-%dT%H:%M:%S").strftime("%Y/%m/%d %H:%M")

    # Pattern to match author
    author_pattern = r'<span class="responsive-hide">by <strong><a href=".*?" class="username.*?">(.*?)</a></strong>'
    author_match = re.search(author_pattern, post, re.DOTALL)
    author = author_match.group(1) if author_match else ""

    json_obj = {
        "title": title,
        "text": text.strip(),
        "published": published,
        "author": author
    }
    output.append(json_obj)


# Write output to JSON file
with open("phpbb_posts.json", "w", encoding="utf-8") as file:
    import json
    json.dump(output, file, indent=4, ensure_ascii=False)

print("\t- Extracted data has been written to page1_posts.json")
