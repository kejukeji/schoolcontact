# coding: UTF-8
import jsonpickle


pickler = jsonpickle.pickler.Pickler(unpicklable=False, max_depth=2)
EARTH_RADIUS=6371           # 地球平均半径，6371km

def flatten(model):
    """去除pickler.flatten里面的一个字段"""
    json = pickler.flatten(model)
    json.pop('_sa_instance_state', None)
    return json