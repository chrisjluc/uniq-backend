import json

id='id'
name = 'name'
u_pop = 'undergradPopulation'
g_pop = 'gradPopulation'
images = 'images'
location = 'location'

class ProgramConverter(object):

	def to_explore_json(self, program):
		data = json.loads(program.to_json())
		ret = {}

		ret[id] = str(program.id)

		if program.name:
			ret[name] = program.name
		else:
			ret[name] = None

		if data[images]:
			ret[images] = data[images]
		else:
			ret[images] = None


		if program.undergradPopulation:
			ret[u_pop] = program.undergradPopulation
		else:
			ret[u_pop] = None

		if program.gradPopulation:
			ret[g_pop] = program.gradPopulation
		else:
			ret[g_pop] = None

		if data[location]:
			ret[location] = data[location]
		else:
			ret[location] = None

		return ret