import requests
import re

resp = requests.get('http://www.cgv.co.kr/movies/')

TitlePattern = re.compile(r'<strong class="title">([\w 가-힣 \:]*)')
PercentPattern = re.compile(r'<span>([\d\.]+\%)')
gradePattern = re.compile(r'<span class="percent">(\d+\%)')

text = resp.text
TitleList = re.findall(TitlePattern, text)
PercentList = re.findall(PercentPattern, text)
gradeList = re.findall(gradePattern, text)

print('\n' + '*' * 6 + 'CGV 영화 랭킹' + '*' * 6, end='\n\n')

for i in range(1, 8):
    print('NO' + str(i), '->', TitleList[i - 1], end='\n' + ' ' * 7)
    print('예매율 :', PercentList[i - 1] + ' , 평점 :', gradeList[i - 1])

print('\n')
