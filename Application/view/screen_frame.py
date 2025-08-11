import tkinter as tk
from tkinter import ttk
from controller.controller import Controller
from model.screen import Screen
from model.location import Location
from tkinter import messagebox

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

		# change background based on if screen is in use
		self.in_use_color = "#eb5d44"
		self.not_in_use_color = "#75e858"

		# Allow the frame to size itself to its contents
		self.grid_propagate(True)

		# Initialize ttk styles for editable widgets and build the form
		self._init_styles()
		self._build_form()

	def _init_styles(self) -> None:
		"""
		Initializes custom ttk styles used to highlight editable widgets.
		"""
		style = ttk.Style()
		style.configure('Editing.TEntry', fieldbackground="#717171")
		style.configure('Editing.TCombobox', fieldbackground='#ffffcc')

	def _build_form(self) -> None:
		"""
		Builds the actual frame (without labels).
		"""
		padx, pady = 1, 2

		# selection checkbox
		cb = tk.Checkbutton(self, variable=self.selected_var, command=lambda: self._on_selected())
		cb.grid(row=0, column=0, padx=padx, pady=pady)
		column = 1

		self.design_str = tk.StringVar(value=self.screen.design)
		self.design_entry = ttk.Entry(self, textvariable=self.design_str, state="readonly", width=38)
		self.design_entry.grid(row=0, column=column, padx=padx, pady=pady, sticky="ew")
		column += 1

		self.customer_str = tk.StringVar(value=self.screen.customer)
		self.customer_entry = ttk.Entry(self, textvariable=self.customer_str, state="readonly", width=35)
		self.customer_entry.grid(row=0, column=column, padx=padx, pady=pady, sticky="ew")
		column += 1

		self.quantity_str = tk.StringVar(value=str(self.screen.quantity))
		self.quantity_entry = ttk.Entry(self, textvariable=self.quantity_str, state="readonly", width=5)
		self.quantity_entry.grid(row=0, column=column, padx=padx, pady=pady, sticky="ew")
		column += 1

		self.description_str = tk.StringVar(value=self.screen.description)
		self.description_entry = ttk.Entry(self, textvariable=self.description_str, state="readonly", width=48)
		self.description_entry.grid(row=0, column=column, padx=padx, pady=pady, sticky="ew")
		column += 1

		self.in_use_var = tk.BooleanVar(value=self.screen.in_use)
		self.in_use_check = ttk.Checkbutton(self, text="In Use", variable=self.in_use_var, command=self.in_use_check_clicked, state="normal")
		self.in_use_check.grid(row=0, column=column, padx=padx, pady=pady)
		column += 1

		# Location dropdown
		self.location_map = {loc.description: loc for loc in self.controller.locations.values()}
		location_names = list(self.location_map.keys())

		current_location = ""
		if self.screen.location_id in self.controller.locations:
			current_location = self.controller.locations[self.screen.location_id].description

		self.location_var = tk.StringVar(value=current_location)
		# Calculate width based on longest location name (minimum width of 5, max of 11)
		max_location_width = max([len(loc) for loc in location_names]) if location_names else 5
		max_location_width = min(11, max(5, max_location_width))  # Ensure min/max width
		
		self.location_dropdown = ttk.Combobox(
			self,
			textvariable=self.location_var,
			values=location_names,
			state="disabled",
			width=max_location_width
		)

		self.location_dropdown.grid(row=0, column=column, padx=padx, pady=pady)
		column += 1

		# Action buttons
		self.save_button = ttk.Button(self, text="Save", command=self.save_changes, state="disabled", width=6)
		self.save_button.grid(row=0, column=column, padx=padx, pady=pady)
		column += 1

		self.edit_button = ttk.Button(self, text="Edit", command=self.toggle_edit, width=8)
		self.edit_button.grid(row=0, column=column, padx=padx, pady=pady)
		column += 1
		column += 1

		self.delete_button = ttk.Button(self, text="Delete", command=self.delete_screen, width=8)
		self.delete_button.grid(row=0, column=column, padx=padx, pady=pady)

		self.toggle_bg_color()

	def _on_selected(self) -> None:
		"""
		Callback from checkbox toggled.
		"""
		if self.select_callback:
			self.select_callback(self.screen, bool(self.selected_var.get()))

	def toggle_edit(self) -> None:
		"""
		Toggles the edit mode.
		"""
		self.editing = not self.editing
		# reset all entries/comboboxes/checkboxes to their prior state
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

			self.toggle_bg_color()

		# Set state and styling based on edit mode
		state = "normal" if self.editing else "readonly"
		entry_style = "Editing.TEntry" if self.editing else "TEntry"
		combobox_style = "Editing.TCombobox" if self.editing else "TCombobox"

		# Update entry widgets to proper state
		for entry in [self.design_entry, self.customer_entry, self.quantity_entry, self.description_entry]:
			entry.configure(state=state, style=entry_style)
		# Ensure columns expand when frame stretches
		for idx in range(self.grid_size()[0]):
			self.columnconfigure(idx, weight=1 if idx < 5 else 0)

		# Update other widgets to correct state
		self.location_dropdown.configure(state="readonly" if self.editing else "disabled", style=combobox_style)
		self.save_button.configure(state="normal" if self.editing else "disabled")
		self.edit_button.configure(text="Cancel" if self.editing else "Edit")


	def save_changes(self) -> None:
		"""
		Validates entries and then updates the corresponding record in the DB.
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

	def in_use_check_clicked(self) -> None:
		"""
		Changes background based on if the screen is in use. If the user is not currently editing, this change is immediately written to the database.
		"""
		if not self.editing:
			self.screen.in_use = not self.screen.in_use
			self.screen.add_to_db(self.controller.connection)
			self.toggle_bg_color()
			

	def delete_screen(self) -> None:
		"""
		Prompts for confirmation of deletion, deletes from DB on confirmation and destroys the ScreenFrame.
		"""
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
	
	def toggle_bg_color(self) -> None:
		"""
		Changes background to green if not in use, red if in use.
		"""
		if self.screen.in_use:
			self.config(bg=self.in_use_color)
		else:
			self.config(bg=self.not_in_use_color)
