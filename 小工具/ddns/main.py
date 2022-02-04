# coding:utf-8
import sys
import re
import os
import requests
import logging
import settings
import logging.config 

# 全局初始化
FORMAT = "json"
LOGIN_TOKEN="285374,91636ddb207542c94aa0e6366b30ae05"
logging.config.dictConfig(settings.LOGGING_DIC)
logger = logging.getLogger("second_logger")

# 域名信息
def domain_info(domain):
    url = "https://dnsapi.cn/Domain.Info"
    data = {
        "login_token": LOGIN_TOKEN,
        "format": FORMAT,
        "domain": domain
    }
    r = requests.post(url, data=data, timeout=5)
    return r.json()["domain"]

# 域名id
def domain_id(domain):
    info = domain_info(domain)
    return info["id"]

# 域名记录信息
def record_info(domain, sub_domain):
    url = "https://dnsapi.cn/Record.List"
    data = {
        "login_token": LOGIN_TOKEN,
        "format": FORMAT,
        "domain": domain,
        "sub_domain": sub_domain
    }
    r = requests.post(url, data=data, timeout=5)
    return r.json()["records"][0]


def record_data(domain, sub_domain):
    info = record_info(domain, sub_domain)
    return info["id"], info["line"], info["value"]

def get_newip():
    response = requests.get("http://txt.go.sohu.com/ip/soip")
    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",response.content.decode(errors='ignore')).group(0)
    return ip

# 更新域名主函数
def record_update(domain, sub_domain):
    newip = get_newip()
    rid, line, oldip = record_data(domain, sub_domain)
    if newip == oldip:
        logger.info(f"ip没有发生改变,仍为{oldip}")
        return None

    url = "https://dnsapi.cn/Record.Ddns"
    data = {
        "login_token": LOGIN_TOKEN,
        "format": FORMAT,
        "domain_id": domain_id(domain),
        "record_id": rid,
        "sub_domain": sub_domain,
        "record_line": line,
        "value": newip,
    }
    try:
        r = requests.post(url, data=data, timeout=5)
        print(r.json())
        res_message = r.json()["status"]["message"]
        res_ip = r.json()["record"]["value"]
        logger.info(f"{res_message},ip修改为{res_ip}")
    except Exception as e:
        logger.error("有错误",exc_info=True)

if __name__ == "__main__":
    record_update("adamli.top","home")
    record_update("adamli.top","@")
