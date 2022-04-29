# import sys
# sys.path.append("D:\\Alexander\\Work\\ISP-2022-053505-main\\Task 2")
import os
import math
from serializers import json_serializer as json
from tests import diff_entities

def test_ds_ls_fun():
    ser = json.JSONSerializer()
    fun = ser.loads(ser.dumps(diff_entities.f))
    assert isinstance(fun(0), float)


def test_d_l_fun():
    ser = json.JSONSerializer()
    file = open("test.json", "w")

    ser.dump(diff_entities.f, file.name)
    fun = ser.load(file.name)

    file.close()
    os.remove(os.path.abspath(file.name))

    assert math.sin(42 * 123 * 0) == fun(0)

def test_ds_ls_obj():
    ser = json.JSONSerializer()
    obj = ser.loads(ser.dumps(diff_entities.milkshake))
    assert str(type(obj)) == str(type(diff_entities.milkshake))

def test_d_l_obj():
    ser = json.JSONSerializer()
    file = open("test.json", "w")

    ser.dump(diff_entities.milkshake, file.name)
    obj = ser.load(file.name)

    file.close()
    os.remove(os.path.abspath(file.name))

    equality = (obj.flavor == diff_entities.milkshake.flavor)
    equality = equality and (obj.volume == diff_entities.milkshake.volume)
    assert equality