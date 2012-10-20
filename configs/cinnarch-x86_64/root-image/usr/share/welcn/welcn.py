#!/usr/bin/python
# -*- coding: UTF-8 -*-

import gi
from gi.repository import Gtk
import subprocess, sys
import threading

import gettext

# Algunas cosas para gettext (para las traducciones)
APP="welcn"
DIR="po"

# Esto permite traducir los textos escritos en el .py (no en glade)
gettext.textdomain(APP)
gettext.bindtextdomain(APP, DIR)


# Y con esto podemos marcar las cadenas a traducir de la forma _("cadena")
_ = gettext.gettext



WELCN_DIR = '/usr/share/welcn/'


class main():


	def __init__(self):

		builder = Gtk.Builder()
		builder.add_from_file(WELCN_DIR + "welcn.ui")
		
		
		#### Language and Keymap window
		self.window = builder.get_object("window1")
		self.button_try = builder.get_object("button1")
		self.button_cli_installer = builder.get_object("button2")



		self.window.connect("delete-event", Gtk.main_quit)
		builder.connect_signals(self)
		self.window.set_title(_('Welcome!'))
		self.window.set_position(Gtk.WindowPosition.CENTER)


		self.window.show_all()

	def on_button1_clicked(self, widget, data=None):
		Gtk.main_quit()

	def on_button2_clicked(self, widget, data=None):
		subprocess.Popen(["cinnarch-setup"])
		sys.exit(0)





if __name__ == '__main__':
	main()
	Gtk.main()