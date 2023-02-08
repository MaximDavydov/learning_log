from django.db import models


class Topic(models.Model):
    """Topic which learned user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returned string view of the model"""
        return self.text


class Entry(models.Model):
    """Information learned by user in the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returned string view of the model"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text[:50]}"
