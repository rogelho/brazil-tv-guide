import requests
from bs4 import BeautifulSoup

class BrazilTV:

    def tv_content(self):

        baseURL = 'https://mi.tv/br/async/channel/'

        channelURL = f'{baseURL}/fox-life-hd/180'

        request = requests.get(channelURL)

        soup = BeautifulSoup(request.content, 'html.parser')

        scheduleHTML = soup.find_all('div', 'content')

        schedule = []

        for show in scheduleHTML:
            soup = BeautifulSoup(str(show), 'html.parser')
            program = {}
            program['show'] = soup.find('h2').text.strip()
            program['sub-title'] = soup.find('span', 'sub-title').string
            program['synopsis'] = soup.find('p', 'synopsis').string.strip()
            program['time'] = soup.find('span', 'time').string
            schedule.append(program)

        return schedule
