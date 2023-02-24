from my_lib.control import *

if __name__ == '__main__':
    from qt_material import apply_stylesheet
    import sys
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    myWin = Main_Widget()
    myWin.show()
    sys.exit(app.exec_())