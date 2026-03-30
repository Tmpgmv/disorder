class ReadOnlyAdminMixin:
    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            # New objects: all editable
            return []

        if obj.unlocked:
            # Все редактируется, если unlocked.
            return []
        else:
            all_fields = [field.name for field in self.model._meta.fields]
            # 'unlocked' всегда можно редактировать.
            return [field for field in all_fields if field != 'unlocked']