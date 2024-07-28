import requests
import re
import json
import csv


# Step 1: Read the HTML file
with open('lessonsHtml.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Step 2: Use Regular Expression to find video IDs
# The pattern looks for "_wq.push({" followed by a sequence of characters that do not include quotes, which is our video ID, followed by "\":"
pattern = r'_wq\.push\(\{"([^"]+)":'
video_ids = re.findall(pattern, html_content)




# Step 3: Print or store the IDs
print(video_ids)


def fetch_thumbnail_url(video_id):
    # Construct the URL with the given video ID
    url = f"https://fast.wistia.net/embed/iframe/{video_id}"

    # Make a GET request to fetch the page content
    response = requests.get(url)
    if response.status_code == 200:
        # Simplified regular expression
        match = re.search(r'"type":"original".*?"url":"(https://embed-ssl.wistia.com/deliveries/[^"]+\.bin)"', response.text)
        if match:
            return match.group(1)  # Directly return the URL from the regex match


# "assets":[{"type":"original","slug":"original","display_name":"Original File","details":{},"width":1920,"height":1080,"ext":"","size":707221753,"bitrate":9807,"public":true,"status":2,"progress":1.0,"metadata":{"av_stream_metadata":"{\"Video\":{\"codec\":\"h264\",\"colorPrimaries\":\"bt709\",\"colorSpace\":\"bt709\",\"colorTransfer\":\"bt709\",\"pixelFormat\":\"yuv420p\",\"rFrameRate\":\"30/1\",\"avgFrameRate\":\"30/1\"}}"},"url":"https://embed-ssl.wistia.com/deliveries/d3c91f977ef6eff8d934399eaef4dfe9.bin","created_at":1686863857},



for video_id in video_ids:
    thumbnail_url = fetch_thumbnail_url(video_id)
    if thumbnail_url:
        print(f"Thumbnail URL for video {video_id}: {thumbnail_url}")
    else:
        print(f"Failed to fetch thumbnail URL for video {video_id}")


# save video links to a csv file


with open('video_links.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Video ID", "Thumbnail URL"])
    for video_id in video_ids:
        thumbnail_url = fetch_thumbnail_url(video_id)
        writer.writerow([video_id, thumbnail_url])

