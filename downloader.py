import csv
import requests
from tqdm import tqdm

def download_video(url, video_id):
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc=f"Downloading {video_id}")

    with open(f"videos/{video_id}.mp4", "wb") as file:
        for data in response.iter_content(chunk_size=1024):
            progress_bar.update(len(data))
            file.write(data)
        progress_bar.close()

    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print(f"ERROR, something went wrong with {video_id}")

def main():
    with open('video_links.csv', mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            download_video(row['Thumbnail URL'], row['Video ID'])

if __name__ == "__main__":
    main()