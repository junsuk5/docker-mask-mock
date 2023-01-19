from typing import Union

from fastapi import FastAPI

from mock_data import data
from if_kakao_data import if_kakao_data

app = FastAPI(
    title="Mock 데이터 문서",
)


@app.get("/")
async def root():
    return {"message": "생존코딩 오준석"}


#
#
# @app.get("/my")
# async def my():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

@app.get("/ifKakao")
async def get_if_kakao_datas():
    return if_kakao_data


@app.get("/mask")
async def get_mask_infos(page: Union[int, None] = None, limit: Union[int, None] = None):
    try:
        if page is None and limit is None:
            return data
        elif page is not None and limit is not None:
            stores = data["stores"]
            result = list(chunks(stores, limit))

            return {
                "count": len(result[page]),
                "stores": result[page]
            }

    except IndexError:
        return {
            "count": 0,
            "stores": []
        }

    return {
        "error": "잘못 된 접근"
    }


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
