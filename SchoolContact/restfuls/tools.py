# coding: utf-8

def parse_request(request_dict, args):
    """返回一个字典"""
    return_dict = {}
    for arg in args:
        return_dict[arg] = request_dict.get(arg)
    return return_dict