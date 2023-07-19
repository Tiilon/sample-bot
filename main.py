from fastapi import FastAPI
from testing import *
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from training import Training


class Bot(BaseModel):
    sentence: str

app = FastAPI()

import os

filename = "./training_data"

if os.path.isfile(filename):
    pass
else:
    train = Training()
    train.build()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/bot-response')
async def get_response(bot: Bot):
    bot_response = Testing()
    response = bot_response.response(bot.sentence)
    return {'message': response}


# if __name__ == '__main__':
#     uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

# write a function print hello world

# uvicorn main:app --host 0.0.0.0 --port 8000