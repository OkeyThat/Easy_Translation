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

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolTip, QLabel, QTextEdit, QVBoxLayout
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class MyApp(QMainWindow):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      QToolTip.setFont(QFont('SansSerif', 10))

      self.lbl1 = QLabel('Enter your sentence:')
      self.te = QTextEdit()
      self.te.setAcceptRichText(False)
      self.lbl2 = QLabel('The number of words is 0')

      self.te.textChanged.connect(self.text_changed)

      vbox = QVBoxLayout()
      vbox.addWidget(self.lbl1)
      vbox.addWidget(self.te)
      vbox.addWidget(self.lbl2)
      vbox.addStretch()

      self.setLayout(vbox)

      btn = QPushButton('Copy', self)
      btn.setToolTip('This is a <b>Copy</b> Button')
      btn.move(50, 50)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(self.copyText)

      self.showStatusBar('wait...')

      self.setWindowTitle('Auto Translation')
      self.setGeometry(300, 300, 300, 200)
      self.show()
  
  def copyText(self):
      text = self.te.toPlainText()
      clipboard.copy(text)
      self.showStatusBar(text)

  def showStatusBar(self, status):
      text = status
      self.statusBar().showMessage(text)

  def text_changed(self):
      text = self.te.toPlainText()
      self.lbl2.setText('The number of words is ' + str(len(text.split())))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())