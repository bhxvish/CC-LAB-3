from locust import HttpUser, task, between

class EventsUser(HttpUser):
    # Consistent and realistic wait time
    wait_time = between(1, 2)

    def on_start(self):
        """
        Runs once when the user starts.
        Helps simulate a real user session.
        """
        self.user = "locust_user"

    @task
    def view_events(self):
        # Name groups all /events requests together in Locust UI
        with self.client.get(
            f"/events?user={self.user}",
            name="/events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure("Failed to load events")
            else:
                response.success()
