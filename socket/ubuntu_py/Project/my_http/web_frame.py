def application(env_dict, start_fun):
    """
    start_fun:请求处理接口
    env_dict:请求体
    """
    start_fun("200 OK", [("Content-Type", "text/html;charset=utf-8"),("APIVERSION","NONE")])
    data = f"Hello {env_dict}"
    return data