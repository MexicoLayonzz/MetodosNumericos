
from PyQt5.QtWidgets import *
import sys

import Metodos.Biseccion as Bis
import Metodos.FalsaPosicion as FPos
import Metodos.Newton_Raphson as NRap
import Metodos.Secante as Sec

class Interfaz(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle('Hola Mundo')
        self.setFixedSize(1280,720)

        self.contenido()
    
    def contenido(self):
        self.lstTabMetodos = []
        self.lstNameMetodos = {'Biseccion':'#98F5F9','Falsa Posicion': 'BLUE','Newton Raphson': 'GREEN','Secante': 'BLACK'}

        self.tabMetodos = QTabWidget(self)
        self.tabMetodos.setGeometry(20,20,1240,680)

        for index,(name,color) in enumerate(self.lstNameMetodos.items()):
            baseWidget = QWidget()
            baseWidget.setStyleSheet(f'background-color: {color};')
            self.tabMetodos.addTab(baseWidget,f'{name}')
            self.lstTabMetodos.append(baseWidget)
            lblTitle = QLabel(f'Metodo De {name}',self.lstTabMetodos[index])
            lblTitle.move(20,20)
            if index == 0:
                self.biseccion_Widgets(indexWidget = index)
            elif index == 1:
                self.falsa_Posicion_Widgets(indexWidget = index)
            elif index == 2:
                self.newton_Raphson_Widgets(indexWidget = index)
            elif index == 3:
                self.secante_Widgets(indexWidget = index)
    
    def biseccion_Widgets(self,indexWidget:int = 0):
        lblFormula = QLabel('Ingrese Formula: ',self.lstTabMetodos[indexWidget])
        lblFormula.move(20,40)

        lneFormula = QLineEdit(self.lstTabMetodos[indexWidget])
        lneFormula.setGeometry(140,40,220,20)
        
        lblIntervalo = QLabel('Ingrese Intervalo: ',self.lstTabMetodos[indexWidget])
        lblIntervalo.move(20,60)

        lblIntA = QLabel('A',self.lstTabMetodos[indexWidget])
        lblIntA.move(140,60)

        lneIntA = QLineEdit(self.lstTabMetodos[indexWidget])
        lneIntA.setGeometry(160,60,80,20)

        lblIntB = QLabel('B',self.lstTabMetodos[indexWidget])
        lblIntB.move(260,60)

        lneIntB = QLineEdit(self.lstTabMetodos[indexWidget])
        lneIntB.setGeometry(280,60,80,20)

        lblTolerancia = QLabel('Ingrese Tolerancia: ',self.lstTabMetodos[indexWidget])
        lblTolerancia.move(20,80)

        lneTolerancia = QLineEdit(self.lstTabMetodos[indexWidget])
        lneTolerancia.setGeometry(140,80,220,20)
        
        btnIterar = QPushButton('Iterar',self.lstTabMetodos[indexWidget])
        btnIterar.setGeometry(20,110,320,20)
        
        lstTituloColumnas = {'i': 40, 'a': 160, 'b': 160, 'f(a)': 160, 'f(b)': 160, 'c': 160, 'f(c)': 160, 'ea': 60, 'er': 60, 'er%': 60}
        tblTablaIteraciones = QTableWidget(self.lstTabMetodos[indexWidget])
        tblTablaIteraciones.setGeometry(20, 280, 1200, 320)
        tblTablaIteraciones.setColumnCount(len(lstTituloColumnas))
        tblTablaIteraciones.setHorizontalHeaderLabels(lstTituloColumnas.keys())
        tblTablaIteraciones.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        for index,(columna,ancho) in enumerate(lstTituloColumnas.items()):
            tblTablaIteraciones.setColumnWidth(index, ancho)

    def falsa_Posicion_Widgets(self,indexWidget:int = 0):
        lblFormula = QLabel('Ingrese Formula: ',self.lstTabMetodos[indexWidget])
        lblFormula.move(20,40)

        lneFormula = QLineEdit(self.lstTabMetodos[indexWidget])
        lneFormula.setGeometry(140,40,220,20)
        
        lblIntervalo = QLabel('Ingrese Intervalo: ',self.lstTabMetodos[indexWidget])
        lblIntervalo.move(20,60)

        lblIntA = QLabel('A',self.lstTabMetodos[indexWidget])
        lblIntA.move(140,60)

        lneIntA = QLineEdit(self.lstTabMetodos[indexWidget])
        lneIntA.setGeometry(160,60,80,20)

        lblIntB = QLabel('B',self.lstTabMetodos[indexWidget])
        lblIntB.move(260,60)

        lneIntB = QLineEdit(self.lstTabMetodos[indexWidget])
        lneIntB.setGeometry(280,60,80,20)

        lblTolerancia = QLabel('Ingrese Tolerancia: ',self.lstTabMetodos[indexWidget])
        lblTolerancia.move(20,80)

        lneTolerancia = QLineEdit(self.lstTabMetodos[indexWidget])
        lneTolerancia.setGeometry(140,80,220,20)
        
        btnIterar = QPushButton('Iterar',self.lstTabMetodos[indexWidget])
        btnIterar.setGeometry(20,110,320,20)

        lstTituloColumnas = {'i': 40, 'a': 160, 'b': 160, 'f(a)': 160, 'f(b)': 160, 'c': 160, 'f(c)': 160, 'ea': 60, 'er': 60, 'er%': 60}
        tblTablaIteraciones = QTableWidget(self.lstTabMetodos[indexWidget])
        tblTablaIteraciones.setGeometry(20, 280, 1200, 320)
        tblTablaIteraciones.setColumnCount(len(lstTituloColumnas))
        tblTablaIteraciones.setHorizontalHeaderLabels(lstTituloColumnas.keys())
        tblTablaIteraciones.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        for index,(columna,ancho) in enumerate(lstTituloColumnas.items()):
            tblTablaIteraciones.setColumnWidth(index, ancho)

    def secante_Widgets(self,indexWidget:int = 0):
        lblFormula = QLabel('Ingrese Formula: ',self.lstTabMetodos[indexWidget])
        lblFormula.move(20,40)

        lneFormula = QLineEdit(self.lstTabMetodos[indexWidget])
        lneFormula.setGeometry(140,40,220,20)
        
        lblIntervalo = QLabel('Ingrese Punto De Partida: ',self.lstTabMetodos[indexWidget])
        lblIntervalo.move(20,60)

        lneIntA = QLineEdit(self.lstTabMetodos[indexWidget])
        lneIntA.setGeometry(180,60,180,20)

        lblTolerancia = QLabel('Ingrese Tolerancia: ',self.lstTabMetodos[indexWidget])
        lblTolerancia.move(20,80)

        lneTolerancia = QLineEdit(self.lstTabMetodos[indexWidget])
        lneTolerancia.setGeometry(140,80,220,20)
        
        btnIterar = QPushButton('Iterar',self.lstTabMetodos[indexWidget])
        btnIterar.setGeometry(20,110,320,20)

        lstTituloColumnas = {'i': 40, 'a': 160, 'f(a)': 160, 'c': 160, 'f(c)': 160, 'ea': 60, 'er': 60, 'er%': 60}
        tblTablaIteraciones = QTableWidget(self.lstTabMetodos[indexWidget])
        tblTablaIteraciones.setGeometry(20, 280, 1200, 320)
        tblTablaIteraciones.setColumnCount(len(lstTituloColumnas))
        tblTablaIteraciones.setHorizontalHeaderLabels(lstTituloColumnas.keys())
        tblTablaIteraciones.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        for index,(columna,ancho) in enumerate(lstTituloColumnas.items()):
            tblTablaIteraciones.setColumnWidth(index, ancho)

    def newton_Raphson_Widgets(self,indexWidget:int = 0):
        
        lblFormula = QLabel('Ingrese Formula: ',self.lstTabMetodos[indexWidget])
        lblFormula.move(20,40)

        lneFormula = QLineEdit(self.lstTabMetodos[indexWidget])
        lneFormula.setGeometry(140,40,220,20)
        
        lblIntervalo = QLabel('Ingrese Punto De Partida: ',self.lstTabMetodos[indexWidget])
        lblIntervalo.move(20,60)

        lneIntA = QLineEdit(self.lstTabMetodos[indexWidget])
        lneIntA.setGeometry(180,60,180,20)

        lblTolerancia = QLabel('Ingrese Tolerancia: ',self.lstTabMetodos[indexWidget])
        lblTolerancia.move(20,80)

        lneTolerancia = QLineEdit(self.lstTabMetodos[indexWidget])
        lneTolerancia.setGeometry(140,80,220,20)
        
        btnIterar = QPushButton('Iterar',self.lstTabMetodos[indexWidget])
        btnIterar.setGeometry(20,110,320,20)

        lstTituloColumnas = {'i': 40, 'a': 160, 'f(a)': 160, 'c': 160, 'f(c)': 160, 'ea': 60, 'er': 60, 'er%': 60}
        tblTablaIteraciones = QTableWidget(self.lstTabMetodos[indexWidget])
        tblTablaIteraciones.setGeometry(20, 280, 1200, 320)
        tblTablaIteraciones.setColumnCount(len(lstTituloColumnas))
        tblTablaIteraciones.setHorizontalHeaderLabels(lstTituloColumnas.keys())
        tblTablaIteraciones.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        for index,(columna,ancho) in enumerate(lstTituloColumnas.items()):
            tblTablaIteraciones.setColumnWidth(index, ancho)

if __name__ == "__main__":
    apli = QApplication(sys.argv)
    inter = Interfaz()
    inter.show()
    sys.exit(apli.exec_())
