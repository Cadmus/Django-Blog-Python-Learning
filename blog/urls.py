from django.urls import path
from django.views.generic import TemplateView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.views import *
from blog.feed import LatestPosts

info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'modified',
}

# Removed url pattern for `slug` to `[\w\-]+` and not `\S+`
# Because it will getting error 404 if use for '/' (homepage) and '/<slug>' (page/else)
# But, makesure the `url page` placed at the bottom from other urls.
# Example:
#   good: r'^(?P<slug>[\w\-]+)/$'
#   bad: r'^(?P<slug>\S+)/$'
# thanks to: http://stackoverflow.com/a/30271379/6396981

urlpatterns = [
    # Handler for Maintenance mode.
    # path(r'^$', TemplateView.as_view(template_name='maintenance.html', content_type='text/html')),

    path('', HomepageView.as_view(), name='homepage'),
    path('blog/<slug:slug>/', DetailPostView.as_view(), name='detail_post_page'),
    path('search/', SearchPostsView.as_view(), name='search_posts_page'),
    path('author/<str:username>/', AuthorPostsView.as_view(), name='author_posts_page'),
    path('tag/<slug:slug>/', TagPostsView.as_view(), name='tag_posts_page'),

    path('feed/', LatestPosts(), name="feed"),
    path('sitemap\.xml', sitemap, {'sitemaps': {'blog': GenericSitemap(
        info_dict, priority=0.6)}}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots\.txt/', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    path('sitemap/', SitemapView.as_view(), name='sitemap_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('trending/', TrendingPostsView.as_view(), name='trending_posts_page'),
    path('<slug:slug>/', DetailPageView.as_view(), name='detail_page'),
]
