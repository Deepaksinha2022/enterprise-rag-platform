from locust import HttpUser, task

class RAGUser(HttpUser):

    @task
    def root(self):
        self.client.get("/")