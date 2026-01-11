from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/receive")
async def receive_message(
    type: str = Form(...),
    content: str = Form(...),
    source: str = Form(...),
    isMentioned: str = Form(...),
    isMsgFromSelf: str = Form(...),
):
    # 处理请求数据
    response_data = {
        "type": type,
        "content": content,
        "source": source,
        "isMentioned": isMentioned,
        "isMsgFromSelf": isMsgFromSelf,
    }
    try:
        # 填写处理逻辑-开始
        print(response_data)
        # 填写处理逻辑-结束
        return JSONResponse(content={"status": "success", "data": response_data})
    except Exception as e:
        print(e)
        return JSONResponse(content={"status": "error", "data": "处理失败"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1217)