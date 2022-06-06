import yaml
from serializers import packer
from serializers.serializer import Serializer


class YAMLSerializer(Serializer):

    def dumps(self, obj):
        return yaml.dump(packer.pack(obj))

    def loads(self, string):
        return packer.unpack(yaml.safe_load(string))
