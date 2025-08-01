from ....utils.logger import logger
from .base import PlatformHandler, StreamData
from .handlers import (
    AcfunHandler,
    BaiduHandler,
    BigoHandler,
    BilibiliHandler,
    BluedHandler,
    ChangliaoHandler,
    ChzzkHandler,
    CustomHandler,
    DouyinHandler,
    DouyuHandler,
    FaceitHandler,
    FlexTVHandler,
    HaixiuHandler,
    HuajiaoHandler,
    HuamaoHandler,
    HuyaHandler,
    InkeHandler,
    JDHandler,
    KuaishouHandler,
    KugouHandler,
    LaixiuHandler,
    LangLiveHandler,
    LehaiHandler,
    LianJieHandler,
    LivemeHandler,
    LookHandler,
    MaoerFMHandler,
    MiguHandler,
    NeteaseHandler,
    PamdaTVHandler,
    PiaopiaoHandler,
    PicartoHandler,
    PopkonTVHandler,
    QiandureboHandler,
    RedNoteHandler,
    ShopeeHandler,
    ShowRoomHandlerHandler,
    SixRoomHandler,
    SoopHandler,
    TaobaoHandler,
    TikTokHandler,
    TwitcastingHandler,
    TwitchHandler,
    VVXQHandler,
    WeiboHandler,
    WinkTVHandler,
    YinboHandler,
    YiqiLiveHandler,
    YoutubeHandler,
    YYHandler,
    ZhihuHandler,
)


def get_platform_handler(
    live_url: str,
    proxy: str | None = None,
    cookies: dict | str | None = None,
    record_quality: str = "default",
    platform: str | None = None,
    username: str | None = None,
    password: str | None = None,
    account_type: str | None = None,
) -> PlatformHandler | None:
    handler_instance = PlatformHandler.get_handler_instance(
        live_url, proxy, cookies, record_quality, platform, username, password, account_type
    )
    if handler_instance:
        return handler_instance
    logger.warning(f"Unknown live platform：{live_url}")
    return None


def get_platform_info(record_url: str) -> tuple:
    platform_map = {
        "douyin.com/": ("抖音直播", "douyin"),
        "https://www.tiktok.com/": ("TikTok直播", "tiktok"),
        "https://live.kuaishou.com/": ("快手直播", "kuaishou"),
        "https://www.huya.com/": ("虎牙直播", "huya"),
        "https://www.douyu.com/": ("斗鱼直播", "douyu"),
        "https://www.yy.com/": ("YY直播", "yy"),
        "https://live.bilibili.com/": ("B站直播", "bilibili"),
        "https://www.xiaohongshu.com/": ("小红书直播", "xiaohongshu"),
        "xhslink.com/": ("小红书直播", "xhs"),
        "https://www.bigo.tv/": ("Bigo直播", "bigo"),
        "https://app.blued.cn/": ("Blued直播", "blued"),
        "sooplive.co.kr/": ("SOOP", "soop"),
        "cc.163.com/": ("网易CC直播", "netease"),
        "qiandurebo.com/": ("千度热播", "qiandurebo"),
        "pandalive.co.kr/": ("PandaTV", "pandalive"),
        "fm.missevan.com/": ("猫耳FM直播", "maoerfm"),
        "winktv.co.kr/": ("WinkTV", "winktv"),
        "flextv.co.kr/": ("FlexTV", "flextv"),
        "look.163.com/": ("Look直播", "look"),
        "popkontv.com/": ("PopkonTV", "popkontv"),
        "twitcasting.tv/": ("TwitCasting", "twitcasting"),
        "live.baidu.com/": ("百度直播", "baidu"),
        "weibo.com/": ("微博直播", "weibo"),
        "kugou.com/": ("酷狗直播", "kugou"),
        "twitch.tv/": ("TwitchTV", "twitch"),
        "liveme.com/": ("LiveMe", "liveme"),
        "huajiao.com/": ("花椒直播", "huajiao"),
        "7u66.com/": ("流星直播", "liuxing"),
        "showroom-live.com/": ("ShowRoom", "showroom"),
        "live.acfun.cn/": ("Acfun", "acfun"),
        "tlclw.com/": ("畅聊直播", "changliao"),
        "ybw1666.com/": ("音播直播", "yingbo"),
        "inke.cn/": ("映客直播", "inke"),
        "zhihu.com/": ("知乎直播", "zhihu"),
        "chzzk.naver.com/": ("CHZZK", "chzzk"),
        "haixiutv.com/": ("嗨秀直播", "haixiu"),
        "vvxqiu.com/": ("VV星球", "vvxq"),
        "17.live/": ("17Live", "17live"),
        "lang.live/": ("浪Live", "lang"),
        "m.pp.weimipopo.com/": ("漂漂直播", "piaopiao"),
        ".6.cn/": ("六间房直播", "6room"),
        "lehaitv.com/": ("乐嗨直播", "lehai"),
        "h.catshow168.com/": ("花猫直播", "catshow"),
        "live.shopee": ("shopee", "shopee"),
        ".shp.": ("shopee", "shopee"),
        "youtube.com/": ("Youtube", "youtube"),
        "tb.cn": ("淘宝直播", "taobao"),
        "3.cn": ("京东直播", "jd"),
        "faceit.com": ("faceit", "faceit"),
        "lailianjie.com": ("连接直播", "lianjie"),
        "miguvideo.com": ("咪咕直播", "migu"),
        "imkktv.com": ("来秀直播", "laixiu"),
        "picarto.tv": ("Picarto", "picarto"),
        ".m3u8": ("自定义录制直播", "custom"),
        ".flv": ("自定义录制直播", "custom"),
    }

    for key, value in platform_map.items():
        if key in record_url:
            return value[0], value[1]

    return None, None


__all__ = [
    "AcfunHandler",
    "BaiduHandler",
    "BigoHandler",
    "BilibiliHandler",
    "BluedHandler",
    "ChangliaoHandler",
    "ChzzkHandler",
    "CustomHandler",
    "DouyinHandler",
    "DouyuHandler",
    "FaceitHandler",
    "FlexTVHandler",
    "HaixiuHandler",
    "HuajiaoHandler",
    "HuamaoHandler",
    "HuyaHandler",
    "InkeHandler",
    "JDHandler",
    "KuaishouHandler",
    "KugouHandler",
    "LaixiuHandler",
    "LangLiveHandler",
    "LehaiHandler",
    "LianJieHandler",
    "LivemeHandler",
    "LookHandler",
    "MaoerFMHandler",
    "MiguHandler",
    "NeteaseHandler",
    "PamdaTVHandler",
    "PiaopiaoHandler",
    "PicartoHandler",
    "PlatformHandler",
    "PopkonTVHandler",
    "QiandureboHandler",
    "RedNoteHandler",
    "ShopeeHandler",
    "ShowRoomHandlerHandler",
    "SixRoomHandler",
    "SoopHandler",
    "StreamData",
    "TaobaoHandler",
    "TikTokHandler",
    "TwitcastingHandler",
    "TwitchHandler",
    "VVXQHandler",
    "WeiboHandler",
    "WinkTVHandler",
    "YYHandler",
    "YinboHandler",
    "YiqiLiveHandler",
    "YoutubeHandler",
    "ZhihuHandler",
    "get_platform_handler",
    "get_platform_info",
]
