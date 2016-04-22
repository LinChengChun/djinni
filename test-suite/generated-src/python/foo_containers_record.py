# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from foo_containers.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyBinary, CPyBoxedI32, CPyDate, CPyObject, CPyObject, CPyObjectProxy, CPyPrimitive, CPyRecord, CPyString

from dh__list_binary import ListBinaryHelper
from dh__list_date import ListDateHelper
from dh__list_int32_t import ListInt32THelper
from dh__list_list_string import ListListStringHelper
from dh__list_optional_binary import ListOptionalBinaryHelper
from dh__list_record_foo_some_other_record import ListRecordFooSomeOtherRecordHelper
from dh__list_string import ListStringHelper
from dh__map_boxed_int32_t_set_string import MapBoxedInt32TSetStringHelper
from dh__map_boxed_int32_t_set_string import MapBoxedInt32TSetStringProxy
from dh__map_int8_t_list_date import MapInt8TListDateHelper
from dh__map_int8_t_list_date import MapInt8TListDateProxy
from dh__map_int8_t_set_string import MapInt8TSetStringHelper
from dh__map_int8_t_set_string import MapInt8TSetStringProxy
from dh__map_optional_string_optional_string import MapOptionalStringOptionalStringHelper
from dh__map_optional_string_optional_string import MapOptionalStringOptionalStringProxy
from dh__map_string_int32_t import MapStringInt32THelper
from dh__map_string_int32_t import MapStringInt32TProxy
from dh__map_string_string import MapStringStringHelper
from dh__map_string_string import MapStringStringProxy
from dh__set_optional_string import SetOptionalStringHelper
from dh__set_optional_string import SetOptionalStringProxy
from dh__set_string import SetStringHelper
from dh__set_string import SetStringProxy
from foo_some_other_record import FooSomeOtherRecord
from foo_some_other_record_helper import FooSomeOtherRecordHelper
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class FooContainersRecord:
    c_data_set = MultiSet()

    @staticmethod
    def check_c_data_set_empty():
        assert len(FooContainersRecord.c_data_set) == 0
        ListInt32THelper.check_c_data_set_empty()
        ListBinaryHelper.check_c_data_set_empty()
        ListOptionalBinaryHelper.check_c_data_set_empty()
        ListListStringHelper.check_c_data_set_empty()
        ListRecordFooSomeOtherRecordHelper.check_c_data_set_empty()
        MapStringInt32THelper.check_c_data_set_empty()
        MapStringStringHelper.check_c_data_set_empty()
        MapOptionalStringOptionalStringHelper.check_c_data_set_empty()
        MapInt8TListDateHelper.check_c_data_set_empty()
        SetStringHelper.check_c_data_set_empty()
        SetOptionalStringHelper.check_c_data_set_empty()
        MapInt8TSetStringHelper.check_c_data_set_empty()
        MapBoxedInt32TSetStringHelper.check_c_data_set_empty()


    def __init__(self, optional_list_int, list_int, list_binary, list_optional_binary, list_list_string, list_record, optional_map_string_int, map_string_int, map_string_string, map_optional_string_optional_string, map_int_list_date, optional_set_string, set_string, set_optional_string, map_int_set_string, map_optional_int_set_string):
        self.optional_list_int = optional_list_int
        self.list_int = list_int
        self.list_binary = list_binary
        self.list_optional_binary = list_optional_binary
        self.list_list_string = list_list_string
        self.list_record = list_record
        self.optional_map_string_int = optional_map_string_int
        self.map_string_int = map_string_int
        self.map_string_string = map_string_string
        self.map_optional_string_optional_string = map_optional_string_optional_string
        self.map_int_list_date = map_int_list_date
        self.optional_set_string = optional_set_string
        self.set_string = set_string
        self.set_optional_string = set_optional_string
        self.map_int_set_string = map_int_set_string
        self.map_optional_int_set_string = map_optional_int_set_string
