from django.db import models

class MysqlBooleanField(models.BooleanField):

    def get_internal_type(self):
        return "MyBooleanField"

    # def db_type(self):
    #     return 'bit(1)'

    def from_db_value(self, value, expression, connection):
        if value in ('t', 'True', '1', b'\x01'): return True
        elif value in ('f', 'False', '0', b'\x00'): return False
        else: return None

    def to_python(self, value):
        if value in (True, False): return value
        if value in ('t', 'True', '1', b'\x01'): return True
        if value in ('f', 'False', '0', b'\x00'): return False

    # def get_db_prep_value(self, value, connection):
    #     return 0x01 if value else 0x00