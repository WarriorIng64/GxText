# This file is part of GxText.
# Copyright (C) 2014 Christopher Kyle Horton <christhehorton@gmail.com>

# GxText is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GxText is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GxText. If not, see <http://www.gnu.org/licenses/>.


# Code for Buttons--------------------------------------------------------------

# TODO: Make the Save and Load buttons actually do what they're supposed to.
save_code = """
print '***GxText: Save button clicked.'
self.parent_window.wm.ShowPopupMessage('GxText', 'You clicked the Save button.')
self.parent_window.code_entry.SetAsFocusedWidget(self.parent_window.code_entry)
"""

load_code = """
print '***GxText: Load button clicked.'
self.parent_window.wm.ShowPopupMessage('GxText', 'You clicked the Load button.')
with open('apps/default/GxText/GxText.py', 'r') as load_file:
  loaded_code_string = load_file.read()
  self.parent_window.code_entry.SetText(loaded_code_string)
self.parent_window.code_entry.multiline.SetCursorAtBeginning()
self.parent_window.code_entry.SetAsFocusedWidget(self.parent_window.code_entry)
"""

run_code = """
try:
  self.parent_window.wm.RunString(self.parent_window.code_entry.GetText())
except SyntaxError as e:
  print "***GxText: SyntaxError in entered app code: ", e
  self.parent_window.wm.ShowPopupMessage('GxText: SyntaxError', str(e))
except Exception as e:
  print "***GxText: Unhandled app code execution error: ", e
  self.parent_window.wm.ShowPopupMessage('GxText: Exception', str(e))
self.parent_window.code_entry.SetAsFocusedWidget(self.parent_window.code_entry)
"""

# Window and UI code------------------------------------------------------------

window = self.CreateWindow(48, 0, 400, 600, 'GxText')
window.SetIcon("apps/default/GxText/")

vbox1 = VBox(window.top_level_container, window, [])
window.AddWidget(vbox1)

hbox_top_buttons = HBox(vbox1, window, [])
hbox_top_buttons.RequestHeight(32)
window.AddWidget(hbox_top_buttons, vbox1)

button_save = Button(hbox_top_buttons, window, "Save", save_code)
button_save.RequestWidth(64)
button_load = Button(hbox_top_buttons, window, "Load", load_code)
button_load.RequestWidth(64)
emptyspace = EmptyWidget(hbox_top_buttons, window)
window.button_run = Button(hbox_top_buttons, window, "Run", run_code)
window.button_run.RequestWidth(64)
window.AddWidget(button_save, hbox_top_buttons)
window.AddWidget(button_load, hbox_top_buttons)
window.AddWidget(emptyspace, hbox_top_buttons)
window.AddWidget(window.button_run, hbox_top_buttons)

window.code_entry = TextEntryCodeBox(vbox1, window, "")
window.AddWidget(window.code_entry, vbox1)
window.code_entry.SetAsFocusedWidget(window.code_entry)
