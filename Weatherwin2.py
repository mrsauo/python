import sys
from PyQt5.QtWidgets import *
from WeatherWin import Ui_Form
import requests


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.clearBtn.clicked.connect(self.clearResult)
        self.ui.queryBtn.clicked.connect(self.queryWeather)

    def queryWeather(self):

        print('* queryWeather')
        cityName = self.ui.weatherComboBox.currentText()
        cityCode = self.transCityName(cityName)
        web = 'http://www.weather.com.cn/data/sk/' + cityCode + '.html'
        rep = requests.get(web)
        rep.encoding = 'utf-8'
        # print(rep.json())

        msg1 = '城市: %s' % rep.json()['weatherinfo']['city'] + '\n'
        msg2 = '风向: %s' % rep.json()['weatherinfo']['WD'] + '\n'
        msg3 = '温度: %s' % rep.json()['weatherinfo']['temp'] + '\n'
        msg4 = '风力: %s' % rep.json()['weatherinfo']['WS'] + '\n' + '度'
        msg5 = '湿度: %s' % rep.json()['weatherinfo']['SD'] + '\n'
        result = msg1 + msg2 + msg3 + msg4 + msg5
        self.ui.resultText.setText(result)

    def transCityName(self, cityName):
        cityCode = ''

        if cityName == '北京':
            cityCode = '101010100'
        elif cityName == '上海':
            cityCode = '101020100'
        elif cityName == '天津':
            cityCode = '101030100'
        elif cityName == '重庆':
            cityCode = '101040100'
        elif cityName == '哈尔滨':
            cityCode = '101050101'
        elif cityName == '长春':
            cityCode = '101060101'
        elif cityName == '沈阳':
            cityCode = '101070101'
        elif cityName == '呼和浩特':
            cityCode = '101080101'
        elif cityName == '石家庄':
            cityCode = '101090101'
        elif cityName == '太原':
            cityCode = '101100101'
        elif cityName == '西安':
            cityCode = '101110101'
        elif cityName == '济南':
            cityCode = '101120101'
        elif cityName == '乌鲁木齐':
            cityCode = '101130101'
        elif cityName == '拉萨':
            cityCode = '101140101'
        elif cityName == '西宁':
            cityCode = '101150101'
        elif cityName == '兰州':
            cityCode = '101160101'
        elif cityName == '银川':
            cityCode = '101170101'
        elif cityName == '郑州':
            cityCode = '101180101'
        elif cityName == '南京':
            cityCode = '101190101'
        elif cityName == '武汉':
            cityCode = '101200101'
        elif cityName == '杭州':
            cityCode = '101210101'
        elif cityName == '合肥':
            cityCode = '101220101'
        elif cityName == '福州':
            cityCode = '101230101'
        elif cityName == '南昌':
            cityCode = '101240101'
        elif cityName == '长沙':
            cityCode = '101250101'
        elif cityName == '贵阳':
            cityCode = '101260101'
        elif cityName == '成都':
            cityCode = '101270101'
        elif cityName == '广州':
            cityCode = '101280101'
        elif cityName == '昆明':
            cityCode = '101090101'
        elif cityName == '南宁':
            cityCode = '101300101'
        elif cityName == '海口':
            cityCode = '101310101'
        elif cityName == '香港':
            cityCode = '101320101'
        elif cityName == '澳门':
            cityCode = '101330101'
        elif cityName == '台北':
            cityCode = '101340101'
        return cityCode

    def clearResult(self):
        print('* clearResult')
        self.ui.resultText.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())