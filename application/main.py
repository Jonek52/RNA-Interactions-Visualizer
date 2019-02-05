'''
@Authors: Jakub Kuligowicz,Jonasz Romanowski and Amadeusz Zieba
'''

from app import *

def main():

    app = QApplication(sys.argv)
    window= App()
    sys.exit(app.exec_())
    return

main()
