from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    adreça = models.CharField(max_length=255)
    telefon = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Vehicle(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    any = models.IntegerField()
    matrícula = models.CharField(max_length=15, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='vehicles')

    def __str__(self):
        return f"{self.marca} {self.model} ({self.matrícula})"

class Article(models.Model):
    nom = models.CharField(max_length=100)
    preu = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nom

class OrdreReparacio(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='ordres_reparacio')
    data_inici = models.DateTimeField()
    data_fi = models.DateTimeField(null=True, blank=True)
    descripció = models.TextField()
    articles = models.ManyToManyField(Article, through='OrdreReparacioArticle')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Ordre {self.id} per {self.vehicle}"

class OrdreReparacioArticle(models.Model):
    ordre_reparacio = models.ForeignKey(OrdreReparacio, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantitat = models.IntegerField()

    def __str__(self):
        return f"{self.quantitat} x {self.article.nom} per {self.ordre_reparacio}"

