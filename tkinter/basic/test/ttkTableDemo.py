#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.6

try:
    import Tkinter
    import tkFont
except ImportError:
    import tkinter as Tkinter
    import tkinter.font as tkFont

import ttk

tree_columns = ("country", "capital", "currency")
tree_data = [
    ("Argentina",      "Buenos Aires",     "ARS"),
    ("Australia",      "Canberra",         "AUD"),
    ("Brazil",         "Brazilia",         "BRL"),
    ("Canada",         "Ottawa",           "CAD"),
    ("China",          "Beijing",          "CNY"),
    ("France",         "Paris",            "EUR"),
    ("Germany",        "Berlin",           "EUR"),
    ("India",          "New Delhi",        "INR"),
    ("Italy",          "Rome",             "EUR"),
    ("Japan",          "Tokyo",            "JPY"),
    ("Mexico",         "Mexico City",      "MXN"),
    ("Russia",         "Moscow",           "RUB"),
    ("South Africa",   "Pretoria",         "ZAR"),
    ("United Kingdom", "London",           "GBP"),
    ("United States",  "Washington, D.C.", "USD")
    ]

def sortby(tree, col, descending):
    """Sort tree contents when a column is clicked on."""
    # grab values to sort
    data = [(tree.set(child, col), child) for child in tree.get_children('')]

    # reorder data
    data.sort(reverse=descending)
    for indx, item in enumerate(data):
        tree.move(item[1], '', indx)

    # switch the heading so that it will sort in the opposite direction
    tree.heading(col,
        command=lambda col=col: sortby(tree, col, int(not descending)))

class App(object):
    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        container = ttk.Frame()
        container.pack(fill='both', expand=True)

        self.tree = ttk.Treeview(columns=tree_columns, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in tree_columns:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            self.tree.column(col, width=tkFont.Font().measure(col.title()))

        for item in tree_data:
            self.tree.insert('', 'end', values=item)

            # adjust columns lenghts if necessary
            for indx, val in enumerate(item):
                ilen = tkFont.Font().measure(val)
                if self.tree.column(tree_columns[indx], width=None) < ilen:
                    self.tree.column(tree_columns[indx], width=ilen)

def main():
    root = Tkinter.Tk()
    root.wm_title("Multi-Column List")
    root.wm_iconname("mclist")
    app = App()
    root.mainloop()

if __name__ == "__main__":
    main()