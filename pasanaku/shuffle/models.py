from django.db import models
from django.contrib.auth.models import User
from .validators import validate_amount, validate_payment_day

class PasanakuGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    bet = models.DecimalField(max_digits=10, decimal_places=2)
    payment_day = models.PositiveIntegerField(validators=[validate_payment_day])
    rounds = models.PositiveIntegerField()
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
        return f"{self.user.username} del grupo {self.group.name}"

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
        return f"Cuota {self.order} del {self.group.name} por el usuario {self.member.user.username}"

class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        super().clean()
        expected_paid = self.round.group.bet
        validate_amount(self.amount, expected_paid)
    
    def __str__(self):
        return f"{self.amount} de {self.member.user.username} para la cuota: {self.round}"

class Invitation(models.Model):
    group = models.ForeignKey(PasanakuGroup, on_delete=models.CASCADE)
    email = models.EmailField()
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    invited_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Invitacion para {self.email} de {self.invited_by.username} para el grupo {self.group.name}"
    

