# main.py
import plugins

def main():
	# Load Plugins
	plugin_ld = plugins.PluginLoader('plugins_fd')
	a = plugin_ld.imported_plugins[0].TestA()
	print(a.Test)

	# Search and load info

	# Write info to csv file

	# Analize it


if __name__ == "__main__":
	main()