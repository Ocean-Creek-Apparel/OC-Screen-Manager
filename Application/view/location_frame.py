"""location_frame.py
A frame representing a single location and its associated screens.
Each LocationFrame shows a heading label and dynamically creates a
ScreenFrame for every screen stored in the given location.
"""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from controller.controller import Controller
from model.location import Location
from model.screen import Screen
from .screen_frame import ScreenFrame

class LocationFrame(tk.Frame):
    """
    UI component that groups screens by location.
    """

    def __init__(self, parent: tk.Widget, controller: Controller, location: Location, screens: list[Screen], select_callback=None):
        super().__init__(parent)
        self.controller = controller
        self.location = location
        self.screens = screens
        self.select_callback = select_callback

        # Styling bold title for location header
        header_bg = self.cget("bg")
        header = tk.Label(
            self,
            text=f"LOCATION: {self.location.description}",
            font=("Segoe UI", 10, "bold"),
            bg=header_bg
        )
        header.pack(anchor="w", padx=2, pady=(4, 2))

        # Build individual ScreenFrames
        for screen in self.screens:
            sf = ScreenFrame(self, controller, screen, select_callback=self.select_callback)
            sf.pack(anchor="w", pady=1, padx=20)