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

def merger(default, outsider):
	container={}
	for default_key, default_value in default.items():
		flag = False
		for outsider_key, outsider_value in outsider.items():
			if(default_key == outsider_key):
				container[default_key] = outsider_value
				flag = True
		
		if(flag == False):
			container[default_key] = default_value
	
	return container
		


