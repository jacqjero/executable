

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi


class MonAppli(QMainWindow):
    def __init__(self):
        super(MonAppli, self).__init__()
        loadUi('UIMonAppli.ui', self)

        # Lecture et affichage du contenu du 1er fichier
        with open('UnFichierTexte.txt', 'r') as f:
            texte1 = f.read()

        self.TE_Fichier1.setText(texte1)

        # Callback
        self.PB_Fichier2.clicked.connect(self.lireAutreFichier)


    def lireAutreFichier(self):
        # Sélection du fichier
        ficAutre, _ = QFileDialog.getOpenFileName(self, 'Selectionner un autre fichier ...', '', '*.txt')

        # Si Annuler
        if len(ficAutre) == 0:
            return

        # Affichae du nom du fichier
        self.LE_Fichier2.setText(ficAutre)

        # Lecture et affichage du contenu du 2ème fichier
        with open(ficAutre) as f:
            texte2 = f.read()

        self.TE_Fichier2.setText(texte2)



# %% Main
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = MonAppli()
    ui.show()
    sys.exit(app.exec_())