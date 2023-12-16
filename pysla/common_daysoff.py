from datetime import date, time
from .daterange import DateRange
from .daily_shifts import Shift, DailyShift
from .datetime_utilities import check_valid_weekday
from pydantic import AfterValidator
from typing_extensions import Annotated
from typing import Set


WEEKDAY = Annotated[int, AfterValidator(check_valid_weekday)]
WEEKDAYS = Set[WEEKDAY]

VIETNAM_VICTORY_DAY = DateRange.fromstr("20240430")
SOLAR_NEW_YEAR = DateRange.fromstr("20240101")
INTERNATIONAL_LABOR_DAY = DateRange.fromstr("20240501")
VIETNAM_INDEPENDENT_DAY = DateRange.fromstr("20240902-20240903")
LUNAR_NEW_YEAR = DateRange.fromstr("20240101-20240105", calendar_type="lunar")
THE_HUNG_KINGS_TEMPLE_FESTIVAL = DateRange.fromstr(
    "20240310", calendar_type="lunar"
)
COMMON_WORKDAYS_IN_WEEK: WEEKDAYS = {0, 1, 2, 3, 4}
COMMON_DAILY_SHIFTS = DailyShift(
    [
        Shift(start=time(8, 30), end=time(11, 45)),
        Shift(start=time(13, 15), end=time(17, 45)),
    ]
)
