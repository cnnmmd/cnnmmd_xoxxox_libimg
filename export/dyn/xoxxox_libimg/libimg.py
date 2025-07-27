#---------------------------------------------------------------------------
# 参照

import aiohttp
from xoxxox.libmid import LibMid

#---------------------------------------------------------------------------
# 処理：画像生成

class PrcImg:

  # 変数
  oldcfg = ""

  # 画像生成
  @staticmethod
  async def cnnimg(datorg, datneg, server, config):

    if config != PrcImg.oldcfg:
      async with aiohttp.ClientSession() as sssweb:
        async with sssweb.post(server + "/sys", json={"config": config}) as datres:
          dicres = await datres.json()
      PrcImg.oldcfg = config

    async with aiohttp.ClientSession() as sssweb:
      async with sssweb.post(server + "/gen", json={"prompt": datorg.decode("utf-8"), "promng": datneg.decode("utf-8")}) as datres:
        rawres = await datres.read()
    return rawres

LibMid.dicprc.append({"key": "xoxxox.PrcImg.cnnimg", "frm": "LibMid.plugin['xoxxox_libimg'].PrcImg.cnnimg(values[dicreq['keydat']], values[dicreq['keyneg']], dicreq['server'], dicreq['config'])", "syn": False})
