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
            QPoint(90,90),QPoint(100,110),
            QPoint(110,90),QPoint(100,150),
            ])
        p.setPen(QColor(255,0,120))
        p.setBrush(QColor(255,0,120))
        p.drawPie(60,150,30,30,0,180*32)
        p.drawPie(90,150,30,30,0,180*32)
        p.drawPie(120,150,30,30,0,180*32)
        p.drawPie(75,180,30,30,0,180*32)
        p.drawPie(105,180,30,30,0,180*32)
        p.drawPie(90,210,30,30,0,180*32)
       # p.drawPolygon([
           # QPoint(50,200),QPoint(150,200),QPoint(100,400),])

        p.end()

app  = QApplication([])

draw1 = Simple_drawing_window2()
draw1.show()
app.exec_()
