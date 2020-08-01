from django.db import models

# Create your models here.
class OpcuaServerInfo(models.Model):
    server_id = models.CharField(max_length= 50)
    server_name = models.CharField(max_length= 100)
    endpoint_url = models.CharField(max_length= 200)
    server_description = models.CharField(max_length= 500)

    def __str__(self):
        return f"{self.server_id} : {self.server_name} : {self.endpoint_url} : {self.server_description} "

