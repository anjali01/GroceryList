from django.contrib import admin

@admin.register(GroceryList)
class GroceryListAdmin(admin.ModelAdmin):
    pass