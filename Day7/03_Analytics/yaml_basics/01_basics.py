'''
what is yaml?

'''

import yaml

with open("first_config.yaml","r") as file:

    config = yaml.safe_load(file)

print("="*100)

