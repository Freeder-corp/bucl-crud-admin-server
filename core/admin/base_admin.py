class BaseReadOnlyAdminMixin:

    def has_add_permission(self, request):
        return False
    
    def had_exchange_permission(self, request, obj=None):
        return False


    def has_delete_permission(self, request, obj=None):
        return False
    
    def get_list_display(self, request, obj=None):
        list_display_field = []
        for field in self.opts.local_fields:
            list_display_field.append(field.name)
        
        for field in self.opts.local_many_to_many:
            list_display_field.append(field.name)
    
        return list(set(list_display_field))
    
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = []
        for field in self.opts.local_fields:
            readonly_fields.append(field.name)

        for field in self.opts.local_many_to_many:
            readonly_fields.append(field.name)
    
        # make all fields readonly
        readonly_fields = list(set(readonly_fields))
        
        return readonly_fields
    
class BaseReadOnlyAndWriteAdminMixin:

    def get_list_display(self, request, obj=None):
        list_display_field = []
        for field in self.opts.local_fields:
            list_display_field.append(field.name)
        
        for field in self.opts.local_many_to_many:
            list_display_field.append(field.name)
    
        return list(set(list_display_field))
    
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = []
        for field in self.opts.local_fields:
            readonly_fields.append(field.name)

        for field in self.opts.local_many_to_many:
            readonly_fields.append(field.name)
    
        # make all fields readonly
        readonly_fields = list(set(readonly_fields))
        
        return readonly_fields