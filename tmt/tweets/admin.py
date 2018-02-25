########################################################################################################################
# IMPORTS

from django.contrib import admin

from .models import Tweet, User
from .views import send_answer


########################################################################################################################
# CLASSES

class UserAdmin(admin.ModelAdmin):
    ordering = (
        'name',
    )

    readonly_fields = (
        'name',
        'followers',
        'place',
        'twitter_link',
    )

    list_display = readonly_fields

    search_fields = (
        'name',
    )

    # Define user link in Twitter
    def twitter_link(self, author):
        if author is not None:
            link = "https://twitter.com/{0}".format(author.name)
            return '<a href="{0}" target="_blank">{0}</a>'.format(link)

    twitter_link.allow_tags = True


class TweetAdmin(admin.ModelAdmin):
    ordering = (
        '-pub_date',
    )

    readonly_fields = (
        'text',
        'pub_date',
        'direct_reference',
        'usuario',
        'retuiteador',
        'retweet_count',
        'twitter_link',
    )

    fieldsets = (
        (None, {
            'fields': readonly_fields
        }),
        ('Respuesta en Twitter', {
            'fields': ('comment',)
        }),
    )

    list_display = (
        'text',
        'pub_date',
        'direct_reference',
        'usuario',
        'retweet_count',
    )

    search_fields = (
        'text',
        'author__name',
    )

    list_filter = (
        'direct_reference',
    )

    # Define tweet link in Twitter
    def twitter_link(self, tweet):
        if tweet is not None:
            link = "https://twitter.com/{0}/status/{1}".format(tweet.author.name, str(tweet.tweet_id))
            return '<a href="{0}" target="_blank">{0}</a>'.format(link)

    twitter_link.allow_tags = True

    # Define user link
    def user_link(self, author):
        if author is not None:
            return '<a href="/tweets/user/{0}/change">{0}</a>'.format(author.name)

    # Link to author
    def usuario(self, tweet):
        if tweet is not None:
            return self.user_link(tweet.author)

    usuario.allow_tags = True

    # Link to acolyte
    def retuiteador(self, tweet):
        if tweet is not None:
            return self.user_link(tweet.retweet_acolyte)

    retuiteador.allow_tags = True

    # Override default save action to send response in Twitter
    def save_model(self, request, tweet, form, change):
        if tweet.comment is not None and tweet.tweet_id != 0:
            if tweet.retweet_acolyte is not None:
                send_answer(tweet.comment, tweet.author.name, tweet.tweet_id, tweet.retweet_acolyte.name)
            else:
                send_answer(tweet.comment, tweet.author.name, tweet.tweet_id)
        tweet.save()


########################################################################################################################
# REGISTRATION

admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)
