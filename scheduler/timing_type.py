from typing import Union
import datetime as dt

from scheduler.trigger.core import Weekday

# execution interval
TimingCyclic = dt.timedelta  # Scheduler
_TimingCyclicList = list[TimingCyclic]

# time on the clock
_TimingDaily = dt.time  # JobTimer
# TimingDaily = Union[dt.time, list[dt.time]]
_TimingDailyList = list[_TimingDaily]  # Job
TimingDailyUnion = Union[_TimingDaily, _TimingDailyList]  # Scheduler

# day of the week or time on the clock
_TimingWeekly = Weekday
_TimingWeeklyList = list[_TimingWeekly]
TimingWeeklyUnion = Union[_TimingWeekly, _TimingWeeklyList]  # Scheduler

TimingJobTimerUnion = Union[TimingCyclic, _TimingDaily, _TimingWeekly]  # JobTimer
TimingJobUnion = Union[_TimingCyclicList, _TimingDailyList, _TimingWeeklyList]  # Job

TimingOnceUnion = Union[
    dt.datetime, TimingCyclic, _TimingWeekly, _TimingDaily
]  # Scheduler.once