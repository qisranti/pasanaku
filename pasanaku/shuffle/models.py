from django.db import models
from django.contrib.auth.models import User

class PasanakuGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    bet = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Member(models.Model):
    group = models.ForeignKey(PasanakuGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    join_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} in {self.group.name}"

class Round(models.Model):
    group = models.ForeignKey(PasanakuGroup, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    received = models.BooleanField(default=False)
    received_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('group', 'order')
        ordering = ['order']

    def __str__(self):
        return f"Round {self.order} in {self.group.name} by {self.member.user.username}"

class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} by {self.member.user.username} for {self.round}"

class Invitation(models.Model):
    group = models.ForeignKey(PasanakuGroup, on_delete=models.CASCADE)
    email = models.EmailField()
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    invited_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Invitation to {self.email} by {self.invited_by.username} for {self.group.name}"
    

