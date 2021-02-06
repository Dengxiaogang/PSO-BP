
from PSOBPnetdemo01MideFile import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import pyqtgraph as py


if __name__ == '__main__':
    app = QApplication(sys.argv )
    dlg =MidFile('PSO-BP神经网络油墨预测模型')

    dlg.show()      
    sys.exit(app.exec_())

