import os
import sys
import importlib.util
import argparse
import asyncio
from xoxxox.params import Engine

#---------------------------------------------------------------------------

def getprc(engine):
  s = importlib.util.spec_from_file_location("module", f"{Engine.dirprc}/{engine}.py")
  module = importlib.util.module_from_spec(s)
  s.loader.exec_module(module)
  return module

def infere(prompt, promng):
  if gensyn == "1":
    datimg = imgprc.infere(prompt, promng)
  else:
    datimg = asyncio.run(imgprc.infere(prompt, promng))
  return datimg

#---------------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("--engine", default="dll")
parser.add_argument("--gensyn", default="1")
parser.add_argument("--prompt", default="")
parser.add_argument("--promng", default="")
objarg = parser.parse_args()
dicprm = {k: v for k, v in vars(objarg).items() if v is not None}

dicprm.pop("engine")
dicprm.pop("gensyn")
engine = objarg.engine
gensyn = objarg.gensyn
prompt = objarg.prompt
promng = objarg.promng

#---------------------------------------------------------------------------

module = getprc(engine)
imgprc = module.ImgPrc(**dicprm)
imgprc.status(**dicprm)
sys.stdout.buffer.write(infere(prompt, promng))
