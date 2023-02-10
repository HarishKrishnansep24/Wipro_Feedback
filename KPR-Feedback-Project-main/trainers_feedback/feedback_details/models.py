from django.db import models

# Create your models here.


class trainer_data(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    phone_no = models.BigIntegerField()

    def __str__(self):
        return self.id


class trainer_feedback(models.Model):
    train_id = models.ForeignKey(
        trainer_data, related_name='code_submit', on_delete=models.CASCADE, default="EC0000")
    # train_data = models.CharField(max_length=20, blank=True)
    communicatin_skill = models.IntegerField()
    content_delivered = models.IntegerField()
    doubt_clarification = models.IntegerField()
    technical_skill = models.IntegerField()
    feedback = models.CharField(max_length=500)
    review = models.CharField(max_length=20, blank=True)
