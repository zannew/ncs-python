from bs4 import BeautifulSoup
from urllib.request import urlopen

class Bugsmusic:

    url = ''

    def scrap(self):
        url = urlopen(self.url)
        soup = BeautifulSoup(url, 'lxml')
        cnt_artist = 0
        cnt_title = 0

        for link1 in soup.find_all(name="p", attrs=({"class":"artists"})):
            cnt_artist += 1
            print(str(cnt_title)+" 위")
            print("아티스트 : " + link1.find('a').text)
        print('---------------------------------------')

        for link2 in soup.find_all(name="p", attrs=({"class": "title"})):
            cnt_title += 1
            print(str(cnt_title) + "위")
            print("노래제목" + link2.text)


    @staticmethod
    def main():
        bugs = Bugsmusic()
        bugs.url = 'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210508&charthour=12'
        bugs.scrap()


if __name__ == '__main__':
    Bugsmusic.main()