# import uuid
#
#
# def convert_uuid():
#     uuid_obj = uuid.uuid4()
#     print("UUID:", uuid_obj)
#     bytes_array = uuid_obj.bytes
#     result = []
#     for byte in bytes_array:
#         result.append(hex(byte))
#     return " ".join(result)
#
#
# print(convert_uuid())
import uuid

print(uuid.uuid4())