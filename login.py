#!C:\tools\python\python.exe
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from locale import getdefaultlocale
import sqlite3
import hashlib

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(330, 158)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        LoginDialog.setMinimumSize(QtCore.QSize(330, 158))
        LoginDialog.setMaximumSize(QtCore.QSize(330, 158))
        self.gridLayoutWidget = QtWidgets.QWidget(LoginDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 331, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, -1, 10, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.idEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.idEdit.setObjectName("idEdit")
        self.gridLayout.addWidget(self.idEdit, 0, 1, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwordEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.passwordEdit.setInputMask("")
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 1, 1, 1, 1)
        self.secretwordEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.secretwordEdit.setText("")
        self.secretwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secretwordEdit.setObjectName("secretwordEdit")
        self.gridLayout.addWidget(self.secretwordEdit, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(LoginDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 110, 330, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.storeCheck = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.storeCheck.setEnabled(True)
        self.storeCheck.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.storeCheck.setChecked(True)
        self.storeCheck.setObjectName("storeCheck")
        self.horizontalLayout.addWidget(self.storeCheck)
        self.loginButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loginButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout.addWidget(self.loginButton)
        self.loginButton.clicked.connect(self.login)
        if getdefaultlocale()[0] == 'de_DE':
            self.retranslateUiGerman(LoginDialog)
        else:
            self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "pyNotify Login"))
        self.label_2.setText(_translate("LoginDialog", "Password:"))
        self.label_3.setText(_translate("LoginDialog", "Secretword:"))
        self.label.setText(_translate("LoginDialog", "Name/Email:"))
        self.secretwordEdit.setToolTip(_translate("LoginDialog", "<html><head/><body><p>Optional</p></body></html>"))
        self.secretwordEdit.setPlaceholderText(_translate("LoginDialog", "Optional"))
        self.storeCheck.setToolTip(_translate("LoginDialog", "This stores your name and password encrypted on your disk"))
        self.storeCheck.setText(_translate("LoginDialog", "Save Login?"))
        self.loginButton.setText(_translate("LoginDialog", "Login"))
        self.loginButton.setShortcut(_translate("LoginDialog", "Return"))

    def retranslateUiGerman(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "pyNotify Login"))
        self.label_2.setText(_translate("LoginDialog", "Passwort:"))
        self.label_3.setText(_translate("LoginDialog", "Secretword:"))
        self.label.setText(_translate("LoginDialog", "Name/Email:"))
        self.secretwordEdit.setToolTip(_translate("LoginDialog", "<html><head/><body><p>Optional</p></body></html>"))
        self.secretwordEdit.setPlaceholderText(_translate("LoginDialog", "Optional"))
        self.storeCheck.setToolTip(_translate("LoginDialog", "Speichert Name und Passwort lokal auf der Festplatte"))
        self.storeCheck.setText(_translate("LoginDialog", "Login speichern?"))
        self.loginButton.setText(_translate("LoginDialog", "Login"))
        self.loginButton.setShortcut(_translate("LoginDialog", "Return"))

    def login(self):
        print(str(self.idEdit.text()))
        with sqlite3.connect('settings.db') as c:
            c.execute('CREATE  TABLE "user" ("name" VARCHAR NOT NULL  UNIQUE , "pw" VARCHAR  UNIQUE , "secretword" VARCHAR  UNIQUE , "store" BOOL DEFAULT true)')
            user = str(self.idEdit.text())
            md5 = hashlib.md5(str(self.passwordEdit.text()).encode("utf-8")).hexdigest()
            pw = md5
            if str(self.secretwordEdit.text()) == '':
                secretword = 'None'
            else:
                secretword = str(self.secretwordEdit.text())
            if self.storeCheck.isChecked() == True:
                c.execute('INSERT INTO "user" ("name","pw","secretword") VALUES ("' + user + '","' + pw + '","' + secretword + '")')
            else:
                c.execute('INSERT INTO "user" ("name", "store") VALUES ("' + user + '", "false")')
            c.commit()

if __name__ == "__main__":
    import sys

    def runLogin(user = None):
        app = QtWidgets.QApplication(sys.argv)
        LoginDialog = QtWidgets.QDialog()
        ui = Ui_LoginDialog()
        ui.setupUi(LoginDialog)
        LoginDialog.show()
        if user is not None:
            ui.idEdit.setText(user)
            ui.storeCheck.setChecked(False)
        sys.exit(app.exec_())

    conSettings = sqlite3.connect('settings.db')
    cursorSettings = conSettings.cursor()
    try:
        cursorSettings.execute('select * from user')
    except sqlite3.OperationalError:
        runLogin()
    else:
        userTable = cursorSettings.fetchall()
        if userTable == []:
            runLogin()
        elif userTable[0][2] == 'false':
            runLogin(userTable[0][0])

    conSettings.close()
