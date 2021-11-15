from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
import xlrd
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

wb=xlrd.open_workbook("医院数据.xls")

province_name = [
        '北京市', '天津市', '河北省', '山西省', '辽宁省', '吉林省', '黑龙江省', '上海市', 
        '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', 
        '湖南省', '广东省', '内蒙古自治区', '广西壮族自治区', '海南省', '重庆市', '四川省', '贵州省',
        '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区'
    ]
value=["医院名称", "医院地址", "联系电话", "医院等级", "重点科室", "经营方式", "传真号码", "电子邮箱", "医院网站"]
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python36\0_eric_project\test1\hello.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #整体
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 350)

        #界面
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        #按钮
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 220, 93, 28)) #起始位置、宽高
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 220, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 300, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        #网站提示文本
        self.label_1 = QtWidgets.QLabel(self.centralWidget)
        self.label_1.setGeometry(QtCore.QRect(142, 280, 300, 15))
        self.label_1.setObjectName("label_1")

        #输出文本框
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 160, 250, 21))
        self.lineEdit.setObjectName("lineEdit")

        #
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(300, 305, 200, 15))
        self.label_5.setObjectName("label_5")
        

        #提示文本
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(300, 140, 200, 15))
        self.label.setObjectName("label")

        

        #下拉选项框
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 60, 100, 22))
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 60, 200, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        self.comboBox_3 = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_3.setGeometry(QtCore.QRect(100, 160, 100, 22))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(100, 140, 72, 15))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(100, 40, 72, 15))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(300, 40, 72, 15))
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "全国医院信息检索"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.pushButton_3.setText(_translate("MainWindow", "访问医院网站"))
        self.label.setText(_translate("MainWindow", "结果："))
        self.label_1.setText(_translate("MainWindow", "点击进入该医院网站"))
        self.label_2.setText(_translate("MainWindow", "检索信息"))
        self.label_3.setText(_translate("MainWindow", "选择省份"))
        self.label_4.setText(_translate("MainWindow", "选择医院"))
        #self.Label.setStyleSheet(font-size:60px)
        #self.Label.setText(_translate("MainWindow", "全国医院信息检索"))


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 初始化省
        self.comboBox.clear()  # 清空items
        self.comboBox.addItem('请选择')
        '''for k, v in dictProvince.items():
            self.comboBox.addItem(v, k)  # 键、值反转'''
        for v in province_name:
            self.comboBox.addItem(v)

    #@pyqtSlot(int)
    # 取市的键值
    def on_comboBox_activated(self):
        sheet_index=self.comboBox.currentIndex()-1
        #sheet_name=province_name[sheet_index]+'医院列表'
        #print(sheet_index)
        sheet=wb.sheets()[sheet_index]

        List=sheet.col_values(0)[3:]
        #print(List)
        self.comboBox_2.clear()
        self.comboBox_2.addItem('请选择')

        for v in List:
            self.comboBox_2.addItem(v)
        '''key = self.comboBox.itemData(index)
        print(key)
        self.comboBox_2.clear()  # 清空items
        if key:
            self.comboBox_2.addItem('请选择')
            # 初始化市
            for k, v in dictCity[key].items():
                self.comboBox_2.addItem(v)  # 键、值反转'''

    
    def on_comboBox_2_activated(self):
        

        self.comboBox_3.clear()
        self.comboBox_3.addItem('请选择')

        for v in value:
            self.comboBox_3.addItem(v)


    #@pyqtSlot()
    def on_pushButton_clicked(self):
        _translate = QtCore.QCoreApplication.translate
        #获取当前选项框索引(注意：‘请选择’也占一项）
        sheet_index=self.comboBox.currentIndex()-1
        sheet=wb.sheets()[sheet_index]

        hospital_index=self.comboBox_2.currentIndex()+3-1
        value_index=self.comboBox_3.currentIndex()-1
       
        Value=sheet.cell(hospital_index,value_index).value
        if Value=='':
            Value='暂无数据'

        #print(hospital_index,value_index,Value)
        #print(str(self.comboBox.currentText())+" "+str(self.comboBox_2.currentText())+" "+str(self.comboBox_3.currentText()))
        self.label.setText(_translate("MainWindow", str(self.comboBox.currentText())+" "+str(self.comboBox_2.currentText())+" "+str(self.comboBox_3.currentText())))
        self.lineEdit.setText(Value)

    #@pyqtSlot()
    def on_pushButton_3_pressed(self):
        _translate = QtCore.QCoreApplication.translate
        #获取当前选项框索引(注意：‘请选择’也占一项）
        sheet_index=self.comboBox.currentIndex()-1
        sheet=wb.sheets()[sheet_index]

        hospital_index=self.comboBox_2.currentIndex()+3-1
        
       
        Value=sheet.cell(hospital_index,8).value
        if Value=='':
            self.label_5.setText(_translate("MainWindow", "该医院网站数据缺失"))
        else:
            print(Value)
            QDesktopServices.openUrl(QUrl(Value))
            self.label_5.setText(_translate("MainWindow", ""))
            

        #print(hospital_index,value_index,Value)
        #print(str(self.comboBox.currentText())+" "+str(self.comboBox_2.currentText())+" "+str(self.comboBox_3.currentText()))
        #self.label.setText(_translate("MainWindow", str(self.comboBox.currentText())+" "+str(self.comboBox_2.currentText())+" "+str(self.comboBox_3.currentText())))
        #self.lineEdit.setText(Value)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    #ui.on_comboBox3_activated()
    ui.show()
    sys.exit(app.exec_())
