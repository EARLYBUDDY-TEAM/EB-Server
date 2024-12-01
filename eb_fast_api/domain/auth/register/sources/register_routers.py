from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.auth.register.sources import register_feature
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schema.sources.schemas import RegisterInfo


router = APIRouter(prefix="/auth/register")


@router.post("")
def register(
    registerInfo: RegisterInfo,
    userCRUD=Depends(EBDataBase.user.getCRUD),
):
    if not register_feature.isValidRegisterInfo(registerInfo):
        raise HTTPException(
            status_code=400,
            detail="유저 정보가 올바르지 않습니다.",
        )

    try:
        register_feature.createUser(
            registerInfo=registerInfo,
            userCRUD=userCRUD,
        )
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )
