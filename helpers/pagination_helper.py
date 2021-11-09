from django.http import HttpResponse
from global_settings import pagination_settings


class PaginationTool:
    page = None
    limit = None
    object = None
    offset = None

    def __init__(self, request, object):
        self.object = object
        self.page = request.GET.get('page')
        self.limit = request.GET.get('limit')

    def set_limit_and_offset(self):
        self.page = int(self.page)
        self.limit = int(self.limit)
        offset = (self.page * self.limit) - self.limit
        self.offset = offset
        self.limit = offset + self.limit

    def set_page_and_limit(self):
        if not self.validate_args():
            self.page = pagination_settings.default_pagination_page
            self.limit = pagination_settings.default_pagination_limit

    def get_data(self):
        if not self.validate_args():
            self.page = pagination_settings.default_pagination_page
            self.limit = pagination_settings.default_pagination_limit
        self.set_limit_and_offset()

        return self.object.__class__.objects.all()[self.offset:self.limit]

    def validate_args(self):

        if self.page is None or self.limit is None:
            return False

        if self.page.isnumeric() is False or self.limit.isnumeric() is False:
            return False

        if int(self.page) <= 0 or int(self.limit) <= 0:
            return False

        return True
