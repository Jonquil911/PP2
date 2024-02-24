import json
with open('sample-data.json') as file:
    data = json.load(file)

template = """
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------   ------ ------
{}
"""

interfaces = []
for item in data['imdata']:
    if 'l1PhysIf' in item:
        attributes = item['l1PhysIf']['attributes']
        dn = attributes['dn']
        description = attributes['descr']
        speed = attributes['speed']
        mtu = attributes['mtu']
        interfaces.append((dn, description, speed, mtu))

formatted_interfaces = "\n".join(f"{dn:<55} {description:<16} {speed:<8} {mtu:<7}" for dn, description, speed, mtu in interfaces)

print(template.format(formatted_interfaces))
