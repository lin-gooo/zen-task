from fastapi import APIRouter, Body, Request

from tools.common import get_logger


router = APIRouter()
logger = get_logger()


@router.post("/login/pwd", summary="密码登录")
async def pwd_login(
    request: Request,
    phone: str = Body(),
    password: str = Body(),
    source: int = Body(UserSource.EDUCATE.value),
):
    await services.check_password(phone, source, password)
    data = await services.login(phone, source=source)
    return ok(data)
