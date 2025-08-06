import tkinter as tk
from tkinter import ttk
from controller.controller import Controller
from model.screen import Screen
from model.location import Location
from tkinter import messagebox

# width scaling relative to monitor (set in MainView)
try:
    from view.main_view import CHAR_SCALE
except Exception:
    CHAR_SCALE = 1.0

def _w(val:int)->int:
    """scale character width keeping a sensible minimum"""
    return max(5, int(val*CHAR_SCALE))

class ScreenFrame(tk.Frame):
	"""
	The view for each individual screen, inherits from tk.Frame.
	"""

	def __init__(self, parent, controller: Controller, screen: Screen, select_callback=None):
		super().__init__(parent)
		self.controller = controller
		self.screen = screen
		self.entries = {}
		self.editing = False
		self.select_callback = select_callback
		self.selected_var = tk.BooleanVar(value=False)

		# Allow the frame to size itself to its contents
		self.config(bg="#cccccc")
		self.grid_propagate(True)

		# Initialize ttk styles for editable widgets
		self._init_styles()

		self._build_form()

	def _init_styles(self):
		"""
		Initializes custom ttk styles used to highlight editable widgets.
		"""
		style = ttk.Style()
		style.configure('Editing.TEntry', fieldbackground='#ffffcc')
		style.configure('Editing.TCombobox', fieldbackground='#ffffcc')

	def _build_form(self):
		"""
		Builds the actual frame (without labels).
		"""
		padx, pady = 1, 2
		# selection checkbox
		cb = tk.Checkbutton(self, variable=self.selected_var, command=lambda: self._on_selected())
		cb.grid(row=0, column=0, padx=padx, pady=pady)
		column = 1

		self.design_str = tk.StringVar(value=self.screen.design)
		self.design_entry = ttk.Entry(self, textvariable=self.design_str, state="readonly", width=_w(38))
		self.design_entry.grid(row=0, column=column, padx=padx, pady=pady, sticky="ew")
		column += 1

		self.customer_str = tk.StringVar(value=self.screen.customer)
		self.customer_entry = ttk.Entry(self, textvariable=self.customer_str, state="readonly", width=_w(39))
		self.customer_entry.grid(row=0, column=column, padx=padx, pady=pady, sticky="ew")
		column += 1

		self.quantity_str = tk.StringVar(value=str(self.screen.quantity))
		self.quantity_entry = ttk.Entry(self, textvariable=self.quantity_str, state="readonly", width=5)
		self.quantity_entry.grid(row=0, column=column, padx=padx, pady=pady, sticky="ew")
		column += 1

		self.description_str = tk.StringVar(value=self.screen.description)
		self.description_entry = ttk.Entry(self, textvariable=self.description_str, state="readonly", width=_w(55))
		self.description_entry.grid(row=0, column=column, padx=padx, pady=pady, sticky="ew")
		column += 1

		self.in_use_var = tk.BooleanVar(value=self.screen.in_use)
		self.in_use_check = ttk.Checkbutton(self, variable=self.in_use_var, state="disabled")
		self.in_use_check.grid(row=0, column=column, padx=padx, pady=pady)
		column += 1

		# Location dropdown
		self.location_map = {loc.description: loc for loc in self.controller.locations.values()}
		location_names = list(self.location_map.keys())

		current_location = ""
		if self.screen.location_id in self.controller.locations:
			current_location = self.controller.locations[self.screen.location_id].description

		self.location_var = tk.StringVar(value=current_location)
		self.location_dropdown = ttk.Combobox(
			self,
			textvariable=self.location_var,
			values=location_names,
			state="disabled",
			width=3
		)

		self.location_dropdown.grid(row=0, column=column, padx=padx, pady=pady)
		column += 1

		# Action buttons
		self.save_button = ttk.Button(self, text="Save", command=self.save_changes, state="disabled", width=_w(6))
		self.save_button.grid(row=0, column=column, padx=padx, pady=pady)
		column += 1

		self.edit_button = ttk.Button(self, text="Edit", command=self.toggle_edit, width=_w(8))
		self.edit_button.grid(row=0, column=column, padx=padx, pady=pady)
		column += 1
		column += 1

		self.delete_button = ttk.Button(self, text="Delete", command=self.delete_screen, width=_w(8))
		self.delete_button.grid(row=0, column=column, padx=padx, pady=pady)

	def _on_selected(self):
		"""Callback from checkbox toggled."""
		if self.select_callback:
			self.select_callback(self.screen, bool(self.selected_var.get()))

	def toggle_edit(self):
		"""
		Toggles the edit mode.
		"""
		self.editing = not self.editing
		if not self.editing:
			self.design_str.set(self.screen.design)
			self.customer_str.set(self.screen.customer)
			self.quantity_str.set(str(self.screen.quantity))
			self.description_str.set(self.screen.description)
			self.in_use_var.set(self.screen.in_use)
			
			current_location = ""
			if self.screen.location_id in self.controller.locations:
				current_location = self.controller.locations[self.screen.location_id].description
			self.location_var.set(current_location)

		# Set state and styling based on edit mode
		state = "normal" if self.editing else "readonly"
		entry_style = "Editing.TEntry" if self.editing else "TEntry"
		combobox_style = "Editing.TCombobox" if self.editing else "TCombobox"

		# Update entry widgets
		for entry in [self.design_entry, self.customer_entry, self.quantity_entry, self.description_entry]:
			entry.configure(state=state, style=entry_style)
		# Ensure columns expand when frame stretches
		for idx in range(self.grid_size()[0]):
			self.columnconfigure(idx, weight=1 if idx < 5 else 0)

		# Update other widgets
		self.in_use_check.configure(state="normal" if self.editing else "disabled")
		self.location_dropdown.configure(state="readonly" if self.editing else "disabled", style=combobox_style)
		self.save_button.configure(state="normal" if self.editing else "disabled")
		self.edit_button.configure(text="Cancel" if self.editing else "Edit")

	def save_changes(self):
		"""
		"""
		if self.validate_entries():
			self.screen.design = self.design_str.get().strip()
			self.screen.customer = self.customer_str.get().strip()
			self.screen.description = self.description_str.get().strip()
			self.screen.quantity = int(self.quantity_str.get().strip())
			self.screen.in_use = bool(self.in_use_var.get())
			selected_location_name = self.location_var.get()
			self.screen.location_id = self.location_map[selected_location_name].location_id

			self.screen.add_to_db(self.controller.connection)

			self.toggle_edit()
			self.controller.update_screens_and_locations()

	def delete_screen(self):
		result = messagebox.askyesno("Delete Screen", f'Are you sure you want to delete "{self.screen.design}"?\nThis action cannot be undone.')
		if result:
			if self.editing:
				self.toggle_edit()
			self.screen.delete_from_db(self.controller.connection)
			self.controller.update_screen_list()
			self.destroy()

	def validate_entries(self) -> bool:
		"""
		Validates the form fields.

		Returns:
			bool: True if all fields are valid, False otherwise.
		"""
		if not self.design_str.get().strip():
			messagebox.showerror("Validation Error", "Design cannot be empty.")
			return False

		if not self.customer_str.get().strip():
			messagebox.showerror("Validation Error", "Customer cannot be empty.")
			return False

		if not self.description_str.get().strip():
			messagebox.showerror("Validation Error", "Description cannot be empty.")
			return False

		quantity_val = self.quantity_str.get().strip()
		if not quantity_val:
			messagebox.showerror("Validation Error", "Quantity cannot be empty.")
			return False
		if not quantity_val.isdigit():
			messagebox.showerror("Validation Error", "Quantity must be an integer.")
			return False

		if not self.location_var.get().strip():
			messagebox.showerror("Validation Error", "Location must be selected.")
			return False

		return True
