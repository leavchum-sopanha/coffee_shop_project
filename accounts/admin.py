from django.contrib import admin
from .models import * 
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ExportActionMixin

admin.site.site_header = "Coffee Shop System"
admin.site.site_title = "Coffee Shop Admin Panel"
admin.site.index_title = "Admin Panel"

class CoffeeMenuAdmin(admin.ModelAdmin):
   list_display = ["id", "name", "price", "short_description", "image_preview", "date_created"]
   list_filter = ["date_created"]
   search_fields = ["name"]
   date_hierarchy = "date_created"

   readonly_fields = ["image_preview"]

   def image_preview(self, obj):
      if obj.image:
         return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
      return "No Image"

   image_preview.short_description = 'Image Preview'

class CoffeeGalleryAdmin(admin.ModelAdmin):
   list_display = ["id", "name", "image_preview", "date_created"]
   list_filter = ["date_created"]
   search_fields = ["name"]
   date_hierarchy = "date_created"

   readonly_fields = ["image_preview"]

   def image_preview(self, obj):
      if obj.image:
         return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
      return "No Image"

   image_preview.short_description = 'Image Preview'

class CoffeeBlogAdmin(admin.ModelAdmin):
   list_display = ["id", "name", "short_description", "image_preview", "date_created"]
   list_filter = ["date_created"]
   search_fields = ["name"]
   date_hierarchy = "date_created"

   readonly_fields = ["image_preview"]

   def image_preview(self, obj):
      if obj.image:
         return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
      return "No Image"

   image_preview.short_description = 'Image Preview'

class BlogGalleryAdmin(admin.ModelAdmin):
   list_display = ["id", "name", "image_preview", "date_created"]
   list_filter = ["date_created"]
   search_fields = ["name"]
   date_hierarchy = "date_created"

   readonly_fields = ["image_preview"]

   def image_preview(self, obj):
      if obj.image:
         return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
      return "No Image"

   image_preview.short_description = 'Image Preview'

class CoffeeAboutAdmin(admin.ModelAdmin):
   list_display = ["id", "image_preview", "description", "video", "date_created"]
   list_filter = ["date_created"]
   search_fields = ["name"]
   date_hierarchy = "date_created"
   readonly_fields = ["image_preview"]

   def image_preview(self, obj):
      if obj.image:
         return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
      return "No Image"

   image_preview.short_description = 'Image Preview'

class CoffeeBannerAdmin(admin.ModelAdmin):
   list_display = ["id", "description", "date_created"]
   list_filter = ["date_created"]
   search_fields = ["name"]

   def image_preview(self, obj):
      if obj.image:
         return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
      return "No Image"

   image_preview.short_description = 'Image Preview'

class CoffeeTopMenuAdmin(admin.ModelAdmin):
   list_display = ["id", "name", "section_id", "date_created"]
   list_filter = ["date_created"]
   search_fields = ["name"]

   def image_preview(self, obj):
      if obj.image:
         return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
      return "No Image"

   image_preview.short_description = 'Image Preview'

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'review_text')

class FooterAdmin(admin.ModelAdmin):
    list_display = ('about_text',)

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('socialMediaName', 'socialMediaURL', 'socialMediaImage')
    search_fields = ["socialMediaName"]

    def image_preview(self, obj):
      if obj.socialMediaImage:
         return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
      return "No Image"

    image_preview.short_description = 'Image Preview'

# Register your models here.
admin.site.register(CoffeeMenu, CoffeeMenuAdmin)
admin.site.register(CoffeeGallery, CoffeeGalleryAdmin)
admin.site.register(CoffeeBlog, CoffeeBlogAdmin)
admin.site.register(CoffeeAbout, CoffeeAboutAdmin)
admin.site.register(CoffeeBanner, CoffeeBannerAdmin)
admin.site.register(CoffeeTopMenu, CoffeeTopMenuAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
