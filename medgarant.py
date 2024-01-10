from typing import Dict, List
from datetime import datetime, time, timedelta


busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:20', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]

gap30 = timedelta(minutes=30)


def str_to_time(str_date: str) -> time:
    return datetime.strptime(str_date, '%H:%M').time()


def dtc(time: time) -> datetime:
    return datetime.combine(datetime.min, time)


def get_gaps(scheldue: List[Dict[str, str]]) -> List[Dict[str, time]]:
    try:
        list_of_times = sorted(
            [str_to_time(item) for t in scheldue for item in t.values()])
    except (TypeError, ValueError) as e:
        raise e

    list_of_times.insert(0, time(9, 0))
    list_of_times.append(time(21, 0))

    final_list = []

    for i in range(1, len(list_of_times), 2):
        time_start = dtc(list_of_times[i])
        time_stop = dtc(list_of_times[i-1])
        td = time_start - time_stop

        while td >= gap30:
            final_list.append(
                {"start": time_stop.time(),
                 "stop": (time_stop + gap30).time()})
            time_stop += gap30
            td = time_start - time_stop

    return final_list


if __name__ == '__main__':
    gaps = get_gaps(busy)
    for t in gaps:
        print(f"{t['start']} - {t['stop']}")
