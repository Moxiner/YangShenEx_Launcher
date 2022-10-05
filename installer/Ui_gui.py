# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Documents\Gitee\YuansShen_LauncherEX\yuanShenEx\installer\gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_installer(object):
    def setupUi(self, installer):
        installer.setObjectName("installer")
        installer.setEnabled(True)
        installer.resize(759, 683)
        self.centralwidget = QtWidgets.QWidget(installer)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_Widget = QtWidgets.QWidget(self.centralwidget)
        self.Main_Widget.setGeometry(QtCore.QRect(20, 10, 730, 471))
        self.Main_Widget.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"}\n"
"QPushButton:hove {\n"
"    padding-bottom:5px;\n"
"}\n"
"QWidget{\n"
"    border-radius:5px;\n"
"}")
        self.Main_Widget.setObjectName("Main_Widget")
        self.Fontground_Label = QtWidgets.QLabel(self.Main_Widget)
        self.Fontground_Label.setGeometry(QtCore.QRect(0, 0, 730, 391))
        self.Fontground_Label.setStyleSheet("border-image: url(:/img/background.png);\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;")
        self.Fontground_Label.setText("")
        self.Fontground_Label.setObjectName("Fontground_Label")
        self.Title_Lable = QtWidgets.QLabel(self.Main_Widget)
        self.Title_Lable.setGeometry(QtCore.QRect(10, 0, 191, 31))
        font = QtGui.QFont()
        font.setFamily("有爱魔兽圆体 CN")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Title_Lable.setFont(font)
        self.Title_Lable.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title_Lable.setObjectName("Title_Lable")
        self.Top_Right_Frame = QtWidgets.QFrame(self.Main_Widget)
        self.Top_Right_Frame.setGeometry(QtCore.QRect(570, 0, 71, 31))
        self.Top_Right_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Top_Right_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Right_Frame.setObjectName("Top_Right_Frame")
        self.InstallerStart_Button = QtWidgets.QPushButton(self.Main_Widget)
        self.InstallerStart_Button.setGeometry(QtCore.QRect(265, 240, 200, 51))
        font = QtGui.QFont()
        font.setFamily("有爱魔兽圆体 CN Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.InstallerStart_Button.setFont(font)
        self.InstallerStart_Button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 200, 31);\n"
"    border-radius:5\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(185, 144, 22);\n"
"    border-radius:5\n"
"\n"
"}")
        self.InstallerStart_Button.setObjectName("InstallerStart_Button")
        self.Bottom_Installer_Frame = QtWidgets.QFrame(self.Main_Widget)
        self.Bottom_Installer_Frame.setGeometry(QtCore.QRect(0, 330, 730, 141))
        self.Bottom_Installer_Frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"hide:True\n"
"")
        self.Bottom_Installer_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Bottom_Installer_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Bottom_Installer_Frame.setObjectName("Bottom_Installer_Frame")
        self.Installer_Frame = QtWidgets.QFrame(self.Bottom_Installer_Frame)
        self.Installer_Frame.setGeometry(QtCore.QRect(10, 10, 711, 121))
        self.Installer_Frame.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:5px;\n"
"    \n"
"    color: rgb(244, 216, 135);\n"
"    background-color: rgb(57, 59, 64);\n"
"}\n"
"QLineEdit {\n"
"    \n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"QFrame {\n"
"    border:none;\n"
"    }")
        self.Installer_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Installer_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Installer_Frame.setObjectName("Installer_Frame")
        self.Look_Button = QtWidgets.QPushButton(self.Installer_Frame)
        self.Look_Button.setGeometry(QtCore.QRect(570, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("有爱魔兽圆体 CN Medium")
        font.setPointSize(7)
        self.Look_Button.setFont(font)
        self.Look_Button.setStyleSheet("QPushButton:pressed {\n"
"        \n"
"    background-color: rgb(34, 35, 38);\n"
"}")
        self.Look_Button.setObjectName("Look_Button")
        self.Path_LineEdit = QtWidgets.QLineEdit(self.Installer_Frame)
        self.Path_LineEdit.setGeometry(QtCore.QRect(20, 40, 531, 31))
        self.Path_LineEdit.setObjectName("Path_LineEdit")
        self.Installer_Label = QtWidgets.QLabel(self.Installer_Frame)
        self.Installer_Label.setGeometry(QtCore.QRect(20, 0, 111, 31))
        font = QtGui.QFont()
        font.setFamily("有爱魔兽圆体 CN Medium")
        font.setPointSize(12)
        self.Installer_Label.setFont(font)
        self.Installer_Label.setObjectName("Installer_Label")
        self.CreateStartedLink_CheckBoc = QtWidgets.QCheckBox(self.Installer_Frame)
        self.CreateStartedLink_CheckBoc.setGeometry(QtCore.QRect(20, 90, 151, 16))
        font = QtGui.QFont()
        font.setFamily("有爱魔兽圆体 CN Medium")
        font.setPointSize(9)
        self.CreateStartedLink_CheckBoc.setFont(font)
        self.CreateStartedLink_CheckBoc.setChecked(True)
        self.CreateStartedLink_CheckBoc.setObjectName("CreateStartedLink_CheckBoc")
        self.CreateDesktopLink_CheckBox = QtWidgets.QCheckBox(self.Installer_Frame)
        self.CreateDesktopLink_CheckBox.setGeometry(QtCore.QRect(150, 90, 131, 16))
        font = QtGui.QFont()
        font.setFamily("有爱魔兽圆体 CN Medium")
        font.setPointSize(9)
        self.CreateDesktopLink_CheckBox.setFont(font)
        self.CreateDesktopLink_CheckBox.setObjectName("CreateDesktopLink_CheckBox")
        self.layoutWidget = QtWidgets.QWidget(self.Main_Widget)
        self.layoutWidget.setGeometry(QtCore.QRect(660, 0, 71, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Top_Right_Layout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.Top_Right_Layout.setContentsMargins(0, 0, 5, 0)
        self.Top_Right_Layout.setSpacing(10)
        self.Top_Right_Layout.setObjectName("Top_Right_Layout")
        self.Min_Bottom = QtWidgets.QPushButton(self.layoutWidget)
        self.Min_Bottom.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255 , 95);\n"
"}")
        self.Min_Bottom.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Min_Bottom.setIcon(icon)
        self.Min_Bottom.setIconSize(QtCore.QSize(20, 20))
        self.Min_Bottom.setObjectName("Min_Bottom")
        self.Top_Right_Layout.addWidget(self.Min_Bottom)
        self.Close_Buttom = QtWidgets.QPushButton(self.layoutWidget)
        self.Close_Buttom.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(255, 0, 0 ， 95);\n"
"}")
        self.Close_Buttom.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close_Buttom.setIcon(icon1)
        self.Close_Buttom.setIconSize(QtCore.QSize(20, 20))
        self.Close_Buttom.setObjectName("Close_Buttom")
        self.Top_Right_Layout.addWidget(self.Close_Buttom)
        self.Fontground_Label.raise_()
        self.Title_Lable.raise_()
        self.Top_Right_Frame.raise_()
        self.Bottom_Installer_Frame.raise_()
        self.layoutWidget.raise_()
        self.InstallerStart_Button.raise_()
        installer.setCentralWidget(self.centralwidget)

        self.retranslateUi(installer)
        self.Min_Bottom.clicked.connect(installer.showMinimized)
        self.Close_Buttom.clicked.connect(installer.close)
        QtCore.QMetaObject.connectSlotsByName(installer)

    def retranslateUi(self, installer):
        _translate = QtCore.QCoreApplication.translate
        installer.setWindowTitle(_translate("installer", "MainWindow"))
        self.Title_Lable.setText(_translate("installer", "原神启动器EX安装程序"))
        self.InstallerStart_Button.setText(_translate("installer", "立即安装"))
        self.Look_Button.setText(_translate("installer", "选择文件位置"))
        self.Installer_Label.setText(_translate("installer", "安装位置"))
        self.CreateStartedLink_CheckBoc.setText(_translate("installer", "创建桌面快捷方式"))
        self.CreateDesktopLink_CheckBox.setText(_translate("installer", "创建开始快捷方式"))
import styple_rc
