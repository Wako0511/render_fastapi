from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>和光大地のホームページ</title>
        </head>
        <body>
            <h1>ようこそ！</h1>
            <p>FastAPIで作成したホームページです。</p>
            <h2>自己紹介</h2>
            <p>大学生です。</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/teacher")
async def teacher(student):
    return {"message": f"{student}さん、今日もよく頑張りました！"}
