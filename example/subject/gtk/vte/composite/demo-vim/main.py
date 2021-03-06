#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

gi.require_version('Vte', '2.91')
from gi.repository import Vte

import signal
import os

class Term:
	app = None
	view = None
	term = None

	cmd = '/usr/bin/vim'

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_term()
		self.view = self.term

	def init_term (self):
		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.new
		self.term = term = Vte.Terminal()

		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.spawn_sync
		ok, pid = term.spawn_sync(
			Vte.PtyFlags.DEFAULT,
			os.environ['HOME'],
			[self.cmd],
			[],
			GLib.SpawnFlags.DO_NOT_REAP_CHILD,
			None,
			None,
		)

		print('ok:', ok)
		print('pid:', pid)

		if (not ok):
			return False

		term.watch_child(pid)

		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.signals.child_exited
		term.connect('child-exited', self.on_child_exited);

		term.show_all()

	def on_child_exited(self, term, status):
		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.signals.child_exited
		print('')
		print('on_child_exited:')
		print('	term:', term)
		print('	status:', status)

		Gtk.main_quit()


class Win:
	app = None
	win = None
	term = None

	title = 'Demo Vte.Terminal Vim'

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_win()

	def init_term (self):
		self.term = term = Term()
		term.app = self.app
		term.init()

	def init_win (self):
		self.win = win = Gtk.Window()

		win.set_title(self.title)

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event
		#win.connect('delete-event', Gtk.main_quit)
		win.connect('delete-event', self.on_close_win)

		self.init_term()
		win.add(self.term.view)

		win.show_all()

	def on_close_win (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.main_quit
		Gtk.main_quit()

		return True

class Signal:
	app = None

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_signal()

	def init_signal (self):
		## https://docs.python.org/3/library/signal.html
		## https://docs.python.org/2/library/signal.html
		signal.signal(signal.SIGINT, signal.SIG_DFL)

class App:
	def init (self):
		self.signal = signal = Signal()
		signal.app = self
		signal.init()

		self.win = win = Win()
		win.app = self
		win.init()

	def run (self):
		Gtk.main()

def main ():
	app = App()
	app.init()
	app.run()

if __name__ == '__main__':
	main()

## Tutorial
## http://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html
## http://python-gtk-3-tutorial.readthedocs.io/en/latest/dialogs.html

## Gtk
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.resize
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.resize_to_geometry

## Vte
## https://lazka.github.io/pgi-docs/index.html#Vte-2.91
## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes.html

## Vte.Terminal
## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html
