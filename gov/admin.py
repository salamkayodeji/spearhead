from django.contrib import admin

#Register your models here.
from .models import Post
from .models import Category
from .models import event
from .models import Gallery
from .models import contact
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category', )


class PostAdmin(admin.ModelAdmin):
    ...
    search_fields = ('coursename', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(event)
admin.site.register(Gallery)
admin.site.register(contact)

