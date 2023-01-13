from PyQt5.QtWidgets import QWidget, QHBoxLayout, QScrollArea, QVBoxLayout, QMenuBar, QMainWindow, QAction
from PyQt5.QtWidgets import QMenu
import json, os
from Widgets.Sections.CentralWidget import CentralWidget
from Widgets.Sections.TopBar import TopBar
from Widgets.Sections.LogicGateContainer import LogicGateContainer
from Widgets.Sections.LogicGateMenu import LogicGateMenu
from pathlib import Path
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simulator porti logice")
        self.setGeometry(0, 0, 800, 600)
        self.setCentralWidget(CentralWidget())

        self._createMenuBar()
        self._connectMenuBarToActions()

        self.show()

    def createNewProject(self):
        print("Creare proiect nou")
        self.centralWidget().logicGateContainer.removeAllGates()

    def saveProject(self):
        projectContent = self.centralWidget().logicGateContainer.generateProjectContent()
        file_path = 'saves/save-test.json'

        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        with open(file_path, "w+") as outfile:
            json.dump(projectContent, outfile)

    def loadProject(self):
        file_path = 'saves/save-test.json'

        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        with open(file_path, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)

        self.centralWidget().logicGateContainer.loadProjectContent(json_object)

    def showHelp(self):
        print("Afisare ajutor")

    def showAbout(self):
        print("Afisare despre")

    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

    def _connectMenuBarToActions(self):
        menuBar = self.menuBar()


        # Meniu proiect
        projectMenu = QMenu("&Proiect", self)

        self.newProjectAction = QAction("Nou")
        self.newProjectAction.triggered.connect(self.createNewProject)

        self.saveProjectAction = QAction("Salvează")
        self.saveProjectAction.triggered.connect(self.saveProject)

        self.loadProjectAction = QAction("Încarcă")
        self.loadProjectAction.triggered.connect(self.loadProject)

        projectMenu.addAction(self.newProjectAction)
        projectMenu.addAction(self.saveProjectAction)
        projectMenu.addAction(self.loadProjectAction)
        menuBar.addMenu(projectMenu)


        # Meniu ajutor
        helpMenu = menuBar.addMenu("&Ajutor")

        self.helpAction = QAction("Ajutor")
        self.helpAction.triggered.connect(self.showHelp)

        self.aboutAction = QAction("Despre")
        self.aboutAction.triggered.connect(self.showAbout)

        helpMenu.addAction(self.helpAction)
        helpMenu.addAction(self.aboutAction)
