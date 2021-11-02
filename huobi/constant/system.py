
HUOBI_URL_PRO = "https://api.huobi.sg"
HUOBI_URL_VN = "https://api.huobi.sg"
HUOBI_URL_SO = "https://api.huobi.sg"


HUOBI_WEBSOCKET_URI_PRO = "wss://api.huobi.sg"
HUOBI_WEBSOCKET_URI_VN = "wss://api.huobi.sg"
HUOBI_WEBSOCKET_URI_SO = "wss://api.huobi.sg"

class WebSocketDefine:
    Uri = HUOBI_WEBSOCKET_URI_PRO

class RestApiDefine:
    Url = HUOBI_URL_PRO

class HttpMethod:
    GET = "GET"
    GET_SIGN = "GET_SIGN"
    POST = "POST"
    POST_SIGN = "POST_SIGN"


class ApiVersion:
    VERSION_V1 = "v1"
    VERSION_V2 = "v2"

def get_default_server_url(user_configed_url):
    if user_configed_url and len(user_configed_url):
        return user_configed_url
    else:
        return RestApiDefine.Url
