from django.urls import path
from Dragster.Routes import NoCodeViews, BlogViews, common, AI_Functions
from NoCodify import settings
from django.conf.urls.static import static

# Initilizes........................

urlpatterns = []


def Make_Join(Componets):
    OutComponets = []
    for i in Componets:
        for j in i:
            OutComponets.append(j)
    return OutComponets


# Paths.............................

NoCodeMaker = [
    path('view_pages', NoCodeViews.index, name='home'),
    path('', common.home, name='home'),
    path('home', common.home, name='home'),
    path('connect_metamask', common.connect_metamask, name='connect_metamask'),
    path('DisConnect', common.DisConnect, name='DisConnect'),
    path('save_wallet_address', common.save_wallet_address, name='save_wallet_address'),
    
    path('blog', common.blog, name='blog'),
    
    path('add', NoCodeViews.addPage, name="addpage"),
    path('edit/<id>', NoCodeViews.editPage, name="editpage"),
    path('page/create', NoCodeViews.savePage, name="create_page"),
    path('editPage/<id>', NoCodeViews.editPageContent, name="editPageContent"),
    path('preview/<id>', NoCodeViews.previewPage, name='previewPage'),
    path('Download_file', NoCodeViews.Download_file, name='Download_file'),
    path('chat_view', NoCodeViews.chat_view, name='chat_view'),
    path('url', NoCodeViews.url, name='url'),
    path('edits', NoCodeViews.edits, name='edits'),
    path('ResumeBuilder', NoCodeViews.ResumeBuilder, name='ResumeBuilder'),
    path('block_detials/<str:block>',
         NoCodeViews.block_detials, name='block_detials'),
    path('blog_block_detials/<str:block>',
         NoCodeViews.blog_block_detials, name='blog_block_detials'),
]

BlogBuilder = [
    path('list_blog', BlogViews.list_blog),
    path('list_edit_blog', BlogViews.list_edit_blog),
    path('view_blog/<str:pk>', BlogViews.view_blog),
    path('edit_blog/<str:pk>', BlogViews.edit_blog),
    path('blog_edit', BlogViews.blog_edit),
    path('save_blog', BlogViews.save_blog),
    path('delete_blog', BlogViews.delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>', BlogViews.save_edit_blog),
]

AI_functions = [
    path('chatbot_res', AI_Functions.chatbot_res,name="chatbot_res"),
]

# Add Paths Together..............

urlpatterns.extend(Make_Join([NoCodeMaker, BlogBuilder, AI_functions]))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
