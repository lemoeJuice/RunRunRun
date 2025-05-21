import requests


def get_id(token):
    """通过 token 向服务器查询 student_id"""

    headers = {
        'Host': 'tyxsjpt.seu.edu.cn',
        'xweb_xhr': '1',
        'miniappversion': 'minappv3.0.1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'tenant': 'NDEzMjAxMDI4Ng==',
        'token': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx5da07e9f6f45cabf/38/page-frame.html',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    url = 'https://tyxsjpt.seu.edu.cn/api/miniapp/studentMini/getStudentInfo'

    response = requests.get(url, headers=headers)

    data = response.json()

    return data['data']['id']
