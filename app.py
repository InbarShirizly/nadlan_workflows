import httpx
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request

app = FastAPI()
limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
timeout = httpx.Timeout(timeout=5.0, read=15.0)
client = httpx.AsyncClient(limits=limits, timeout=timeout)

@app.get("/", response_class=JSONResponse)
async def index(request: Request):
    return JSONResponse(content={"message": "Starter API with FastAPI"})


@app.get("/sum_numbers", response_class=JSONResponse)
async def sum_numbers(request: Request, a: int, b: int):
    return JSONResponse(content={"result": a + b}, headers={"X-Custom-Header": "sum_numbers"})


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        #log_config=str(ROOT_DIR / "server/log_conf.yaml"),
        use_colors=True,
        access_log=True,
    )
