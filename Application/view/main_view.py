import tkinter as tk
from tkinter import ttk, messagebox
from controller.controller import Controller
from tkinter import font as tkfont

class MainView(tk.Tk):
    """
    The main view for the application.
    """
    def __init__(self, controller: Controller):
        super().__init__()
        # enlarge default fonts
        for fname in self.tk.call('font','names'):
            f=tkfont.nametofont(fname)
            try:
                f.configure(size=f.cget('size')+2)
            except Exception:
                pass

        self.controller = controller
        self.title("Screen Locator")
        self.state("zoomed")
        # scale window to 85% of current monitor and expose a scale factor for child widgets
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        w, h = int(sw*0.85), int(sh*0.85)
        x, y = (sw-w)//2, (sh-h)//2

        # menubar with settings
        menubar = tk.Menu(self)
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Change Database Path", command=self._change_db_path)
        menubar.add_cascade(label="Settings", menu=settings_menu)
        self.config(menu=menubar)

        # layout
        root = ttk.Frame(self); root.pack(fill='both', expand=True)
        root.columnconfigure(1, weight=1)   # right pane expands
        root.rowconfigure(0, weight=1)

        sidebar = ttk.Frame(root, width=250, padding=8)
        sidebar.grid(row=0, column=0, sticky='ns')
        sidebar.columnconfigure(0, weight=1)

        self._build_sidebar(sidebar)

        display_container = ttk.Frame(root)
        display_container.grid(row=0, column=1, sticky='nsew')
        self._build_display_area(display_container)

        # register as observer so we refresh when data changes
        if hasattr(self.controller, 'observers'):
            self.controller.observers.append(self)

        # first paint
        self.refresh_display()

    # settings
    def _change_db_path(self):
        from tkinter import filedialog, messagebox
        new_path = filedialog.askopenfilename(title="Select SQLite DB", filetypes=[("SQLite DB","*.db"), ("All","*.*")])
        if new_path:
            try:
                self.controller.update_db_path(new_path)
                messagebox.showinfo("Database Updated", f"Database path updated to:\n{new_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to switch database:\n{e}")

    # sidebar widgets
    def _build_sidebar(self, parent):
        ttk.Label(parent, text="Screen Locator",
                  font=('Segoe UI', 14, 'bold')).pack(anchor='w', pady=(0,10))

        # search widgets
        search_row = ttk.Frame(parent); search_row.pack(fill='x', pady=(0,6))
        ttk.Label(search_row, text="Search").pack(side='left')
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_row, textvariable=self.search_var)
        search_entry.pack(side='left', fill='x', expand=True)
        search_entry.bind('<Return>', lambda e: self.refresh_display())
        ttk.Button(search_row, text="Search", command=self.refresh_display).pack(side='left', padx=4)

        # search parameters
        params = ttk.LabelFrame(parent, text="Search Parameters")
        params.pack(fill='x', pady=4)
        self.param_vars = {
            'design': tk.BooleanVar(value=True),
            'customer': tk.BooleanVar(value=True),
            'description': tk.BooleanVar(value=True),
        }
        for name, var in self.param_vars.items():
            ttk.Checkbutton(params, text=name.title(), variable=var,
                            command=self.refresh_display).pack(anchor='w')

        # usage filters
        usage = ttk.LabelFrame(parent, text="Usage")
        usage.pack(fill='x', pady=4)
        self.show_in_use = tk.BooleanVar(value=False)
        self.show_not_in_use = tk.BooleanVar(value=False)
        ttk.Checkbutton(usage, text="In-Use Only",
                        variable=self.show_in_use,
                        command=self.refresh_display).pack(anchor='w')
        ttk.Checkbutton(usage, text="Not In-Use Only",
                        variable=self.show_not_in_use,
                        command=self.refresh_display).pack(anchor='w')

        # location filter (store frame and vars for later refresh)
        self.loc_vars = {}
        # Location filter: scrollable canvas inside label frame
        self.loc_frame = ttk.LabelFrame(parent, text="Locations")
        self.loc_frame.pack(fill='both', expand=True, pady=4)
        self.loc_frame.rowconfigure(0, weight=1)
        self.loc_frame.columnconfigure(0, weight=1)

        # create canvas and scrollbar
        self.loc_canvas = tk.Canvas(self.loc_frame, borderwidth=0, highlightthickness=0)
        self.loc_scroll = ttk.Scrollbar(self.loc_frame, orient="vertical", command=self.loc_canvas.yview)
        self.loc_canvas.configure(yscrollcommand=self.loc_scroll.set)
        self.loc_canvas.grid(row=0, column=0, sticky='nsew')
        self.loc_scroll.grid(row=0, column=1, sticky='ns')

        # checkbuttons
        self.loc_inner = ttk.Frame(self.loc_canvas)
        self.loc_canvas.create_window((0,0), window=self.loc_inner, anchor='nw')
        # update scroll region
        self.loc_inner.bind("<Configure>", lambda e: self.loc_canvas.configure(scrollregion=self.loc_canvas.bbox("all")))

        # enable mouse wheel scrolling for location list
        self._bind_mousewheel(self.loc_canvas)

        ttk.Checkbutton(self.loc_inner, text="All", command=self._toggle_all_locations).pack(anchor='w')

        self.loc_rows={}  # mapping loc_id -> row frame
        self._update_location_filter_widgets()



    # scrollable right sie
    def _build_display_area(self, parent):
        # row 0loc_create, row1 screen_create, row2 bulk actions, row3 canvas
        parent.rowconfigure(3, weight=1)
        parent.columnconfigure(0, weight=1)

        # location create bar (row 0)
        self.loc_create_bar = ttk.Frame(parent, padding=4)
        self.loc_create_bar.grid(row=0, column=0, columnspan=2, sticky='ew')
        self._build_location_create_bar()

        # screen create bar (row 1)
        self.screen_create_bar = ttk.Frame(parent, padding=4)
        self.screen_create_bar.grid(row=1, column=0, columnspan=2, sticky='ew')
        self._build_screen_create_bar()

        # bulk action bar (row 2)
        self.action_bar = ttk.Frame(parent)
        self.action_bar.grid(row=2, column=0, columnspan=2, sticky='ew')
        self._build_action_bar()

        # scrollable canvas (row 3)
        self.display_canvas = tk.Canvas(parent, borderwidth=0)
        vsb = ttk.Scrollbar(parent, orient="vertical", command=self.display_canvas.yview)
        self.display_canvas.configure(yscrollcommand=vsb.set)

        self.display_canvas.grid(row=3, column=0, sticky='nsew')
        vsb.grid(row=3, column=1, sticky='ns')

        self.scroll_frame = ttk.Frame(self.display_canvas)
        self.display_canvas.create_window((0,0), window=self.scroll_frame, anchor='nw')

        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.display_canvas.configure(scrollregion=self.display_canvas.bbox("all"))
        )
        # mouse wheel binding (reuse code you already added)
        self._bind_mousewheel(self.display_canvas)

    def _bind_mousewheel(self, canvas):
        from tkinter import ttk
        def _on(event, target_canvas=canvas, root_widget=canvas):
            # allow widgets to handle their own scrolling
            widget = event.widget
            # Ignore non-tk widgets
            if not hasattr(widget, "winfo_class"):
                return
            if isinstance(widget, ttk.Combobox) or widget.winfo_class() in ("Listbox",):
                return
            # ensure event occurred within the target widget subtree
            w = widget
            inside = False
            while w is not None:
                if w == root_widget:
                    inside = True
                    break
                w = w.master
            if not inside:
                return
            delta = -1*(event.delta//120) if event.delta else (1 if event.num==5 else -1)
            target_canvas.yview_scroll(delta, "units")
        # global binding, but handler checks subtree to decide action
        canvas.bind_all("<MouseWheel>", _on, add="+")
        canvas.bind_all("<Button-4>", _on, add="+")
        canvas.bind_all("<Button-5>", _on, add="+")

    # filter helpers
    def _delete_location(self, loc):
        # prevent deletion if any screens still reference this location
        if any(s.location_id == loc.location_id for s in self.controller.screens):
            messagebox.showerror('Cannot Delete', 'There are screens assigned to this location. Move or delete them first.')
            return
        if messagebox.askyesno('Delete Location', f'Delete location "{loc.description}"?'):
            self.controller.delete_location(loc)

    def _update_location_filter_widgets(self):
        """
        Ensure the location filter checklist includes all current locations.
        """
        # add new locations
        for loc in self.controller.locations.values():
            if loc.location_id not in self.loc_vars:
                var = tk.BooleanVar(value=True)
                self.loc_vars[loc.location_id] = var
                row = ttk.Frame(self.loc_inner)
                row.pack(fill='x', anchor='w')
                ttk.Checkbutton(row, text=loc.description, variable=var,
                                command=self.refresh_display).pack(side='left', anchor='w')
                ttk.Button(row, text='✖', width=2, command=lambda l=loc: self._delete_location(l)).pack(side='right')
                self.loc_rows[loc.location_id]=row
        # remove deleted locations
        removed=[lid for lid in self.loc_vars.keys() if lid not in self.controller.locations]
        for lid in removed:
            self.loc_vars.pop(lid)
            row=self.loc_rows.pop(lid, None)
            if row is not None:
                row.destroy()

    def _toggle_all_locations(self):
        val = all(var.get() for var in self.loc_vars.values())
        for var in self.loc_vars.values():
            var.set(not val)
        self.refresh_display()

    # filtering and drawing-
    # Observer callback from Controller
    def data_updated(self):
        """
        Callback triggered by Controller when underlying data changes.
        """
        self.refresh_display()

    def _build_location_create_bar(self):
        ttk.Label(self.loc_create_bar, text='New Location:').pack(side='left')
        self.new_loc_var = tk.StringVar()
        ttk.Entry(self.loc_create_bar, textvariable=self.new_loc_var, width=30).pack(side='left', padx=2)
        ttk.Button(self.loc_create_bar, text='Add', command=self._create_location).pack(side='left')

    def _build_screen_create_bar(self):
        pad=2
        ttk.Label(self.screen_create_bar, text='New Screen | Design:').pack(side='left', padx=pad)
        self.new_design_var=tk.StringVar(); ttk.Entry(self.screen_create_bar, textvariable=self.new_design_var, width=15).pack(side='left', padx=pad)
        ttk.Label(self.screen_create_bar, text='Customer:').pack(side='left', padx=pad)
        self.new_customer_var=tk.StringVar(); ttk.Entry(self.screen_create_bar, textvariable=self.new_customer_var, width=15).pack(side='left', padx=pad)
        ttk.Label(self.screen_create_bar, text='Qty:').pack(side='left', padx=pad)
        self.new_qty_var=tk.StringVar(); ttk.Entry(self.screen_create_bar, textvariable=self.new_qty_var, width=5).pack(side='left', padx=pad)
        ttk.Label(self.screen_create_bar, text='Description:').pack(side='left', padx=pad)
        self.new_desc_var=tk.StringVar(); ttk.Entry(self.screen_create_bar, textvariable=self.new_desc_var, width=20).pack(side='left', padx=pad)
        ttk.Label(self.screen_create_bar, text='Location:').pack(side='left', padx=pad)
        self.new_loc_choice=tk.StringVar()
        self.new_loc_combo=ttk.Combobox(self.screen_create_bar, textvariable=self.new_loc_choice, state='readonly', width=20)
        self.new_loc_combo.pack(side='left', padx=pad)
        self.new_inuse_var=tk.BooleanVar(value=False)
        ttk.Checkbutton(self.screen_create_bar, text='In Use', variable=self.new_inuse_var).pack(side='left', padx=pad)
        ttk.Button(self.screen_create_bar, text='Add Screen', command=self._create_screen).pack(side='left', padx=pad)

    def _build_action_bar(self):
        self.selected_screens: set = set()
        self.action_bar_buttons = {}
        for txt, cmd in (
            ("Mark In-Use", lambda: self._bulk_update_usage(True)),
            ("Mark Not In-Use", lambda: self._bulk_update_usage(False)),
            ("Delete", self._bulk_delete),
        ):
            btn_obj = ttk.Button(self.action_bar, text=txt, command=cmd, state='disabled')
            btn_obj.pack(side='left', padx=2, pady=2)
            self.action_bar_buttons[txt] = btn_obj
        # Move to location dropdown
        ttk.Label(self.action_bar, text='Move to:').pack(side='left', padx=(20,2))
        self.move_loc_var = tk.StringVar()
        loc_names=[loc.description for loc in self.controller.locations.values()]
        self.move_combo=ttk.Combobox(self.action_bar, values=loc_names, state='readonly', width=25, textvariable=self.move_loc_var)
        self.move_combo.pack(side='left')
        move_btn = ttk.Button(self.action_bar, text='Move', command=self._bulk_move, state='disabled')
        move_btn.pack(side='left', padx=2)
        self.action_bar_buttons['Move']=move_btn

    def _refresh_create_dropdowns(self):
        loc_names=[loc.description for loc in self.controller.locations.values()]
        self.new_loc_combo['values']=loc_names
        self.move_combo['values']=loc_names

    def _create_location(self):
        desc=self.new_loc_var.get().strip()
        if not desc:
            messagebox.showerror('Error','Description cannot be empty')
            return
        if desc.lower() in [l.description.lower() for l in self.controller.locations.values()]:
            messagebox.showerror('Error','Location description must be unique')
            return
        from model.location import Location
        self.controller.add_location(Location(desc))
        self.new_loc_var.set('')

    def _create_screen(self):
        design=self.new_design_var.get().strip()
        customer=self.new_customer_var.get().strip()
        qty=self.new_qty_var.get().strip()
        desc=self.new_desc_var.get().strip()
        loc_name=self.new_loc_choice.get().strip()
        # validations similar to ScreenFrame.validate_entries
        if not design:
            messagebox.showerror('Validation Error','Design cannot be empty.'); return
        if not customer:
            messagebox.showerror('Validation Error','Customer cannot be empty.'); return
        if not desc:
            messagebox.showerror('Validation Error','Description cannot be empty.'); return
        if not qty:
            messagebox.showerror('Validation Error','Quantity cannot be empty.'); return
        if not qty.isdigit():
            messagebox.showerror('Validation Error','Quantity must be an integer.'); return
        if not loc_name:
            messagebox.showerror('Validation Error','Location must be selected.'); return
        from model.screen import Screen
        location_id=[l.location_id for l in self.controller.locations.values() if l.description==loc_name][0]
        screen=Screen(location_id,int(qty),design,customer,desc,self.new_inuse_var.get())
        self.controller.add_screen(screen)
        #clear
        self.new_design_var.set(''); self.new_customer_var.set(''); self.new_qty_var.set(''); self.new_desc_var.set(''); self.new_inuse_var.set(False)

    def _update_action_bar_state(self):
        state='normal' if self.selected_screens else 'disabled'
        for btn in self.action_bar_buttons.values():
            btn.configure(state=state)

    def _select_callback(self, screen, selected):
        if selected:
            self.selected_screens.add(screen)
        else:
            self.selected_screens.discard(screen)
        self._update_action_bar_state()

    def _bulk_update_usage(self, in_use: bool):
        for s in list(self.selected_screens):
            s.in_use = in_use
            s.add_to_db(self.controller.connection)
        self.controller.update_screen_list()

    def _bulk_delete(self):
        if not self.selected_screens:
            return
        if not messagebox.askyesno('Confirm Delete',
                                   f'Delete {len(self.selected_screens)} selected screens? This cannot be undone.'):
            return
        for s in list(self.selected_screens):
            s.delete_from_db(self.controller.connection)
        self.selected_screens.clear()
        self.controller.update_screen_list()

    def _bulk_move(self):
        dest_name=self.move_loc_var.get()
        if not dest_name or dest_name not in [l.description for l in self.controller.locations.values()]:
            return
        dest_loc=[l for l in self.controller.locations.values() if l.description==dest_name][0]
        for s in list(self.selected_screens):
            s.location_id=dest_loc.location_id
            s.add_to_db(self.controller.connection)
        self.controller.update_screens_and_locations()

    def refresh_display(self):
        # clear previous selection set and disable buttons
        self.selected_screens.clear()
        self._update_action_bar_state()

        # sync filters and dropdowns
        self._update_location_filter_widgets()
        self._refresh_create_dropdowns()
        for child in self.scroll_frame.winfo_children():
            child.destroy()
        # reset scroll to top
        if hasattr(self, 'display_canvas'):
            self.display_canvas.yview_moveto(0)

        # build filter predicates
        search = self.search_var.get().lower()
        active_params = [k for k,v in self.param_vars.items() if v.get()]
        loc_ids = [lid for lid,var in self.loc_vars.items() if var.get()]
        in_use_filter = None
        if self.show_in_use.get() and not self.show_not_in_use.get():
            in_use_filter = True
        elif self.show_not_in_use.get() and not self.show_in_use.get():
            in_use_filter = False

        # apply filters
        filtered = []
        for s in self.controller.screens:
            if loc_ids and s.location_id not in loc_ids:
                continue
            if in_use_filter is not None and s.in_use!=in_use_filter:
                continue
            if search:
                match = False
                if 'design' in active_params and search in s.design.lower():
                    match=True
                if 'customer' in active_params and search in s.customer.lower():
                    match=True
                if 'description' in active_params and search in s.description.lower():
                    match=True
                if not match:
                    continue
            filtered.append(s)

        # group by location
        grouped={}
        for sc in filtered:
            grouped.setdefault(sc.location_id,[]).append(sc)

        from view.location_frame import LocationFrame
        for loc_id in sorted(grouped, key=lambda lid: self.controller.locations[lid].description.lower()):
            lf = LocationFrame(self.scroll_frame, self.controller,
                               self.controller.locations[loc_id], grouped[loc_id], select_callback=self._select_callback)
            lf.pack(fill='x', pady=2, padx=4, anchor='n')