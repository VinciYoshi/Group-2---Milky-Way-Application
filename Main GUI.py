from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
from functions import *

# Creation of the database
createDatabase()

# GUI Window
class Ui_root(object):

    def setupUi(self, root):
        root.setObjectName("root")
        root.setFixedSize(795, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("baby_bottle.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        root.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")
        self.tabs.setGeometry(QtCore.QRect(0, 0, 600, 570))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.tabs.setFont(font)
        self.tabs.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabs.setObjectName("tabs")

        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")

        self.logo = QtWidgets.QLabel(self.home)
        self.logo.setGeometry(QtCore.QRect(50, 0, 700, 570))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("milkyway.png"))
        self.logo.setObjectName("logo")

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)

        self.aboutUs = QtWidgets.QLabel(self.home)
        self.aboutUs.setGeometry(QtCore.QRect(253, 400, 130, 30))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)

        self.aboutUs.setFont(font)
        self.aboutUs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutUs.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutUs.setObjectName("aboutUs")

        self.tabs.addTab(self.home, "")

# Tab 2 - Donation of milk
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")
        self.tab2.setObjectName("tab2")

        self.cID = QtWidgets.QLabel(self.tab2)
        self.cID.setGeometry(QtCore.QRect(50, 30, 150, 20))

        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(11)

        self.cID.setFont(font)
        self.cID.setObjectName("cID")

        self.cFirstName = QtWidgets.QLabel(self.tab2)
        self.cFirstName.setGeometry(QtCore.QRect(50, 60, 150, 20))

        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(11)

        self.cFirstName.setFont(font)
        self.cFirstName.setObjectName("cFirstNameName")

        self.cLastName = QtWidgets.QLabel(self.tab2)
        self.cLastName.setGeometry(QtCore.QRect(50, 90, 150, 20))

        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(11)

        self.cLastName.setFont(font)
        self.cLastName.setObjectName("cLastName")

        self.cDescrip = QtWidgets.QLabel(self.tab2)
        self.cDescrip.setGeometry(QtCore.QRect(50, 135, 150, 20))

        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(11)

        self.cDescrip.setFont(font)
        self.cDescrip.setObjectName("cDescrip")

        self.cExpiry = QtWidgets.QLabel(self.tab2)
        self.cExpiry.setGeometry(QtCore.QRect(50, 255, 150, 20))

        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(11)

        self.cExpiry.setFont(font)
        self.cExpiry.setObjectName("cExpiry")

        self.cIDInput = QtWidgets.QLineEdit(self.tab2)
        self.cIDInput.setGeometry(QtCore.QRect(200, 30, 350, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.cIDInput.setFont(font)
        self.cIDInput.setFrame(True)
        self.cIDInput.setObjectName("cIDInput")

        self.cFirstNameInput = QtWidgets.QLineEdit(self.tab2)
        self.cFirstNameInput.setGeometry(QtCore.QRect(200, 60, 350, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.cFirstNameInput.setFont(font)
        self.cFirstNameInput.setObjectName("cFirstNameInput")

        self.cLastNameInput = QtWidgets.QLineEdit(self.tab2)
        self.cLastNameInput.setGeometry(QtCore.QRect(200, 90, 350, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.cLastNameInput.setFont(font)
        self.cLastNameInput.setObjectName("cLastNameInput")

        self.cDescripInput = QtWidgets.QTextEdit(self.tab2)
        self.cDescripInput.setGeometry(QtCore.QRect(200, 135, 350, 100))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.cDescripInput.setFont(font)
        self.cDescripInput.setObjectName("cDescripInput")

        self.cExpiryInput = QtWidgets.QCalendarWidget(self.tab2)
        self.cExpiryInput.setGeometry(QtCore.QRect(200, 255, 350, 210))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)

        self.cExpiryInput.setFont(font)
        self.cExpiryInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cExpiryInput.setGridVisible(True)
        self.cExpiryInput.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.NoHorizontalHeader)
        self.cExpiryInput.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.cExpiryInput.setObjectName("cExpiryInput")

        self.cClear = QtWidgets.QPushButton(self.tab2)
        self.cClear.setGeometry(QtCore.QRect(250, 475, 100, 30))
        self.cClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cClear.setObjectName("cClear")

        self.cSubmit = QtWidgets.QPushButton(self.tab2)
        self.cSubmit.setGeometry(QtCore.QRect(400, 475, 100, 30))
        self.cSubmit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cSubmit.setObjectName("cSubmit")

        self.tabs.addTab(self.tab2, "")

# Tab 3 - Read Function
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")
        self.tab3.setObjectName("tab3")

        self.rTable = QtWidgets.QTableWidget(self.tab3)
        self.rTable.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")
        self.rTable.setGeometry(QtCore.QRect(20, 250, 550, 250))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(7)

        self.rTable.setFont(font)
        self.rTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.rTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.rTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.rTable.setGridStyle(QtCore.Qt.SolidLine)
        self.rTable.setCornerButtonEnabled(True)
        self.rTable.setObjectName("rTable")
        self.rTable.setColumnCount(5)
        self.rTable.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.rTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.rTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.rTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.rTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.rTable.setHorizontalHeaderItem(4, item)
        self.rTable.horizontalHeader().setVisible(True)
        self.rTable.horizontalHeader().setCascadingSectionResizes(True)
        self.rTable.horizontalHeader().setDefaultSectionSize(137)
        self.rTable.horizontalHeader().setHighlightSections(True)

        self.rLine = QtWidgets.QFrame(self.tab3)
        self.rLine.setGeometry(QtCore.QRect(190, 20, 3, 160))
        self.rLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.rLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.rLine.setObjectName("rLine")

        self.rFind = QtWidgets.QLabel(self.tab3)
        self.rFind.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.rFind.setObjectName("rFind")

        self.rFindInput = QtWidgets.QLineEdit(self.tab3)
        self.rFindInput.setGeometry(QtCore.QRect(20, 50, 150, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.rFindInput.setFont(font)
        self.rFindInput.setObjectName("rFindInput")

        self.rSearch = QtWidgets.QPushButton(self.tab3)
        self.rSearch.setGeometry(QtCore.QRect(50, 90, 93, 28))
        self.rSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rSearch.setObjectName("rSearch")

        self.rFirstName = QtWidgets.QLabel(self.tab3)
        self.rFirstName.setGeometry(QtCore.QRect(210, 20, 110, 16))
        self.rFirstName.setObjectName("rFirstName")

        self.rLastName = QtWidgets.QLabel(self.tab3)
        self.rLastName.setGeometry(QtCore.QRect(210, 60, 110, 16))
        self.rLastName.setObjectName("rLastName")

        self.rExpiry = QtWidgets.QLabel(self.tab3)
        self.rExpiry.setGeometry(QtCore.QRect(210, 110, 110, 16))
        self.rExpiry.setObjectName("rExpiry")

        self.rDescription = QtWidgets.QLabel(self.tab3)
        self.rDescription.setGeometry(QtCore.QRect(210, 150, 110, 16))
        self.rDescription.setObjectName("rDescription")

        self.rReadFirstName = QtWidgets.QLineEdit(self.tab3)
        self.rReadFirstName.setGeometry(QtCore.QRect(320, 20, 250, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.rReadFirstName.setFont(font)
        self.rReadFirstName.setReadOnly(True)
        self.rReadFirstName.setObjectName("rReadFirstName")

        self.rReadLastName = QtWidgets.QLineEdit(self.tab3)
        self.rReadLastName.setGeometry(QtCore.QRect(320, 60, 250, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.rReadLastName.setFont(font)
        self.rReadLastName.setReadOnly(True)
        self.rReadLastName.setObjectName("rReadLastName")

        self.rReadExpiry = QtWidgets.QLineEdit(self.tab3)
        self.rReadExpiry.setGeometry(QtCore.QRect(320, 110, 250, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.rReadExpiry.setFont(font)
        self.rReadExpiry.setReadOnly(True)
        self.rReadExpiry.setObjectName("rReadExpiry")

        self.rReadDescrip = QtWidgets.QTextEdit(self.tab3)
        self.rReadDescrip.setGeometry(QtCore.QRect(320, 150, 250, 81))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.rReadDescrip.setFont(font)
        self.rReadDescrip.setReadOnly(True)
        self.rReadDescrip.setObjectName("rReadDescrip")

        self.rRefresh = QtWidgets.QPushButton(self.tab3)
        self.rRefresh.setGeometry(QtCore.QRect(450, 500, 100, 28))
        self.rRefresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rRefresh.setObjectName("rRefresh")

        self.rRemind = QtWidgets.QLabel(self.tab3)
        self.rRemind.setGeometry(QtCore.QRect(20, 200, 300, 20))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)

        self.rRemind.setFont(font)
        self.rRemind.setAlignment(QtCore.Qt.AlignCenter)
        self.rRemind.setObjectName("rRemind")

        self.tabs.addTab(self.tab3, "")

# Tab 4 - Update Tab (Edit)
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.tab4.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")

        self.uID = QtWidgets.QLabel(self.tab4)
        self.uID.setGeometry(QtCore.QRect(50, 50, 150, 15))
        self.uID.setObjectName("uID")

        self.uFirstName = QtWidgets.QLabel(self.tab4)
        self.uFirstName.setGeometry(QtCore.QRect(50, 115, 151, 16))
        self.uFirstName.setObjectName("uFirstName")

        self.uLastName = QtWidgets.QLabel(self.tab4)
        self.uLastName.setGeometry(QtCore.QRect(50, 150, 151, 16))
        self.uLastName.setObjectName("uLastName")

        self.uDescrip = QtWidgets.QLabel(self.tab4)
        self.uDescrip.setGeometry(QtCore.QRect(50, 185, 151, 16))
        self.uDescrip.setObjectName("uDescrip")

        self.uExpiry = QtWidgets.QLabel(self.tab4)
        self.uExpiry.setGeometry(QtCore.QRect(50, 300, 150, 15))
        self.uExpiry.setObjectName("uExpiry")

        self.uIDInput = QtWidgets.QLineEdit(self.tab4)
        self.uIDInput.setGeometry(QtCore.QRect(200, 44, 250, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.uIDInput.setFont(font)
        self.uIDInput.setObjectName("uIDInput")

        self.uSearch = QtWidgets.QPushButton(self.tab4)
        self.uSearch.setGeometry(QtCore.QRect(480, 44, 93, 25))
        self.uSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uSearch.setObjectName("uSearch")

        self.uFirstNameInput = QtWidgets.QLineEdit(self.tab4)
        self.uFirstNameInput.setGeometry(QtCore.QRect(200, 115, 371, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.uFirstNameInput.setFont(font)
        self.uFirstNameInput.setObjectName("uFirstNameInput")

        self.uLastNameInput = QtWidgets.QLineEdit(self.tab4)
        self.uLastNameInput.setGeometry(QtCore.QRect(200, 150, 371, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.uLastNameInput.setFont(font)
        self.uLastNameInput.setObjectName("uLastNameInput")

        self.uDescripInput = QtWidgets.QTextEdit(self.tab4)
        self.uDescripInput.setGeometry(QtCore.QRect(200, 185, 371, 100))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.uDescripInput.setFont(font)
        self.uDescripInput.setObjectName("uDescripInput")

        self.uCalendar = QtWidgets.QCalendarWidget(self.tab4)
        self.uCalendar.setGeometry(QtCore.QRect(200, 290, 371, 210))
        self.uCalendar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uCalendar.setGridVisible(True)
        self.uCalendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.NoHorizontalHeader)
        self.uCalendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.uCalendar.setObjectName("uCalendar")

        self.uSmallLabel = QtWidgets.QLabel(self.tab4)
        self.uSmallLabel.setGeometry(QtCore.QRect(50, 80, 521, 20))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)

        self.uSmallLabel.setFont(font)
        self.uSmallLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uSmallLabel.setObjectName("uSmallLabel")

        self.uLine1 = QtWidgets.QFrame(self.tab4)
        self.uLine1.setGeometry(QtCore.QRect(50, 80, 191, 20))
        self.uLine1.setFrameShape(QtWidgets.QFrame.HLine)
        self.uLine1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.uLine1.setObjectName("uLine1")
        self.uLine2 = QtWidgets.QFrame(self.tab4)

        self.uLine2.setGeometry(QtCore.QRect(380, 80, 191, 20))
        self.uLine2.setFrameShape(QtWidgets.QFrame.HLine)
        self.uLine2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.uLine2.setObjectName("uLine2")

        self.uDone = QtWidgets.QPushButton(self.tab4)
        self.uDone.setGeometry(QtCore.QRect(60, 400, 93, 28))
        self.uDone.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uDone.setObjectName("uDone")

        self.uCancel = QtWidgets.QPushButton(self.tab4)
        self.uCancel.setGeometry(QtCore.QRect(60, 450, 93, 28))
        self.uCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uCancel.setObjectName("uCancel")

        self.tabs.addTab(self.tab4, "")

# Tab 5 - Withdraw Milk (Delete)
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.tab5.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")

        self.dID = QtWidgets.QLabel(self.tab5)
        self.dID.setGeometry(QtCore.QRect(50, 50, 150, 15))
        self.dID.setObjectName("dID")

        self.dIDInput = QtWidgets.QLineEdit(self.tab5)
        self.dIDInput.setGeometry(QtCore.QRect(200, 44, 250, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.dIDInput.setFont(font)
        self.dIDInput.setObjectName("dIDInput")

        self.dSearch = QtWidgets.QPushButton(self.tab5)
        self.dSearch.setGeometry(QtCore.QRect(480, 44, 93, 25))
        self.dSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dSearch.setObjectName("dSearch")

        self.dContents = QtWidgets.QLabel(self.tab5)
        self.dContents.setGeometry(QtCore.QRect(50, 80, 521, 20))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)

        self.dContents.setFont(font)
        self.dContents.setAlignment(QtCore.Qt.AlignCenter)
        self.dContents.setObjectName("dContents")

        self.uLine2_2 = QtWidgets.QFrame(self.tab5)
        self.uLine2_2.setGeometry(QtCore.QRect(380, 80, 191, 20))
        self.uLine2_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.uLine2_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.uLine2_2.setObjectName("uLine2_2")
        self.uLine2_3 = QtWidgets.QFrame(self.tab5)
        self.uLine2_3.setGeometry(QtCore.QRect(50, 80, 191, 20))
        self.uLine2_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.uLine2_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.uLine2_3.setObjectName("uLine2_3")

        self.dFirstName = QtWidgets.QLabel(self.tab5)
        self.dFirstName.setGeometry(QtCore.QRect(50, 120, 151, 16))
        self.dFirstName.setObjectName("dFirstName")

        self.dFirstNameInput = QtWidgets.QLineEdit(self.tab5)
        self.dFirstNameInput.setGeometry(QtCore.QRect(200, 115, 371, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.dFirstNameInput.setFont(font)
        self.dFirstNameInput.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.dFirstNameInput.setReadOnly(True)
        self.dFirstNameInput.setObjectName("dFirstNameInput")

        self.dLastName = QtWidgets.QLabel(self.tab5)
        self.dLastName.setGeometry(QtCore.QRect(50, 150, 151, 16))
        self.dLastName.setObjectName("dLastName")

        self.dLastNameInput = QtWidgets.QLineEdit(self.tab5)
        self.dLastNameInput.setGeometry(QtCore.QRect(200, 145, 371, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.dLastNameInput.setFont(font)
        self.dLastNameInput.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.dLastNameInput.setReadOnly(True)
        self.dLastNameInput.setObjectName("dLastNameInput")

        self.dDescrip = QtWidgets.QLabel(self.tab5)
        self.dDescrip.setGeometry(QtCore.QRect(50, 180, 151, 16))
        self.dDescrip.setObjectName("dDescrip")

        self.dDescripInput = QtWidgets.QTextEdit(self.tab5)
        self.dDescripInput.setGeometry(QtCore.QRect(200, 180, 371, 200))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.dDescripInput.setFont(font)
        self.dDescripInput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.dDescripInput.setReadOnly(True)
        self.dDescripInput.setObjectName("dDescripInput")

        self.dExpiry = QtWidgets.QLabel(self.tab5)
        self.dExpiry.setGeometry(QtCore.QRect(50, 400, 150, 15))
        self.dExpiry.setObjectName("dExpiry")

        self.dExpiryInput = QtWidgets.QLineEdit(self.tab5)
        self.dExpiryInput.setGeometry(QtCore.QRect(200, 395, 371, 25))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.dExpiryInput.setFont(font)
        self.dExpiryInput.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.dExpiryInput.setReadOnly(True)
        self.dExpiryInput.setObjectName("dExpiryInput")

        self.dDelete = QtWidgets.QPushButton(self.tab5)
        self.dDelete.setGeometry(QtCore.QRect(202, 460, 371, 28))
        self.dDelete.setObjectName("dDelete")

        self.tabs.addTab(self.tab5, "")

# NOTIFICATION BAR SA RIGHT
        self.notifications = QtWidgets.QGroupBox(self.centralwidget)
        self.notifications.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")
        self.notifications.setGeometry(QtCore.QRect(600, 74, 193, 468))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.notifications.setFont(font)
        self.notifications.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.notifications.setObjectName("notifications")

        self.groupBox = QtWidgets.QGroupBox(self.notifications)
        self.groupBox.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 171, 200))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.nRequestApproval = QtWidgets.QTableWidget(self.groupBox)
        self.nRequestApproval.setGeometry(QtCore.QRect(10, 20, 151, 171))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)

        self.nRequestApproval.setFont(font)
        self.nRequestApproval.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.nRequestApproval.setObjectName("nRequestApproval")
        self.nRequestApproval.setColumnCount(2)
        self.nRequestApproval.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.nRequestApproval.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.nRequestApproval.setHorizontalHeaderItem(1, item)
        self.nRequestApproval.horizontalHeader().setDefaultSectionSize(74)

        self.groupBox_2 = QtWidgets.QGroupBox(self.notifications)
        self.groupBox_2.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")
        self.groupBox_2.setGeometry(QtCore.QRect(10, 245, 171, 200))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.nWithdrawed = QtWidgets.QTableWidget(self.groupBox_2)
        self.nWithdrawed.setGeometry(QtCore.QRect(10, 20, 151, 171))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)

        self.nWithdrawed.setFont(font)
        self.nWithdrawed.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.nWithdrawed.setObjectName("nWithdrawed")
        self.nWithdrawed.setColumnCount(2)
        self.nWithdrawed.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.nWithdrawed.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.nWithdrawed.setHorizontalHeaderItem(1, item)
        self.nWithdrawed.horizontalHeader().setDefaultSectionSize(74)

        self.nSetDaysInBetween = QtWidgets.QSpinBox(self.centralwidget)
        self.nSetDaysInBetween.setGeometry(QtCore.QRect(630, 40, 46, 22))
        self.nSetDaysInBetween.setObjectName("nSetDaysInBetween")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")
        self.label.setGeometry(QtCore.QRect(610, 20, 181, 16))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")
        self.label_2.setGeometry(QtCore.QRect(680, 43, 91, 16))
        self.label_2.setObjectName("label_2")

        self.nRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.nRefresh.setStyleSheet("color: black;"
                        "background-color: #FCE1E4")
        self.nRefresh.setGeometry(QtCore.QRect(597, 542, 198, 28))
        self.nRefresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nRefresh.setObjectName("nRefresh")
        root.setCentralWidget(self.centralwidget)

        self.retranslateUi(root)
        self.tabs.setCurrentIndex(0)
        self.cClear.clicked.connect(self.cIDInput.clear)
        self.cClear.clicked.connect(self.cFirstNameInput.clear)
        self.cClear.clicked.connect(self.cLastNameInput.clear)
        self.cClear.clicked.connect(self.cDescripInput.clear)
        self.cClear.clicked.connect(self.cExpiryInput.showToday)
        self.cSubmit.clicked.connect(self.cExpiryInput.showToday)
        QtCore.QMetaObject.connectSlotsByName(root)

        # HOME CALLING

        self.aboutUs.mousePressEvent = self.hAboutUs

        # >> CREATE CALLING <<

        # Button to add product
        self.cSubmit.clicked.connect(self.auxAddProduct)

        # >> READ CALLING <<

        # Make text fields uneditable
        self.rReadFirstName.setReadOnly(True)
        self.rReadLastName.setReadOnly(True)
        self.rReadDescrip.setReadOnly(True)
        self.rReadExpiry.setReadOnly(True)

        # Find from database by ID
        self.rSearch.clicked.connect(self.findProduct)

        # Refresh read table data
        self.tableProduct()
        self.rRefresh.clicked.connect(self.tableProduct)

        # >> UPDATE CALLING <<

        # Search product
        self.uSearch.clicked.connect(self.uSearchSet)
        self.uCancel.clicked.connect(self.uSearchSet)

        # Update the product
        self.uDone.clicked.connect(self.uConfirmation)

        # >> DELETE CALLING <<

        # This shows contents for deletion of a row
        self.dSearch.clicked.connect(self.dShowContents)

        # Clicks button to delete item
        self.dDelete.clicked.connect(self.dConfirmation)

        # >> NOTIFICATIONS CALLING <<

        # Notifications Refresh
        self.nRefresh.clicked.connect(self.nExpiryWarning)
        self.nRefresh.clicked.connect(self.nWithdrawn)

# Fixation of Texts
    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "MILKY WAY MILK BANK MANAGEMENT SYSTEM"))
#CREATE
        self.aboutUs.setText(_translate("root",
                                        "<html><head/><body><p><span style=\" font-style:italic; color:#5500ff;\">About Us</span></p></body></html>"))
        self.tabs.setTabText(self.tabs.indexOf(self.home), _translate("root", "Home"))
        self.cID.setText(_translate("root", "MILK ID:"))
        self.cFirstName.setText(_translate("root", "First Name:"))
        self.cLastName.setText(_translate("root", "Last Name:"))
        self.cDescrip.setText(_translate("root", "Description:"))
        self.cExpiry.setText(_translate("root", "Expiry date:"))
        self.cClear.setText(_translate("root", "Clear"))
        self.cSubmit.setText(_translate("root", "Submit"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab2), _translate("root", "Donate Milk"))

        item = self.rTable.horizontalHeaderItem(0)
        item.setText(_translate("root", "MILK ID"))
        item = self.rTable.horizontalHeaderItem(1)
        item.setText(_translate("root", "First Name"))
        item = self.rTable.horizontalHeaderItem(2)
        item.setText(_translate("root", "Last Name"))
        item = self.rTable.horizontalHeaderItem(3)
        item.setText(_translate("root", "Description"))
        item = self.rTable.horizontalHeaderItem(4)
        item.setText(_translate("root", "Expiry Date"))
#READ
        self.rFind.setText(_translate("root", "Enter MILK ID:"))
        self.rSearch.setText(_translate("root", "Search"))
        self.rFirstName.setText(_translate("root", "First Name:"))
        self.rLastName.setText(_translate("root", "Last Name:"))
        self.rExpiry.setText(_translate("root", "Expiry date:"))
        self.rDescription.setText(_translate("root", "Description:"))
        self.rRefresh.setText(_translate("root", "Refresh"))
        self.rRemind.setText(_translate("root", "Can\'t see your product? Find it by MILK ID"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab3), _translate("root", "View Database"))
#UPDATE
        self.uID.setText(_translate("root", "Enter MILK ID:"))
        self.uFirstName.setText(_translate("root", "First Name:"))
        self.uLastName.setText(_translate("root", "Last Name:"))
        self.uDescrip.setText(_translate("root", "Description:"))
        self.uExpiry.setText(_translate("root", "Expiry date:"))
        self.uSearch.setText(_translate("root", "Search"))
        self.uSmallLabel.setText(_translate("root", "Edit product below"))
        self.uDone.setText(_translate("root", "Done"))
        self.uCancel.setText(_translate("root", "Cancel"))
#DELETE
        self.tabs.setTabText(self.tabs.indexOf(self.tab4), _translate("root", "Edit Info    "))
        self.dID.setText(_translate("root", "Enter MILK ID:"))
        self.dSearch.setText(_translate("root", "Search"))
        self.dContents.setText(_translate("root", "Product contents"))
        self.dFirstName.setText(_translate("root", "First Name:"))
        self.dLastName.setText(_translate("root", "Last Name:"))
        self.dDescrip.setText(_translate("root", "Description:"))
        self.dExpiry.setText(_translate("root", "Expiry date:"))
        self.dDelete.setText(_translate("root", "Withdraw Milk"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab5), _translate("root", "Withdraw Milk"))
        self.notifications.setTitle(_translate("root", "Notifications"))
        self.groupBox.setTitle(_translate("root", "Expiry Warning"))

        item = self.nRequestApproval.horizontalHeaderItem(0)
        item.setText(_translate("root", "ID"))
        item = self.nRequestApproval.horizontalHeaderItem(1)
        item.setText(_translate("root", "Name"))
        self.groupBox_2.setTitle(_translate("root", "To be Withdrawn"))
        item = self.nWithdrawed.horizontalHeaderItem(0)
        item.setText(_translate("root", "ID"))
        item = self.nWithdrawed.horizontalHeaderItem(1)
        item.setText(_translate("root", "Name"))
        self.label.setText(_translate("root", "Milk Expiry"))
        self.label_2.setText(_translate("root", "days from now"))
        self.nRefresh.setText(_translate("root", "Refresh"))

    # >> HOME FUNCTIONALITY

    def hAboutUs(self, event):
        msg = QMessageBox()
        msg.setWindowTitle("About Us")
        msg.setIcon(QMessageBox.Information)
        t1 = "This GUI was designed by the students of CPE21S3 under the supervision of Engr. Jonathan Vidal Taylar of"
        t2 = "Technological Institute of the Philippines - Quezon City, Group 2. School Year 2022-2023. "
        t3 = "Simply click the button bellow to check the creators of this project "
        t4 = "\n\nCopyright 2022, MILKY WAY, All Rights Reserved."
        msg.setText(t1 + t2 + t3 + t4)

        a = "Sheina Mae De Leon\n"
        b = "Ashley Joshua Agato\n"
        c = "Charizze Mendoza\n"
        d = "Vincent Gon Serrano\n"
        e = "Iris Villanueva\n"
        members = a + b +c + d + e

        msg.setDetailedText(members)

        msg.exec_()

    # >> CREATE FUNCTIONALITY <<

    # Tells the user that the item is added successfully
    def cMessage(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Product added successfully!")
        msg.exec_()

    # Add product to database
    def auxAddProduct(self):
        date = self.cExpiryInput.selectedDate()
        now = QDate.currentDate()
        expiryYear = date.year()
        expiryDay = date.dayOfYear()
        currentYear = now.year()
        currentDay = now.dayOfYear()

        a = self.cIDInput.text()
        b = self.cFirstNameInput.text()
        c = self.cLastNameInput.text()
        d = self.cDescripInput.toPlainText()
        e = date.toString()

        if expiryYear > currentYear:
            f = now.daysTo(date)
        elif expiryYear == currentYear:
            f = expiryDay - currentDay
        elif expiryYear < currentYear:
            f = now.daysTo(date)
            f *= -1

        addProduct(a, b, c, d, e, f)

        self.cMessage()
        self.cIDInput.setText('')
        self.cFirstNameInput.setText('')
        self.cLastNameInput.setText('')
        self.cDescripInput.setText('')

    # >> READ FUNCTIONALITY <<

    # Read: Database to table
    def tableProduct(self):
        allData = readProductTable()
        self.rTable.setRowCount(0)

        for rowNumber, rowData in enumerate(allData):
            self.rTable.insertRow(rowNumber)
            for columnNumber, data in enumerate(rowData):
                self.rTable.setItem(rowNumber, columnNumber,
                                    QtWidgets.QTableWidgetItem(str(data)))

    # Read: Find to database
    def findProduct(self):
        a = self.rFindInput.text()
        findRow = readProductFind(a)
        try:
            self.rReadFirstName.setText(findRow[1])
            self.rReadLastName.setText(findRow[2])
            self.rReadDescrip.setPlainText(findRow[3])
            self.rReadExpiry.setText(findRow[4])
        except:
            msg = QMessageBox()
            msg.setWindowTitle("An error occured")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Product ID is not found!")
            msg.exec_()

    # >> UPDATE FUNCTIONALITY <<

    # Asks the user if they are sure about the data update
    def uConfirmation(self):
        msg = QMessageBox()
        msg.setWindowTitle("Product update confirmation")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Are you sure you want to update this product?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        choice = msg.exec_()

        if choice == QMessageBox.Yes:
            self.updateConfirmed()

    # Tells the user that product is updated successfully
    def updateConfirmed(self):
        self.updatePasser()
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Product updated successfully!")
        msg.exec_()

        self.uIDInput.setText('')
        self.uFirstNameInput.setText('')
        self.uLastNameInput.setText('')
        self.uDescripInput.setPlainText('')

    # Passes the arguments on to the function
    def updatePasser(self):
        date = self.uCalendar.selectedDate()
        now = QDate.currentDate()
        expiryYear = date.year()
        expiryDay = date.dayOfYear()
        currentYear = now.year()
        currentDay = now.dayOfYear()

        pId = self.uIDInput.text()
        a = self.uFirstNameInput.text()
        b = self.uLastNameInput.text()
        c = self.uDescripInput.toPlainText()
        d = date.toString()

        if expiryYear > currentYear:
            e = now.daysTo(date)
        elif expiryYear == currentYear:
            e = expiryDay - currentDay
        elif expiryYear < currentYear:
            e = now.daysTo(date)
            e *= -1

        confirmEdit(pId, a, b, c, d, e)

    # Sets text inputs
    def uSearchSet(self):
        a = self.uIDInput.text()
        setEdits = editShow(a)

        try:
            self.uFirstNameInput.setText(setEdits[1])
            self.uLastNameInput.setText(setEdits[2])
            self.uDescripInput.setText(setEdits[3])
        except:
            msg = QMessageBox()
            msg.setWindowTitle("An error occured")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Product ID is not found!")
            msg.exec_()

    # >> DELETE FUNCTIONALITY <<

    # Asks if you are sure about the deletion
    def dConfirmation(self):
        msg = QMessageBox()
        msg.setWindowTitle("Delete confirmation")
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete this product?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        choice = msg.exec_()

        if choice == QMessageBox.Yes:
            self.dConfirmed()

    def dConfirmed(self):
        self.deleteItem()
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Product deleted successfully!")
        msg.exec_()

        self.dIDInput.setText('')
        self.dFirstNameInput.setText('')
        self.dLastNameInput.setText('')
        self.dDescripInput.setText('')
        self.dExpiryInput.setText('')

    # DELETE: This functions shows contents for deleting a data in a table
    def dShowContents(self):
        a = self.dIDInput.text()
        findRow = readProductFind(a)

        try:
            self.dFirstNameInput.setText(findRow[1])
            self.dLastNameInput.setText(findRow[2])
            self.dDescripInput.setPlainText(findRow[3])
            self.dExpiryInput.setText(findRow[4])
        except:
            msg = QMessageBox()
            msg.setWindowTitle("An error occured")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Product ID is not found!")
            msg.exec_()

    # This function deletes the product after clicking delete button
    def deleteItem(self):
        a = self.dIDInput.text()
        deleteData = deleteRow(a)

    # >> NOTIFICATIONS FUNCTIONALITY <<

    # Calls the warning function from the other side
    def nExpiryWarning(self):
        while self.nRequestApproval.rowCount() > 0:
            self.nRequestApproval.removeRow(0)

        allData = nExpiryWarningShow(self.nSetDaysInBetween.value())

        for rowNumber, rowData in enumerate(allData):
            self.nRequestApproval.insertRow(rowNumber)
            for columnNumber, data in enumerate(rowData):
                self.nRequestApproval.setItem(rowNumber, columnNumber,
                                      QtWidgets.QTableWidgetItem(str(data)))

    # Calls the withdrawed function from the other side
    def nWithdrawn(self):
        while self.nWithdrawed.rowCount() > 0:
            self.nWithdrawed.removeRow(0)

        allData = nWithdrawnShow(self.nSetDaysInBetween.value())

        for rowNumber, rowData in enumerate(allData):
            self.nWithdrawed.insertRow(rowNumber)
            for columnNumber, data in enumerate(rowData):
                self.nWithdrawed.setItem(rowNumber, columnNumber,
                                      QtWidgets.QTableWidgetItem(str(data)))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
