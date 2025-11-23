from locust import HttpUser, task, between

class DjangoUser(HttpUser):
    wait_time = between(1, 3)
    token = None

    def on_start(self):
        # Obtener JWT antes de iniciar carga
        response = self.client.post("/api/token/", json={
            "username": "Joelito",
            "password": "1234"
        })
        self.token = response.json().get("access")

    @task
    def get_users(self):
        self.client.get(
            "/api/users/",
            headers={"Authorization": f"Bearer {self.token}"}
        )
