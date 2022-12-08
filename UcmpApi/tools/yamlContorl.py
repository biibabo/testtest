import yaml


def read_yaml():
    with open('../data/Create_Ucloud_host.yaml', mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        # stream = f :文件流，Loader=yaml.FullLoader：加载所有数据
        return value


if __name__ == '__main__':
    read_yaml()
