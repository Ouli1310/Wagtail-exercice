from django.db import models


from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager



class HomePage(Page):
   def get_context(self, request):
        context = super().get_context(request)

        context['posts'] = Post.objects.child_of(self).live()

        return context


class Post(Page):
    user_name = models.CharField(max_length=250)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tags = ClusterTaggableManager(through='InstaPageTag', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('user_name'),
        ImageChooserPanel('image'),
        InlinePanel('comments', heading='Comments'),
        FieldPanel('tags'),
    ]

   

class InstaComments(Orderable):
    related_post = ParentalKey('Post', on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=255)

    panels = [
        FieldPanel('comment') 
    ]


class InstaPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'Post',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )

class ProfilPage(Page):
    def get_context(self, request):
        context = super().get_context(request)

        context['posts'] = Post.objects.child_of(self).live()

        return context