from serializers import serializer
from serializers import json_serializer
from serializers import yaml_serializer
from serializers import toml_serializer


class SerializerCreator:

    def create_serializer(self) -> serializer.Serializer:
        pass


class JSONSerializerCreator(SerializerCreator):

    def create_serializer(self) -> serializer.Serializer:
        return json_serializer.JSONSerializer()


class YAMLSerializerCreator(SerializerCreator):

    def create_serializer(self) -> serializer.Serializer:
        return yaml_serializer.YAMLSerializer()


class TOMLSerializerCreator(SerializerCreator):

    def create_serializer(self) -> serializer.Serializer:
        return toml_serializer.TOMLSerializer()
