from PySide.QtCore import *
from PySide.QtGui import *
class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple drawing1")
        #self.rabbit = QImage("image/rabbit.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(70,100),QPoint(100,110),
            QPoint(130,100),QPoint(100,150),
            ])
        p.setPen(QColor(255,0,0,127))
        p.setBrush(QColor(255,0,0,127))
        p.drawPie(50,150,100,100,0,180*32)

       # p.drawPolygon([
           # QPoint(50,200),QPoint(150,200),QPoint(100,400),])

        p.end()

app  = QApplication([])

draw1 = Simple_drawing_window2()
draw1.show()
app.exec_()
