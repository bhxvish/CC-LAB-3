from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        # Simulate different users
        self.username = "locust_user"

        # Common headers (extendable)
        self.headers = {
            "Accept": "application/json"
        }

    @task
    def view_my_events(self):
        with self.client.get(
            "/my-events",
            params={"user": self.username},
            headers=self.headers,
            name="View My Events",
            catch_response=True
        ) as response:

            if response.status_code != 200:
                response.failure(f"Failed with status {response.status_code}")
            else:
                response.success()

