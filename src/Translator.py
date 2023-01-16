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

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolTip, QLabel, QTextEdit, QVBoxLayout, QDialog
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QFont, QMouseEvent, QCursor

class MyApp(QMainWindow):

  def __init__(self):
      super().__init__()
      self.initUI()
      self.transResultText = ''

  def initUI(self):
      widget = QWidget(self)                # 위젯의 인스턴스 생성만으로도 QMainWindow에 붙는다.
      self.setCentralWidget(widget)    # 위젯이 QMainWindow 전체를 차지하게 된다
      self.setWindowFlags(Qt.WindowStaysOnTopHint)

      QToolTip.setFont(QFont('SansSerif', 10))

      x = 0
      y = 0

      self.text = 'x: {0}, y: {1}'.format(x, y)
      self.label = QLabel(self.text, self)
      self.label.move(20, 20)

      self.setMouseTracking(True)

        
      self.lbl1 = QLabel('Enter your sentence:')
      self.te = QTextEdit()
      self.te.setAcceptRichText(False)
      self.lbl2 = QLabel('The number of words is 0')

      self.te.textChanged.connect(self.text_changed)

      transBtn = QPushButton('Translate', self)
      transBtn.setToolTip('This is a <b>Translate</b> Button')
      transBtn.resize(transBtn.sizeHint())
      transBtn.clicked.connect(self.transText)

      copyBtn = QPushButton('Copy', self)
      copyBtn.setToolTip('This is a <b>Copy</b> Button')
      copyBtn.resize(copyBtn.sizeHint())
      copyBtn.clicked.connect(self.copyText)

      newWindowBtn = QPushButton('create Window', self)
      newWindowBtn.clicked.connect(self.dialog_open)
    
      self.dialog = QDialog()
    
      vbox = QVBoxLayout()
      vbox.addWidget(self.label)
      vbox.addWidget(self.lbl1)
      vbox.addWidget(self.te)
      vbox.addWidget(self.lbl2)
      vbox.addWidget(transBtn)
      vbox.addWidget(copyBtn)
      vbox.addWidget(newWindowBtn)
      vbox.addStretch()

      widget.setLayout(vbox)

      self.showStatusBar('wait...')

      self.setWindowTitle('Auto Translation')
      self.setGeometry(300, 300, 300, 200)
      self.show()
  
  def dialog_open(self):
      btnText = 'close'
      if len(self.transResultText) > 0:
          btnText = self.transResultText

      btnDialog = QPushButton(btnText, self.dialog)
      btnDialog.setToolTip('This is a <b>Copy</b> Button')
      btnDialog.clicked.connect(self.dialog_close)

      self.dialog.setWindowModality(Qt.ApplicationModal)
      self.dialog.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
      self.dialog.setStyleSheet("background-color : rgba(255, 255, 255, 100)") 
      self.dialog.resize(btnDialog.sizeHint())
      self.dialog.show()

  def dialog_close(self):
      self.dialog.close()

  def transText(self):
      translator = googletrans.Translator()
      if len(self.te.toPlainText().split()) > 0:
        result1 = translator.translate(self.te.toPlainText(), dest='en')
        self.transResultText = result1.text
        self.statusBar().showMessage(result1.text)
      else:
        self.statusBar().showMessage('none Text')

  def copyText(self):
      text = self.statusBar().currentMessage()
      clipboard.copy(text)

  def showStatusBar(self, status):
      text = status
      self.statusBar().showMessage(text)

  def text_changed(self):
      text = self.te.toPlainText()
      self.lbl2.setText('The number of words is ' + str(len(text.split())))

  def mousePressEvent(self, e):
      x = e.x()
      y = e.y()

      text = 'x: {0}, y: {1}'.format(x, y)
      self.label.setText(text)
      self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())