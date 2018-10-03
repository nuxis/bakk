from django.db import models


class BadgeAccess(models.Model):
    card = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        active = ""
        if not self.active:
            active = " :: [NOT ACTIVE]"
        return "{} :: {}{}".format(self.description, self.card, active)

    class Meta:
        unique_together = ('card', 'active')


class BadgeAccessLog(models.Model):
    card = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    badgeaccess = models.ForeignKey(BadgeAccess, blank=True, null=True, on_delete=models.CASCADE)
    request_ip = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
