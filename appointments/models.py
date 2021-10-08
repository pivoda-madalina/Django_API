from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    e_mail = models.EmailField(unique=True)
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Appointment(models.Model):
    CH_s = (('Mani', 'Mani'), ('Pedi', 'Pedi'))
    CH_t = (('Semi', 'Semi'), ('Gel', 'Gel'), ('Classic', 'Classic'))

    person = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    service = models.CharField(max_length=50, choices=CH_s)
    type = models.CharField(max_length=50, choices=CH_t)

    def __str__(self):
        return f"Appointment: {self.person}, {self.service}, {self.type}, {self.start_date}."
