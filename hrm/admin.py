from django.contrib import admin

# Register your models here.
class MultiDBModelAdmin(admin.ModelAdmin):
    # Using which database for this model
    using = "hrm"
    def save_model(self, request, obj, form, change):
        # Tell django to save objects to the 'accounts' database.
        obj.save(using=self.using)
        
    def delete_model(self, request, obj):
        obj.delete(using=self.using)
        
    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)
