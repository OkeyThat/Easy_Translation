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
      transBtn.clicked.connect(self.transText)

      copyBtn = QPushButton('Copy', self)
      copyBtn.setToolTip('This is a <b>Copy</b> Button')
      copyBtn.move(50, 50)
      copyBtn.resize(copyBtn.sizeHint())
      copyBtn.clicked.connect(self.copyText)

      newWindowBtn = QPushButton('create Window', self)
      newWindowBtn.clicked.connect(self.dialog_open)
    
      dialog = QDialog()
    
      vbox = QVBoxLayout()
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
      btnDialog = QPushButton('close',self.dialog)
      btnDialog.move(100,100)
      btnDialog.cliked.connect(self.dialog_close)

      self.dialog.setWindowTitle('Dialog')
      self.dialog.setWindowModality(Qt.ApplicationModal)
      self.dialog.resize(300,200)
      self.dialog.show()


  def dialog_close(self):
      self.dialog.close()

  def transText(self):
      translator = googletrans.Translator()
      if len(self.te.toPlainText().split()) > 0:
        result1 = translator.translate(self.te.toPlainText(), dest='en')
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())