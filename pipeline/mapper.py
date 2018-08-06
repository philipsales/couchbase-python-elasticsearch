import json

def mapper(obj):
	container = {}
	for key, value in obj.items():
		if(type(value).__name__ == "dict"):
			temp = mapper(value)
			container.update(temp)
			continue

		container[key] = value
	
	return container