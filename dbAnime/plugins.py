#plugins.py
import os
from importlib import import_module

class PluginLoader:
	def __init__(self,path):
		self.path = path
		self.contents = os.listdir(self.path)
		self.load_plugins()

	def load_plugins(self):
		to_import = [plugin[:-3] for plugin in self.contents if plugin.endswith('.py')]
		try:
			self.imported_plugins = [import_module(f'{self.path}.{plugin}') for plugin in to_import]
		except ImportError:
			print(ImportError)
			exit()