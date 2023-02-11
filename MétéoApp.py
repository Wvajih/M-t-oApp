import requests
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from MeteoApp import Ui_MeteoApp
from numpy import array

def Exctracter(t,n):
    for l in range(len(t)):
        if (len(t[l])>7):
            ch=t[l]
            t[l]=ch[0:7]
    s=""
    e=""
    while(len(s)<n):
        s=""
        for i in range (len(t)):
            s+=t[i]+e
        e+=" "
    return s
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MeteoApp()
        self.ui.setupUi(self.main_win)
        self.ui.Button.clicked.connect(self.SetLabelValue)
    def show(self):
        self.main_win.show()
    def setb(self):
        QtWidgets.QPushButton(self)
    def SetLabelValue(self):
        x=self.ui.lineEdit.text()
        try:
            url = ('https://www.meteoart.com/'+x+'?page=today')
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            table1 = soup.find('tbody')
            rows1 = table1.find_all('tr')
            m1=array([[str]*8]*13)
            i1=0
            for row1 in rows1:
                cols1 = row1.find_all('td')
                data1 = [col1.text for col1 in cols1]
                j1=0
                for k1 in data1:
                    print(k1)
                    m1[i1][j1]=k1
                    j1+=1
                i1+=1
            print("---------------------")
            r=0
            for p in range(13):
                if (m1[p][0] is str) :
                    r+=1
            print(r)
            print(m1)
            if r!=2:
                Temp=Exctracter(m1[0][:],117)
                Meteo=Exctracter(m1[1][:],117)
                Pluie=Exctracter(m1[2][:],117)
                Pres=Exctracter(m1[3][:],117)
                Neige=Exctracter(m1[4][:],117)
                Gel=Exctracter(m1[5][:],117)
                Hu=Exctracter(m1[6][:],117)
                V_Vent=Exctracter(m1[7][:],115)
                R_Vent=Exctracter(m1[8][:],115)
                Vent=Exctracter(m1[9][:],120)
                D_Vent=Exctracter(m1[10][:],120)
                Nuage=Exctracter(m1[9][:],117)
                Visib=Exctracter(m1[12][:],117)
                self.ui.label_24.setText("Température        |       "+Temp)
                self.ui.label_25.setText("Météo                   |       "+Meteo)
                self.ui.label_26.setText( "Risques de pluie   |       "+Pluie)
                self.ui.label_27.setText( "Précipitations       |       "+Pres)
                self.ui.label_28.setText( "Risques de neige |       "+Neige)
                self.ui.label_29.setText( "Risque de gel       |       "+Gel)
                self.ui.label_30.setText( "Humidité               |       "+Hu)
                self.ui.label_31.setText( "Vitesse du vent    |       "+V_Vent)
                self.ui.label_32.setText( "Rafales de vent   |       "+R_Vent)
                self.ui.label_33.setText( "Vent                     |       "+Vent)
                self.ui.label_34.setText( "Direction du vent |       "+D_Vent)
                self.ui.label_35.setText( "Nuage                  |       "+Nuage)
                self.ui.label_36.setText( "Visibilité                |       "+Visib)
            else:
                Temp=Exctracter(m1[0][:],117)
                Meteo=Exctracter(m1[1][:],117)
                Pluie=Exctracter(m1[2][:],117)
                Pres=Exctracter(m1[3][:],117)
                #Neige=Exctracter(m1[4][:],117)
                #Gel=Exctracter(m1[5][:],117)
                Hu=Exctracter(m1[4][:],117)
                V_Vent=Exctracter(m1[5][:],115)
                R_Vent=Exctracter(m1[6][:],115)
                Vent=Exctracter(m1[7][:],120)
                D_Vent=Exctracter(m1[8][:],120)
                Nuage=Exctracter(m1[9][:],117)
                Visib=Exctracter(m1[10][:],117)
                print()
                self.ui.label_24.setText("Température        |       "+Temp)
                self.ui.label_25.setText("Météo                   |       "+Meteo)
                self.ui.label_26.setText( "Risques de pluie   |       "+Pluie)
                self.ui.label_27.setText( "Précipitations       |       "+Pres)
                self.ui.label_28.setText( "Risques de neige |       ")
                self.ui.label_29.setText( "Risque de gel       |       ")
                self.ui.label_30.setText( "Humidité               |       "+Hu)
                self.ui.label_31.setText( "Vitesse du vent    |       "+V_Vent)
                self.ui.label_32.setText( "Rafales de vent   |       "+R_Vent)
                self.ui.label_33.setText( "Vent                     |       "+Vent)
                self.ui.label_34.setText( "Direction du vent |       "+D_Vent)
                self.ui.label_35.setText( "Nuage                  |       "+Nuage)
                self.ui.label_36.setText( "Visibilité                |       "+Visib)
            
            # Extract the data from the table
            table = soup.find(class_='inner_wrap')
            rows = table.find_all(class_='weather_day_box')
            m=array([[str]*5]*15)
            i=0
            for row in rows:
                cols = row.find_all('div')
                data = [col.text for col in cols]
                j=0
                for k in data:
                    print(k)
                    m[i][j]=str([k])
                    j+=1
                i+=1
            print(m)
            Da1=m[0][0]
            Mois1=m[0][1]
            mm1=m[0][3]
            c1=m[0][4]
            Da2=m[1][0]
            Mois2=m[1][1]
            mm2=m[1][3]
            c2=m[1][4]
            Da3=m[2][0]
            Mois3=m[2][1]
            mm3=m[2][3]
            c3=m[2][4]
            Da4=m[3][0]
            Mois4=m[3][1]
            mm4=m[3][3]
            c4=m[3][4]
            Da5=m[4][0]
            Mois5=m[4][1]
            mm5=m[4][3]
            c5=m[4][4]
            self.ui.Day1.setText("<html><head/><body><p><span style=\" color:#ffffff;\">"+Da1[2:-2].upper()+"</span></p></body></html>")
            self.ui.Month1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">"+Mois1[2:-2]+"</span></p></body></html>")
            self.ui.mm1.setText("<html><head/><body><p><span style=\" font-size:7pt; color:#ffffff;\">"+mm1[2:-2]+"</span></p></body></html>")
            self.ui.c1.setText("<html><head/><body><p><span style=\" color:#ffffff;\">"+c1[2:-2]+"</span></p></body></html>")

            self.ui.Day2.setText("<html><head/><body><p><span style=\" color:#ffffff;\">"+Da2[2:-2].upper()+"</span></p></body></html>")
            self.ui.Month2.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">"+Mois2[2:-2]+"</span></p></body></html>")
            self.ui.mm2.setText("<html><head/><body><p><span style=\" font-size:7pt; color:#ffffff;\">"+mm2[2:-2]+"</span></p></body></html>")
            self.ui.c2.setText("<html><head/><body><p><span style=\" color:#ffffff;\">"+c2[2:-2]+"</span></p></body></html>")

            self.ui.Day3.setText("<html><head/><body><p><span style=\" color:#ffffff;\">"+Da3[2:-2].upper()+"</span></p></body></html>")
            self.ui.Month3.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">"+Mois3[2:-2]+"</span></p></body></html>")
            self.ui.mm3.setText("<html><head/><body><p><span style=\" font-size:7pt; color:#ffffff;\">"+mm3[2:-2]+"</span></p></body></html>")
            self.ui.c3.setText("<html><head/><body><p><span style=\" color:#ffffff;\">"+c3[2:-2]+"</span></p></body></html>")
            
            self.ui.Day4.setText("<html><head/><body><p><span style=\" color:#ffffff;\">"+Da4[2:-2].upper()+"</span></p></body></html>")
            self.ui.Month4.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">"+Mois4[2:-2]+"</span></p></body></html>"[2:-2])
            self.ui.mm4.setText("<html><head/><body><p><span style=\" font-size:7pt; color:#ffffff;\">"+mm4[2:-2]+"</span></p></body></html>")
            self.ui.c4.setText("<html><head/><body><p><span style=\" color:#ffffff;\">"+c4[2:-2]+"</span></p></body></html>")

            self.ui.Day5.setText("<html><head/><body><p><span style=\" color:#ffffff;\">"+Da5[2:-2].upper()+"</span></p></body></html>")
            self.ui.Month5.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">"+Mois5[2:-2]+"</span></p></body></html>")
            self.ui.mm5.setText("<html><head/><body><p><span style=\" font-size:7pt; color:#ffffff;\">"+mm5[2:-2]+"</span></p></body></html>")
            self.ui.c5.setText("<html><head/><body><p><span style=\" color:#ffffff;\">"+c5[2:-2]+"</span></p></body></html>")
        except:
            self.ui.lineEdit.setText(x+": Research")
if __name__=="__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())