########################################################################################################################
# IMPORTS

from django.db import models


########################################################################################################################
# MODELS

class User(models.Model):
    class Meta:
        verbose_name = 'Usuario'

    name = models.TextField('Nombre', primary_key=True)
    followers = models.IntegerField('Seguidores', default=0)
    place = models.TextField('Localización', null=True)


class Tweet(models.Model):
    pub_date = models.DateTimeField('Fecha')
    tweet_id = models.BigIntegerField('Id', default=0)
    author = models.ForeignKey(User, related_name='Usuario', on_delete=models.CASCADE, null=True)
    retweet_acolyte = models.ForeignKey(User, related_name='Retuiteador', on_delete=models.CASCADE, null=True)
    retweet_count = models.IntegerField('Retweets', default=0)
    direct_reference = models.BooleanField('Ref. Directa', default=False)
    text = models.TextField('Texto', primary_key=True)
    comment = models.TextField('Texto', max_length=140, null=True)
