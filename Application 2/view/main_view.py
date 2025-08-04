import tkinter as tk
from tkinter import ttk
from controller.controller import Controller

class MainView():
    """
    The main application window.

    Attributes:
        controller (Controller): the controller for this instance of the program.
    """

    def __init__(self, controller: Controller):
        """
        Initializes the main view.
        
        Arguments:
            controller (Controller): the controller for this instance.
        """
        super().__init__()
        self.controller = Controller

        self.title('Screen Locator')
        self.state('Zoomed')