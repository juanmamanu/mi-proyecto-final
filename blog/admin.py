from django.contrib import admin
from blog.models import Post, title , About

admin.site.register(title)
admin.site.register(Post)
admin.site.register(About)

admin.site.site_header = "pagina principal"
admin.site.site_title = "Portal de administracion"
admin.site.index_title ="bienvenido al portal de administracion"



