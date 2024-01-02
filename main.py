import requests
import time
import json


def get_public_ip():
    return requests.get('https://api64.ipify.org?format=json').json()['ip']

def read_config():
    with open('config.json') as json_file:
        data = json.load(json_file)
        return data


def update_cf(config):
    headers = {
        'Authorization': "Bearer "+config['api_token'],
        'Content-Type': 'application/json',
    }

    while True:
        public_ip = get_public_ip()
        for domain in config['dns']:

            data = {
                "type":  domain["type"],
                "name": domain["name"],
                "content": public_ip
            }
            data = json.dumps(data)
            response = requests.put('https://api.cloudflare.com/client/v4/zones/'+config['zone_id']+'/dns_records/'+domain['record_id'], headers=headers, data=data)

            print(f"Update record {domain['name']} " if response.status_code == 200 else "Error updating record")
        time.sleep(config['time']*60)

if __name__ == "__main__":
    config = read_config();
    update_cf(config);