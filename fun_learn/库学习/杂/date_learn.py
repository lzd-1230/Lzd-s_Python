"""
python中有效的基本时间类型
class datetime.date
一个理想化的简单型日期，它假设当今的公历在过去和未来永远有效。 属性: year, month, and day。

class datetime.time
一个独立于任何特定日期的理想化时间，它假设每一天都恰好等于 24*60*60 秒。包含属性: hour, minute, second, microsecond 和 tzinfo。

class datetime.datetime
日期和时间的结合。属性：year, month, day, hour, minute, second, microsecond, and tzinfo.
"""
from datetime import date
print(date.today().year)
text = "2019-11-22"
print(*map(int,text.split("-")))
