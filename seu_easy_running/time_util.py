def calculate_speed(seconds: int, distance: float) -> str:
    """计算配速（分钟/公里）"""
    mins_per_km = (seconds / 60) / float(distance)
    minutes = int(mins_per_km)
    seconds = int((mins_per_km - minutes) * 60)
    return f"{minutes}'{seconds}''"


def format_display_time(seconds: int) -> str:
    """将秒数格式化为显示时间（HH:MM:SS）"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"
