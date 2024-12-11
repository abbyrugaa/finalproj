from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between tasks in seconds (random between 1 to 3)

    @task
    def get_homepage(self):
        # Task to simulate a GET request to the homepage
        self.client.get("/quizzes")
