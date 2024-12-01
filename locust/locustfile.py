from locust import HttpUser, task, TaskSet


class AuthBehavior(TaskSet):
    def login(self) -> str:
        response = self.client.post("/auth/login")
        access_token = response.json()["access_token"]
        return access_token

    #     email: str
    # password: str
    # fcm_token: str


class ScheduleBehavior(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
