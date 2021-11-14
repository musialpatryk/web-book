from global_settings import pagination_settings


#TODO: wiecej informacji o bledach, na ktorych podstawie tylko bledne wartosci beda przywracane do domyslnych?
class PaginationTool:
    page = None
    limit = None
    # object = None
    offset = None

    def __init__(self, page, limit):
        # self.object = object
        self.page = page
        self.limit = limit

    def set_limit_and_offset(self):
        self.page = int(self.page)
        self.limit = int(self.limit)
        offset = (self.page * self.limit) - self.limit
        self.offset = offset
        self.limit = offset + self.limit

    def get_data(self):
        self.prepare_data()
        return self.offset, self.limit
        # return self.object.__class__.objects.all()[self.offset:self.limit]

    def prepare_data(self):
        if not self.validate_args():
            self.page = pagination_settings.default_pagination_page
            self.limit = pagination_settings.default_pagination_limit
        self.set_limit_and_offset()

    def validate_args(self):
        if self.page is None or self.limit is None:
            return False

        if self.page.isnumeric() is False or self.limit.isnumeric() is False:
            return False

        if int(self.page) <= 0 or int(self.limit) <= 0:
            return False

        if int(self.limit) not in pagination_settings.pagination_limits:
            return False

        return True
