import yaml
import json

if __name__ == '__main__':
    # 给定的 YAML 数据
    yaml_data = """
    payload:
      - '+.0008d6ba2e.com'
      - '+.000dn.com'
      - '+.0013.cc'
    """

    # 解析 YAML 数据
    f = open("Anti-Ad Clash.yaml", encoding="utf-8")
    parsed_yaml = yaml.load(f, Loader=yaml.FullLoader)
    # 提取域名
    domains = [entry[2:] for entry in parsed_yaml['payload']]

    # 构造 JSON 数据
    json_data = {
        "version": 1,
        "rules": [
            {
                "domain": domains
            }
        ]
    }
    # 将 JSON 数据保存到文件
    with open('domains.json', 'w') as json_file:
        json.dump(json_data, json_file)
    print(json_data)
