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

save_code = """
import os
dir = os.path.dirname(self.parent_window.file_entry.GetText())
if not os.path.exists(dir):
  os.makedirs(dir)
try:
  with open(self.parent_window.file_entry.GetText(), 'w+') as save_file:
    self.parent_window.file_name = save_file.name
    save_file.write(self.parent_window.code_entry.GetText())
    self.parent_window.SetTitlebarText('GxText: ' + save_file.name)
    self.parent_window.wm.ShowPopupMessage('GxText', 'File saved to ' + self.parent_window.file_entry.GetText() + '.')
except IOError as e:
  self.parent_window.wm.ShowPopupMessage('Error', self.parent_window.file_entry.GetText() + ' could not be saved.')
self.parent_window.code_entry.SetAsFocusedWidget(self.parent_window.code_entry)
"""

load_code = """
backup = self.parent_window.code_entry.GetText()
try:
  with open(self.parent_window.file_entry.GetText(), 'r') as load_file:
    loaded_code_string = load_file.read()
    self.parent_window.code_entry.SetText(loaded_code_string)
    self.parent_window.file_name = load_file.name
    self.parent_window.SetTitlebarText('GxText: ' + load_file.name + '*')
    self.parent_window.wm.ShowPopupMessage('GxText', 'File loaded from ' + self.parent_window.file_entry.GetText() + '.')
except IOError as e:
  self.parent_window.wm.ShowPopupMessage('Error', self.parent_window.file_entry.GetText() + ' does not exist.')
  self.parent_window.code_entry.SetText(backup)
self.parent_window.code_entry.multiline.SetCursorAtBeginning()
self.parent_window.code_entry.SetAsFocusedWidget(self.parent_window.code_entry)
"""

run_code = """
try:
  self.parent_window.wm.RunString(self.parent_window.code_entry.GetText())
except SyntaxError as e:
  import traceback
  for frame in traceback.extract_tb(sys.exc_info()[2]):
    line_number = frame[1]
  line_number_text = "(Line " + str(line_number) + ")"
  print "***GxText: SyntaxError in entered app code: ", e, line_number_text
  self.parent_window.wm.ShowPopupMessage('GxText: SyntaxError', str(e) + " " + line_number_text)
  self.parent_window.code_entry.multiline.SetCursorAtLineStart(line_number - 1)
except Exception as e:
  import traceback
  for frame in traceback.extract_tb(sys.exc_info()[2]):
    line_number = frame[1]
  line_number_text = "(Line " + str(line_number) + ")"
  print "***GxText: SyntaxError in entered app code: ", e, line_number_text
  self.parent_window.wm.ShowPopupMessage('GxText: Exception', str(e) + " " + line_number_text)
  self.parent_window.code_entry.multiline.SetCursorAtLineStart(line_number - 1)
self.parent_window.code_entry.SetAsFocusedWidget(self.parent_window.code_entry)
"""

gxtext_frame_code = """
cursor_pos = self.code_entry.multiline.GetCursorPosition()
cursor_pos_string = "Line " + str(cursor_pos[0] + 1) + ", Column " + str(cursor_pos[1])
self.SetStatusbarText(cursor_pos_string)
"""

# Window and UI code------------------------------------------------------------

window = self.CreateWindow(48, 0, 400, 600, 'GxText: <New file>')
window.SetIcon("apps/default/GxText/")

vbox1 = VBox(window.top_level_container, window, [])
window.AddWidget(vbox1)

hbox_top_buttons = HBox(vbox1, window, [])
hbox_top_buttons.RequestHeight(32)
window.AddWidget(hbox_top_buttons, vbox1)

window.file_entry = TextEntrySinglelineBox(vbox1, window, "apps/default/GxText/GxText.py")
window.AddWidget(window.file_entry, vbox1)

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

window.file_name = "<New file>"

window.SetFrameCode(gxtext_frame_code)
