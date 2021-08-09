# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from typing import Dict
app = FastAPI()

data ='{"Web":"http://47.113.205.237/web/","Payload":"http://47.113.205.237/payload/","Playgame":"https://www.tomorrowing.cn/playgames/"}'
app = FastAPI()

@app.get("/end/", response_model=Dict[str, str ])
async def read_keyword_weights():
    return {"Web":"http://47.113.205.237/web/","Payload":"http://47.113.205.237/payload/","Playgame":"https://www.tomorrowing.cn/playgames/"}

import os
@app.get("/")

async def read_keyword_weights():
    name = ''
    file_dir = './api'
    for root, dirs, files in os.walk(file_dir, topdown=False):
        for i in files:
            data=i+','
            name+=data
       

    return name
