from serializers import packer
from serializers.serializer import Serializer


class JSONSerializer(Serializer):

    def to_str(self, obj):
        if isinstance(obj, dict):
            strings = list()
            for key, value in obj.items():
                strings.append(f'{self.to_str(key)}:{self.to_str(value)},')
            return f"{{{''.join(strings)[:-1]}}}"
        elif isinstance(obj, str):
            s = obj.translate(str.maketrans({
                "\"": r"\"",
                "\\": r"\\",
            }))
            return f"\"{s}\""
        elif obj is None:
            return 'null'
        else:
            return str(obj)

    def dumps(self, obj):
        return self.to_str(packer.pack(obj))

    def loads(self, string):
        null = None
        return packer.unpack(eval(string))
