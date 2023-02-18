from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QVBoxLayout,QHBoxLayout,QLabel
from PyQt5.QtCore import QCoreApplication,QDate,Qt
from PyQt5.QtGui import QIcon
import requests
from urllib.request import urlopen
import pandas as pd
import numpy as np
import datetime as dt
import calendar
class Mainmenu(QMainWindow): 
    def get_day(y,m,d):
        days = ['월','화','수','목','금','토','일']
        return days[calendar.weekday(y, m ,d)]
    
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('')
        self.setWindowIcon(QIcon('bab.png'))
        self.setGeometry(300, 300, 640, 480)
        widget = QWidget()
        layout = QVBoxLayout()
        label1 = QLabel('오늘의 식당메뉴를 확인하세요!', self)
        label1.setAlignment(Qt.AlignCenter)
        font1 = label1.font()
        font1.setPointSize(15)
        font1.setFamily('D2Coding')
        font1.setBold(True)
        label1.setFont(font1)
        gongdaButton = QPushButton('공대식당',self)
       
        GPButton = QPushButton('감꽃푸드코트',self)
       
        welfareButton = QPushButton('복지관',self)

        quit_btn = QPushButton('나가기', self)
        quit_btn.resize(quit_btn.sizeHint())
        quit_btn.clicked.connect(QCoreApplication.instance().quit)
        layout.addWidget(label1)
        layout.addStretch(2)
        layout.addWidget(gongdaButton)
        layout.addStretch(1)
        layout.addWidget(GPButton)
        layout.addStretch(1)
        layout.addWidget(welfareButton)
        layout.addStretch(1)
        layout.addWidget(quit_btn)
        layout.addStretch(1)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        self.statusBar().showMessage('오늘의 날짜 : '+self.date.toString(Qt.DefaultLocaleLongDate))
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mainmenu()
    sys.exit(app.exec_())        
    
    
    
    # def choice(self):
    #     now = dt.datetime.today().weekday()
    #     nowdate = dt.datetime.today()
    #     nowdate
    #     print('금일은 {0}년 {1}월 {2}일 {3}요일입니다.'.format(nowdate.year, nowdate.month, nowdate.day, self.get_day(nowdate.year, nowdate.month, nowdate.day)))



print('-------메뉴 알리미--------')
print('교직원 식당을 선택해주세요')
print('1. 공대식당')
print('2. GP감꽃푸드코트')
print('3. 복지관 교직원식')

# def menu_print():
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QVBoxLayout,QHBoxLayout,QLabel
from PyQt5.QtCore import QCoreApplication,QDate,Qt
from PyQt5.QtGui import QIcon
import requests
from urllib.request import urlopen
import pandas as pd
import numpy as np
import datetime as dt
import calendar
res = 1
menu = []
now = dt.datetime.today().weekday()
now
if res ==1:
    res_num = 85
    html = urlopen(f'https://coop.knu.ac.kr/sub03/sub01_01.html?shop_sqno={res_num}')
    soup = BeautifulSoup(html.read(),'html.parser')
    x =  soup.select('tbody > tr > td> ul > li.first>p')
    for i in x:
        menu.append(i.text)
    menu = menu[:21:2]
    lunch_menu = menu[:5]
    dinner_menu = menu[5:]
elif res ==2:
    res_num = 46
    html = urlopen(f'https://coop.knu.ac.kr/sub03/sub01_01.html?shop_sqno={res_num}')
    soup = BeautifulSoup(html.read(),'html.parser')
    x =  soup.select('tbody > tr > td> ul > li.first >p')
    for i in x:
        menu.append(i.text)
    lunch_menu = menu[:11:2]
    
elif res ==3:
    res_num = 85
    html = urlopen(f'https://coop.knu.ac.kr/sub03/sub01_01.html?shop_sqno={res_num}')
    soup = BeautifulSoup(html.read(),'html.parser')
    x =  soup.select('tbody > tr > td> ul > li.first>p')
    for i in x:
        menu.append(i.text)
    lunch_menu = menu[:11:2]

print(f'오늘 점심메뉴 : \n{lunch_menu[now]}')
print(f'오늘 저녁메뉴 : \n{dinner_menu[now]}')



# nowdate = dt.datetime.strptime(now, "%Y%m%d")
# nowdate
# np.datetime64('today','D')

# start_date= soup.select_one('span.fb').text.strip()[0:10]
# end_date= soup.select_one('span.fb').text.strip()[13:23]
# start_date = dt.datetime.strptime(start_date,'%Y-%m-%d')
# end_date= dt.datetime.strptime(end_date,'%Y-%m-%d')
# if start_date <= nowdate <= end_date:
#     print('t')
# now

# end_date+dt.timedelta(1)

