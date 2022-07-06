from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pandas

class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        #custom properties
        self.value=0
        self.width =200
        self.height=200
        self.progress_width=10
        self.progress_rounded_cap = True
        self.progress_color = 0x7d12ff
        self.max_value=100
        self.font_family="Segoe UI"
        self.font_size =12
        self.suffix="%"
        self.text_color=0x498BD1
        self.enable_show=True

        #set default size window layout
        self.resize(self.width, self.height)

    def add_shadow(self,enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setOffset(0)
            self.shadow.setColor(QColor(125,18,255,80))
            self.setGraphicsEffect(self.shadow)
    
    def set_value(self,value):
        self.value =value
        self.repaint() #render progress bar after change valu

    #paint event, design your circular progress
    def paintEvent(self,e):
       #set progress parameters
       width = self.width-self.progress_width
       height=self.height-self.progress_width
       margin = self.progress_width/2
       value =self.value*360/self.max_value

       #painter
       painter = QPainter()
       painter.begin(self)
       painter.setRenderHint(QPainter.Antialiasing) #remove pixelated edges
       painter.setFont(QFont(self.font_family, self.font_size))

       #create rectangle
       rect = QRect(0,0,self.width,self.height)
       painter.setPen(Qt.NoPen)
       painter.drawRect(rect)

       #pen
       pen =QPen()
       pen.setColor(QColor(self.progress_color))
       pen.setWidth(self.progress_width)

       #set round cap
       if self.progress_rounded_cap:
        pen.setCapStyle(Qt.RoundCap)

       #create arc circular progress
       painter.setPen(pen)
       painter.drawArc(margin,margin,width,height,-90*16, -value*16)

       #create text
       pen.setColor(QColor(self.text_color))
       painter.setPen(pen)

       painter.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

       #end
       painter.end()