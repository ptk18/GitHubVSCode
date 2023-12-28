import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, _):
        p = QPainter()
        p.begin(self)
        
        # draw carrot leaf
        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])
        
        # draw apple body
        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(220,20,60))
        #p.drawPie(50, 150, 100, 100, 0, 180*16)
        p.drawEllipse(QRect(25, 150, 150, 150))
        
        # draw rabbit
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)

        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
