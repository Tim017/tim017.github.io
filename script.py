import requests
import yaml
import re

# 1 Fetch MD file
URL = "https://raw.githubusercontent.com/crossxx-labs/free-proxy/refs/heads/main/README.md"
response = requests.get(URL)
if response.status_code != 200:
    raise Exception(f"Failed to fetch data from {URL}")

# 2 Extract link from MD content
markdown_content = response.text
pattern = r'https:\/\/clash\.crossxx\.com\/sub\/vmess\/(\d+)'
match = re.search(pattern, markdown_content)

# 3 Save URL to one yaml file
if match:
    yaml_url = f"https://clash.crossxx.com/sub/vmess/{match.group(1)}"
    print(yaml_url)
    response = requests.get(yaml_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {URL}")
    else:
        yaml_text = response.content.decode('utf-8')
        data = yaml.safe_load(yaml_text)
        with open("data.yaml", "w", encoding="utf-8") as yaml_file:
            yaml.dump(data, yaml_file, allow_unicode=True, sort_keys=False)
