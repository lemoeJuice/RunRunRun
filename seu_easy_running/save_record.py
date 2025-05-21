import requests
import json

plan_config = {
    'planId': '403640124545491473',
    'routeName': '桃园田径场',
    'routeRule': '九龙湖校区',
    'ruleId': '402186368309502988',
    'maxTime': 12,
    'minTime': 4,
    'orouteKilometre': 1.2,
    'ruleStartTime': '06:00',
    'ruleEndTime': '22:00'
}


def send_request(url, headers, data):
    # 设置请求头
    headers.update({'content-type': 'application/json;charset=utf-8',
                    'Referer': 'https://servicewechat.com/wx5da07e9f6f45cabf/38/page-frame.html',
                    'charset': 'utf-8'})

    data.update(plan_config)

    response = requests.post(url, headers=headers, json=data)

    return response


def save_start_record(headers: dict, info: dict, start_img_url: str) -> str:
    """保存开始记录并返回记录ID"""
    url = f"https://{headers['Host']}/api/exercise/exerciseRecord/saveStartRecord"

    data = {
        'recordTime': info['date'],
        'startTime': info['start_time'],
        'endTime': '',
        'dispTimeText': 0,
        'exerciseTimes': '',
        'routeKilometre': '',
        'speed': "0'00''",
        'calorie': 0,

        'startImage': start_img_url,
        'endImage': '',

        'studentId': info['student_id'],
        'strLatitudeLongitude': []
    }

    response = send_request(url, headers, data)

    if response.status_code == 200:
        record_id = json.loads(response.text)['data']
        return record_id
    else:
        raise Exception(f'Request failed with status code {response.status_code}. Response: {response.text}')


def save_final_record(headers: dict, info: dict,
                      start_img_url: str, finish_img_url: str, record_id: str) -> None:
    """保存最终记录"""
    url = f"https://{headers['Host']}/api/exercise/exerciseRecord/saveRecord"

    data = {
        'recordTime': info['date'],
        'startTime': info['start_time'],
        'endTime': info['finish_time'],
        'dispTimeText': info['display_time'],
        'exerciseTimes': info['seconds'],
        'routeKilometre': info['distance'],
        'speed': info['speed'],
        'calorie': info['calorie'],

        'startImage': start_img_url,
        'endImage': finish_img_url,

        'id': record_id,
        'studentId': info['student_id'],
        'strLatitudeLongitude': info['track_data'],
        'nowStatus': 2
    }

    response = send_request(url, headers, data)

    if response.status_code != 200:
        raise Exception(f'Request failed with status code {response.status_code}. Response: {response.text}')
