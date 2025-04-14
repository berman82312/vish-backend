from django.db import models

# Create your models here.

class LatestRateCardManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_latest=True, is_archived=False)

class RateCard(models.Model):
    class Meta:
        db_table = 'rate_cards'
    
    MILESTONE1 = 'm1'
    MILESTONE2 = 'm2'
    MILESTONE3 = 'm3'
    MILESTONE4 = 'm4'
    MILESTONE5 = 'm5'
    MILESTONE6 = 'm6'
    MILESTONE7 = 'm7'
    MILESTONE_CHOICES = [
        (MILESTONE1, 'M1'),
        (MILESTONE2, 'M2'),
        (MILESTONE3, 'M3'),
        (MILESTONE4, 'M4'),
        (MILESTONE5, 'M5'),
        (MILESTONE6, 'M6'),
        (MILESTONE7, 'M7'),
    ]

    HOUR = 'hour'
    HUMANDAY = 'humanday'
    MONTHLY = 'monthly'
    ONETIME = 'onetime'
    UNIT_CHOICES = [
        (HOUR, 'Hour'),
        (HUMANDAY, 'Human Day'),
        (MONTHLY, 'Monthly'),
        (ONETIME, 'One Time'),
    ]
    
    milestone = models.CharField(max_length=20, choices=MILESTONE_CHOICES, default=MILESTONE1)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(max_length=100, choices=UNIT_CHOICES, default=ONETIME)
    default_amount = models.PositiveSmallIntegerField(default=1)
    min_amount = models.PositiveSmallIntegerField(default=1)
    is_recurring = models.BooleanField(default=False)
    is_latest = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    version = models.PositiveSmallIntegerField(default=1)
    description = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archived_at = models.DateTimeField(blank=True, null=True)

    business_model = models.ForeignKey(
        'BusinessModel',
        on_delete=models.DO_NOTHING,
        related_name='rate_cards'
    )
    service_categories = models.ManyToManyField(
        'ServiceCategory',
        related_name='rate_cards'
    )

    service_areas = models.ManyToManyField(
        'ServiceArea',
        related_name='rate_cards'
    )

    include_rate_cards = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='related_rate_cards'
    )

    objects = models.Manager()
    latest = LatestRateCardManager()

    def __str__(self):
        return self.name


class BusinessModel(models.Model):
    class Meta:
        db_table = 'business_models'
    
    title = models.CharField(max_length=100)
    description = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    class Meta:
        db_table = 'service_categories'
    
    title = models.CharField(max_length=100)
    description = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ServiceArea(models.Model):
    class Meta:
        db_table = 'service_areas'
    
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ExchangeRate(models.Model):
    class Meta:
        db_table = 'exchange_rates'
    
    currency = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    is_latest = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archived_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
