network_settings = {
    1: {'name': 'Network_1', 'ip_range': '192.168.1.0/24', 'status': 'active'},
    2: {'name': 'Network_2', 'ip_range': '192.168.2.0/24', 'status': 'inactive'}
}
#print(network_settings)

def create_network(network_id, name, ip_range, status):
    if network_id in network_settings:
        print(f"Network with ID {network_id} already exists.")
    else:
        network_settings[network_id] = {'name': name, 'ip_range': ip_range, 'status': status}
        print(f"Network '{name}' created with ID {network_id}.")
print(create_network)


def read_network(network_id):
    network = network_settings.get(network_id)
    if network:
        print(f"Network {network_id}: {network}")
    else:
        print(f"Network with ID {network_id} does not exist.")


def update_network(network_id, name=None, ip_range=None, status=None):
    if network_id in network_settings:
        if name:
            network_settings[network_id]['name'] = name
        if ip_range:
            network_settings[network_id]['ip_range'] = ip_range
        if status:
            network_settings[network_id]['status'] = status
        print(f"Network {network_id} updated.")
    else:
        print(f"Network with ID {network_id} does not exist.")


def delete_network(network_id):
    if network_id in network_settings:
        del network_settings[network_id]
        print(f"Network {network_id} deleted.")
    else:
        print(f" Network with ID {network_id} does not exist.")



def setup_virtual_network(network_id, name, ip_range, status):
    if network_id not in network_settings:
        create_network(network_id, name, ip_range, status)
        print(f"Virtual network '{name}' is set up with IP range {ip_range} and status {status}.")
    else:
        print(f"Network with ID {network_id} already exists, consider updating it.")

def update_network_settings(settings_id, new_config):
    if settings_id in network_settings:
        network_settings[settings_id].update(new_config)
        print(f"Network {settings_id} updated with new configuration: {new_config}")
    else:
        print(f"Network with ID {settings_id} does not exist.")


create_network(1, 'Network_1', '192.168.1.0/24', 'active')
read_network(1)
update_network(1, name='New_Network_1', status='inactive')
delete_network(1)
setup_virtual_network(3, 'Network_3', '192.168.3.0/24', 'active')
new_settings = {'ip_range': '192.168.1.0/25', 'status': 'inactive'}
update_network_settings(1, new_settings)
