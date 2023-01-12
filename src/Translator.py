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

try:
    # 없는 모듈 import시 에러 발생
    import googletrans
except:
    # pip 모듈 업그레이드
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', 'googletrans==4.0.0-rc1', 'pip'])
    # 다시 import
    import googletrans

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolTip, QLabel, QTextEdit, QVBoxLayout
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class MyApp(QMainWindow):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      widget = QWidget(self)                # 위젯의 인스턴스 생성만으로도 QMainWindow에 붙는다.
      self.setCentralWidget(widget)    # 위젯이 QMainWindow 전체를 차지하게 된다

      QToolTip.setFont(QFont('SansSerif', 10))

      self.lbl1 = QLabel('Enter your sentence:')
      self.te = QTextEdit()
      self.te.setAcceptRichText(False)
      self.lbl2 = QLabel('The number of words is 0')

      self.te.textChanged.connect(self.text_changed)

      transBtn = QPushButton('Translate', self)
      transBtn.setToolTip('This is a <b>Translate</b> Button')
      transBtn.move(50, 50)
      transBtn.resize(transBtn.sizeHint())
      transBtn.clicked.connect(self.transText(self.te.toPlainText()))

      copyBtn = QPushButton('Copy', self)
      copyBtn.setToolTip('This is a <b>Copy</b> Button')
      copyBtn.move(50, 50)
      copyBtn.resize(copyBtn.sizeHint())
      copyBtn.clicked.connect(self.copyText)

      vbox = QVBoxLayout()
      vbox.addWidget(self.lbl1)
      vbox.addWidget(self.te)
      vbox.addWidget(self.lbl2)
      vbox.addWidget(transBtn)
      vbox.addWidget(copyBtn)
      vbox.addStretch()

      widget.setLayout(vbox)

      self.showStatusBar('wait...')

      self.setWindowTitle('Auto Translation')
      self.setGeometry(300, 300, 300, 200)
      self.show()
  
  def transText(self, inputText: str):
      translator = googletrans.Translator()
      result1 = translator.translate(inputText, dest='en')
      self.statusBar().showMessage(result1.text)

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