from locust import HttpUser, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def test_endpoint(self):
        self.client.get("/app/addusers/")  # مسیر API خود را جایگزین کنید

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    host = "http://127.0.0.1:8000"  # آدرس سرور جنگو
    min_wait = 1000
    max_wait = 2000
