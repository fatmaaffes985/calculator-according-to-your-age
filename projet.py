from PyQt5.QtWidgets import QLabel,QLineEdit,QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QMessageBox,QComboBox
import sys
import math
def calculer():
    age=Age.text().strip()
    a=A.text().strip()
    b=B.text().strip()
    if a=="" or b=="" or age=="" :
        QMessageBox.critical(fenetre,"Erreur","Voulez-vous saisir ?")
        A.setStyleSheet("background-color:red;")
        B.setStyleSheet("background-color:red;")
        Age.setStyleSheet("background-color:red;")
        return
    elif  a.isdigit()==False or b.isdigit()==False or age.isdigit()==False:
        QMessageBox.critical(fenetre,"Erreur","Voulez-vous saisir  un entier")
        A.setStyleSheet("background-color:red;")
        B.setStyleSheet("background-color:red;")
        Age.setStyleSheet("background-color:red;")
        return

    else:
        if int(age)>=5 and int(age)<=10:
            if int(b) == 0:
                QMessageBox.critical(fenetre, "Erreur", "on ne peut pas diviser par 0")
                B.setStyleSheet("background-color:red;")
                return
            else:
                f = float(a) / float(b)
                resultat=f"""
                somme(A+B):{int(a)+int(b)}
                Différence (A - B): {int(a) - int(b)}
                Produit (A × B): {int(a) * int(b)}
                Division (A ÷ B): {f:.6f}"""
        elif int(age)>=11 and int(age)<=18:
            resultat=f"""
            puissance (A^B):{int(a)**int(b)}
            pgcd (A,B):{math.gcd(int(a),int(b))}
            ppcm(A,B):{abs(int(a)*int(b))//math.gcd(int(a),int(b))} """
        else:
            resultat=f"""
            A en binaire = {bin(int(a))}, B en binaire = {bin(int(b))}
            A & B (ET) = {int(a) & int(b)}, A | B (OU) = {int(a) | int(b)}
            A ^ B (XOR) = {int(a) ^ int(b)}
            A en hexadécimal = {hex(int(a))}, B en hexadécimal = {hex(int(b))}
            A en octal = {oct(int(a))}, B en octal = {oct(int(b))}"""


        resultats.setText(resultat)
        combo.addItem(resultat)
        resultats.setStyleSheet("background-color:beige;")


def effacer():
    A.clear()
    B.clear()
    Age.clear()
    resultats.setText("")
    A.setStyleSheet("background-color:white;")
    B.setStyleSheet("background-color:white;")
    Age.setStyleSheet("background-color:white;")
    resultats.setStyleSheet("background-color:white;")
def quitter():
    fenetre.close()

app=QApplication(sys.argv)
fenetre=QWidget()
fenetre.setWindowTitle("Calculatrice d'entier")
fenetre.setFixedSize(500, 300)
layout=QVBoxLayout()
layouttitre=QHBoxLayout()
titre=QLabel("Operations selon ton age")
layouttitre.addWidget(titre)
layoutage=QHBoxLayout()
age=QLabel("votre Age")
Age=QLineEdit()
layoutage.addWidget(age)
layoutage.addWidget(Age)
layouta=QHBoxLayout()
a=QLabel("Entier A")
A=QLineEdit()
layouta.addWidget(a)
layouta.addWidget(A)
layoutb=QHBoxLayout()
b=QLabel("Entier B")
B=QLineEdit()
layoutb.addWidget(b)
layoutb.addWidget(B)
layoutc=QHBoxLayout()
combo = QComboBox()
layoutc.addWidget(combo)
layoutbt=QHBoxLayout()
b1=QPushButton("Calculer")
b2=QPushButton("Effacer")
b3=QPushButton("Qitter")
layoutbt.addWidget(b1)
layoutbt.addWidget(b2)
layoutbt.addWidget(b3)
b1.clicked.connect(calculer)
b2.clicked.connect(effacer)
b3.clicked.connect(quitter)
layoutres=QHBoxLayout()
resultats=QLabel("")
layoutres.addWidget(resultats)
titre.setStyleSheet("color:darkred;font-style: italic;text-align:center;font-weight:bold;")
a.setStyleSheet("color:brown;font-style: italic;")
b.setStyleSheet("color:brown;font-style: italic;")
age.setStyleSheet("color:brown;font-style: italic;")
A.setStyleSheet("border: 2px solid brown;")
B.setStyleSheet("border: 2px solid brown;")
Age.setStyleSheet("border: 2px solid brown;")
b1.setStyleSheet("background-color:beige;")
b2.setStyleSheet("background-color:beige;")
b3.setStyleSheet("background-color:beige;")
layout.addLayout(layouttitre)
layout.addLayout(layoutage)
layout.addLayout(layouta)
layout.addLayout(layoutb)
layout.addLayout(layoutc)
layout.addLayout(layoutbt)
layout.addLayout(layoutres)
fenetre.setLayout(layout)
fenetre.show()
sys.exit(app.exec_())