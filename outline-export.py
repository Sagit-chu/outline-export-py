import requests
import json
import datetime
import time
import os
########################################################################
# 说明
# docker镜像使用方法
# 添加环境变量，URL, TOKEN
# 映射路径 /data 为备份储存的路径
########################################################################
# 获取环境变量-获取URL地址和TOKEN，URL示例https://example.com:port
url0 = os.environ.get('URL')
token = os.environ.get('TOKEN')

headers = {"Authorization": "Bearer "+token}
url = ''.join([url0, '/api/collections.export_all'])

# 请求备份
response = requests.post(url, headers=headers)
# 判断请求返回是否为200
if response.status_code != 200:
    print('导出失败 Status code =', response.status_code)

# 解析返回的JSON
j = json.dumps(response.json(), indent=4, sort_keys=True,
               separators=(',', ': '), ensure_ascii=False)
response_data = json.loads(j)

# print(response_data)
# ID 文件的ID
id = response_data['data']['fileOperation']['id']

# 拼接下载链接
downloadUrl = ''.join([url0, '/api/fileOperations.redirect?id=', id])

# print(downloadUrl)
# 下载
# 睡眠30秒，等待备份文件生成
time.sleep(30)
d = requests.get(downloadUrl, headers=headers)
filename = ''.join(
    ['/data', datetime.datetime.now().strftime('%Y%m%d%H%M'), response_data['data']['fileOperation']['name']])
# 下载储存文件
print(filename)
open(filename, 'wb').write(d.content)
