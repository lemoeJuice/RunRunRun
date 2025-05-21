import requests
import json
import os


def upload(url, headers, image_path):
    headers['Referer'] = 'https://servicewechat.com/wx5da07e9f6f45cabf/38/page-frame.html'

    with open(image_path, 'rb') as image_file:
        response = requests.post(
            url=url,
            headers=headers,
            files={'file': (os.path.basename(image_path), image_file, 'image/jpeg')}
        )
        return response


def upload_image(headers: dict, image_path: str, image_type: str) -> str:
    """上传图片并返回图片 URL"""
    url_pairs = {'start': f"https://{headers['Host']}/api/miniapp/exercise/uploadRecordImage",
                 'finish': f"https://{headers['Host']}/api/miniapp/exercise/uploadRecordImage2"}

    response = upload(url_pairs[image_type], headers, image_path)
    if response.status_code == 200:
        image_url = json.loads(response.text)['data']
        return image_url
    else:
        raise Exception(
            f'Failed to upload {image_type} image. Status Code: {response.status_code}. Response: {response.text}')
