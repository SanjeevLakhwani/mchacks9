from selenium import webdriver
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from time import sleep
import pandas as pd

load_dotenv()

C_NAME, C_ID, INF = 0, 1, 2


def load_channels(file_path):
    data = pd.read_csv(file_path)
    return data.to_numpy()


def collect_data(channels):
    data = []
    for channel in channels:
        for title in collect_titles(channel[C_ID]):
            data.append([title, channel[C_NAME], channel[INF]])
    df = pd.DataFrame(data, columns=["video_title", "channel_name", "informative"])
    df.to_csv('video_data.csv', index=False)


def collect_titles(channel_id):
    driver = webdriver.Chrome()
    driver.get(f"https://www.youtube.com/{channel_id}/videos?view=0&sort=p&flow=grid")
    sleep(0.2)
    driver.execute_script("window.scrollBy(0,10000)", "")
    sleep(0.5)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    titles = soup.findAll('a', id='video-title')
    return [x.text for x in titles]


if __name__ == '__main__':
    channels = load_channels('channel_data.csv')
    collect_data(channels)
