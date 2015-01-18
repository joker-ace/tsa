from django.db import models

from queries.models import Query


class Tweet(models.Model):
    query = models.OneToOneField(Query)
    text = models.CharField(max_length=140, null=False, db_index=True)
    date = models.CharField(max_length=50, null=False)
    hashtags = models.CharField(max_length=100, null=True, default=None)
    twitter_user = models.CharField(max_length=100, null=False)
    tweet_id = models.BigIntegerField(null=False, db_index=True)

    def __unicode__(self):
        return u'Tweet #' + unicode(self.tweet_id)

    def to_dict(self):
        return {
            'query': self.pk,
            'text': self.text,
            'date': self.date,
            'hashtags': self.hashtags,
            'user': self.twitter_user,
            'id': self.tweet_id
        }