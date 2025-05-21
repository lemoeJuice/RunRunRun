from .time_util import calculate_speed, format_display_time
from .image_upload import upload_image
from .save_record import save_start_record, save_final_record


def run_example(student_id: str, token: str, start_image: str, finish_image: str, track_data: str,
                date: str, start_time: str, finish_time: str, seconds: int, distance: float, calorie: int):
    """
    模拟提交一次跑步打卡记录，包括起始照片、时间、距离和消耗卡路里等信息。
    Args:
        student_id (str): 可以根据 token 在 get_student_id.py 中获得
        token (str): 获得方法请自行了解
        start_image (str): 起跑照片的本地路径
        finish_image (str): 终点照片的本地路径
        track_data (str）: 可参考 tracks.py 自行生成
        date (str): 跑步日期，格式为 'YYYY-MM-DD'
        start_time (str): 跑步开始时间，格式为 'HH:MM:SS'
        finish_time (str): 跑步结束时间，格式为 'HH:MM:SS'
        seconds (int): 跑步持续时间（单位：秒）
        distance (float): 跑步距离（单位：公里）
        calorie (int): 本次运动消耗的卡路里

    Returns:
        None

    Note:
        该函数仅作示例。实际的校验内容较少，但仍不推荐直接使用。请自行确保上传操作的合理性，本项目不对直接/间接使用造成的一切后果承担责任.
    """

    info = {
        'student_id': student_id,
        'token': token,

        'date': date,
        'start_time': start_time,
        'finish_time': finish_time,
        'display_time': format_display_time(seconds),
        'seconds': str(seconds),
        'distance': str(distance),
        'speed': calculate_speed(seconds, distance),
        'calorie': str(calorie),
        'track_data': track_data
    }

    # headers 会被修改，但是在这里并不影响
    headers = {
        'Host': 'tyxsjpt.seu.edu.cn',
        'token': f'Bearer {token}',
        'miniappversion': 'minappv3.0.1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; V2284A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160253 MMWEBSDK/20240301 MMWEBID/4107 MicroMessenger/8.0.48.2580(0x28003036) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'tenant': 'NDEzMjAxMDI4Ng=='
    }

    # 上传开始图片
    start_img_url = upload_image(headers, start_image, 'start')

    # 上传结束图片
    finish_img_url = upload_image(headers, finish_image, 'finish')

    # 保存开始记录
    record_id = save_start_record(headers, info, start_img_url)

    # 保存最终记录
    save_final_record(headers, info, start_img_url, finish_img_url, record_id)
