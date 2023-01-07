import sys
import subprocess

try:
    # 없는 모듈 import시 에러 발생
    import clipboard
except:
    # pip 모듈 업그레이드
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    # 에러 발생한 모듈 설치
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'clipboard'])
    # 다시 import
    import clipboard

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def copyText(self):
      text = 'Translation Word'
      clipboard.copy(text)

  def initUI(self):
      QToolTip.setFont(QFont('SansSerif', 10))

      btn = QPushButton('Copy', self)
      btn.setToolTip('This is a <b>Copy</b> Button')
      btn.move(50, 50)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(self.copyText)

      self.setWindowTitle('Auto Translation')
      self.setGeometry(300, 300, 300, 200)
      self.show()
  
  def copyText(self):
      text = 'Translation Word'
      clipboard.copy(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())