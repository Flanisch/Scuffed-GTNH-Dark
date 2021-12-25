from configparser import ConfigParser
import json
import os.path

class GregTechRenamer:
	searchStrings = []
	filename = ''

	def run(self):
		if(os.path.exists('config.ini')):
			config = ConfigParser()
			config.read('config.ini', encoding = 'utf8')

			if config.has_section('SEARCH') and config.has_option('SETTINGS', 'toReplace') and config.has_option('SETTINGS', 'replacement'):
					stringsToReplace = json.loads(config.get('SEARCH','keywords'))
					filename  = config['SETTINGS']['filename']
					stringToReplace  = config['SETTINGS']['toReplace'].strip("'")
					replacementString = config['SETTINGS']['replacement'].strip("'")
					print(replacementString)
			else:
				print("Not all variables were set")
				return

		fileContent = []
		with open(filename, 'rt', encoding = 'utf8') as readFile:
			fileContent = readFile.readlines()

		with open(filename, "wt",encoding="utf8") as writeFile:
			for line in fileContent:
				for string in stringsToReplace:
					if string in line and not replacementString in line:
						line = line.replace(stringToReplace, replacementString)
					
				writeFile.writelines(line)

if __name__ == '__main__':
	GregTechRenamer().run()