from locust import HttpUser, task, TaskSet, events
from typing import Optional
import requests
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo


access_token: Optional[str] = None


class ScheduleBehavior(HttpUser):
    def create_schedule_info(self) -> ScheduleInfo:
        mock_schedule_info = ScheduleInfo.mock()
        mock_schedule_info.time = eb_datetime.get_datetime_now()
        return mock_schedule_info

    def create_path_info(self) -> PathInfo:
        mock_path_info = PathInfo.mock()
        return mock_path_info

    @task
    def task_create_schedule(self):
        path = "/schedule/create"
        schedule_info = self.create_schedule_info()
        path_info = self.create_path_info()
        json = {
            "scheduleInfo": schedule_info.model_dump(mode="json"),
            "pathInfo": path_info.model_dump(mode="json"),
        }
        headers = {"access_token": access_token}
        self.client.post(
            path,
            json=json,
            headers=headers,
        )


def get_global_access_token(host: str) -> str:
    path = "/auth/login"
    json = {
        "email": "abc@abc.com",
        "password": "abcd12",
        "fcm_token": "fcm_token",
    }
    with requests.post(host + path, json=json) as response:
        response_dict = response.json()
        print(response_dict)
        tmp_access_token = response_dict["accessToken"]
        return tmp_access_token


@events.test_start.add_listener
def setup_locust(environment, **kwargs):
    global access_token
    access_token = get_global_access_token(environment.host)
    print(access_token)
