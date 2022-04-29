import toml
from serializers import packer
from serializers.serializer import Serializer


class TOMLSerializer(Serializer):

    def dumps(self, obj):
        return toml.dumps(packer.pack(obj))

    def loads(self, string):
        return packer.unpack(toml.loads(string))
