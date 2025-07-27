import sys
import argparse
import asyncio
import aiohttp

#---------------------------------------------------------------------------

async def reqsys(dicreq, adrreq):
  async with aiohttp.ClientSession() as sssweb:
    async with sssweb.post(adrreq, json=dicreq) as datres:
      dicres = await datres.json()
      return dicres

async def reqgen(dicreq, adrreq):
  async with aiohttp.ClientSession() as sssweb:
    async with sssweb.post(adrreq, json=dicreq) as datres:
      datimg = await datres.read()
      return datimg

#---------------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("--server", default="http://localhost")
parser.add_argument("--prompt", default="")
parser.add_argument("--promng", default="")
objarg = parser.parse_args()
dicprm = {k: v for k, v in vars(objarg).items() if v is not None}

dicprm.pop("server")
server = objarg.server

adssys = "/sys"
adsgen = "/gen"

#---------------------------------------------------------------------------

dicres = asyncio.run(reqsys(dicprm, server + adssys))
datimg = asyncio.run(reqgen(dicprm, server + adsgen))
sys.stdout.buffer.write(datimg)
