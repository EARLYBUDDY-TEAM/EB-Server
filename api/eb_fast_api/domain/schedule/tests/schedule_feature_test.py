import pytest
from eb_fast_api.domain.schedule.sources import schedule_feature, schedule_schema
from datetime import datetime
from sqlalchemy.exc import IntegrityError


#  @pytest.mark.xfail(raises=IntegrityError)
#     def test_author_no_email(self, db_session):
#         author = Author(
#             firstname="James",
#             lastname="Clear"
#         )
#         db_session.add(author)
#         try:
#             db_session.commit()
#         except IntegrityError:
#             db_session.rollback()


# @pytest.mark.xfail(raises=IntegrityError)
# def test_create_schedule():
#     scheduleInfo = schedule_schema.ScheduleInfo(
#         title="title",
#         time=datetime.now(),
#         isNotify=False,
#     )
#     try:
#         schedule_feature.create_schedule(scheduleInfo)
#     except:
#         raise Exception()
