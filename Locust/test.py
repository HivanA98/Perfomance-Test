from locust import HttpUser, between, task

class SauceDemoUser(HttpUser):
    host = "https://www.saucedemo.com"
    wait_time = between(1, 5)
    
    def on_start(self):
        # Melakukan login saat user pertama kali memulai
        self.login()
from locust import HttpUser, between, task

class SauceDemoUser(HttpUser):
    host = "https://www.saucedemo.com"
    wait_time = between(1, 5)
    
    def on_start(self):
        # Melakukan login saat user pertama kali memulai
        self.login()

    def login(self):
        # Request POST ke endpoint login
        response = self.client.post("/",
                                    data={"username": "standard_user",
                                          "password": "secret_sauce"})
        if response.status_code == 200:
            print("Login successful")
        else:
            print("Login failed:", response.status_code)
            print(response.text)
    
    @task
    def view_inventory(self):
        # Mengakses halaman inventory setelah login
        self.client.get("/inventory.html")

    @task
    def view_about(self):
        # Mengakses halaman about
        self.client.get("/about.html")

    def login(self):
        # Request POST ke endpoint login
        response = self.client.get("/",
                                    data={"username": "standard_user",
                                          "password": "secret_sauce"})
        if response.status_code == 200:
            print("Login successful")
        else:
            print("Login failed:", response.status_code)
            print(response.text)
    
    @task
    def view_inventory(self):
        # Mengakses halaman inventory setelah login
        self.client.get("/inventory.html")

    @task
    def view_about(self):
        # Mengakses halaman about
        self.client.get("/about.html")
