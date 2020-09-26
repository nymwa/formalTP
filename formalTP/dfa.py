import sys
import yaml

terminals = {}
variables = {}

def empty(sent):
	return len(sent) == 0


class Variable(dict):
	def __init__(self, rules):
		for key, value in rules.items():
			self[key] = value

	def check(self, sent, key):
		if key.startswith('_'):
			if sent[0] in terminals[key]:
				return True
		if sent[0] == key:
			return True
		return False

	def __call__(self, sent):
		if len(sent) == 0:
			return False
		for key, value in self.items():
			if self.check(sent, key):
				for var in value:
					if var is None:
						if len(sent[1:]) == 0:
							return True
					else:
						if variables[var](sent[1:]):
							return True
		return False


def main():
	with open('rule.yaml') as f:
		dct = yaml.safe_load(f)
	for key, value in dct.items():
		if key.startswith('_'):
			terminals[key] = set(value)
		else:
			variables[key] = Variable(value)
	

	for x in sys.stdin:
		x = x.strip().split()
		x = [w for w in x if w not in {',', '.'}]
		if variables['S'](x):
			p = 'o'
		else:
			p = 'x'
		print(p, ':', ' '.join(x))
