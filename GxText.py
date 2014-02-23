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

window = self.CreateWindow(48, 0, 400, 600, 'GxText')
window.SetIcon("apps/default/GxText/")

vbox1 = VBox(window.top_level_container, window, [])
window.AddWidget(vbox1)

hbox_top_buttons = HBox(vbox1, window, [])
hbox_top_buttons.RequestHeight(32)
window.AddWidget(hbox_top_buttons, vbox1)

button_save = Button(hbox_top_buttons, window, "Save", "print 'GxText: Save button clicked.'")
button_save.RequestWidth(64)
button_load = Button(hbox_top_buttons, window, "Load", "print 'GxText: Load button clicked.'")
button_load.RequestWidth(64)
emptyspace = EmptyWidget(hbox_top_buttons, window)
button_run = Button(hbox_top_buttons, window, "Run", "print 'GxText: Run button clicked.'")
button_run.RequestWidth(64)
window.AddWidget(button_save, hbox_top_buttons)
window.AddWidget(button_load, hbox_top_buttons)
window.AddWidget(emptyspace, hbox_top_buttons)
window.AddWidget(button_run, hbox_top_buttons)

text_area = TextEntryMonoBox(vbox1, window, "Left-click this area to focus the text box and begin typing.")
window.AddWidget(text_area, vbox1)
