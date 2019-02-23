from django.contrib import admin
from book.models import BookInfo, PeopleInfo

admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'


class PeopleInfoStackInLine(admin.TabularInline):
    model = PeopleInfo #要关联的模型
    extra = 2 #附加编辑的数量


@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    inlines = [PeopleInfoStackInLine]

    list_per_page = 10
    actions_on_top = False
    actions_on_bottom = True
    list_display = ['id', 'name', 'readcount', 'bookname', 'people_name', 'image']
    list_filter = ['name']
    search_fields = ['name', 'id']
    # 调整编辑页显示
    # fields = ['name', 'pub_date']
    # fieldsets = (
    #     ('基本', {'fields': ['name', 'pub_date']}),
    #     ('高级', {
    #         'fields': ['readcount', 'commentcount'],
    #         'classes': ('collapse',)  # 是否折叠显示
    #     })
    # )


# Register your models here.
# admin.site.register(BookInfo)