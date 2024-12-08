from eb_fast_api.database.sources.crud.user_crud import UserCRUD
from eb_fast_api.domain.schema.sources.login_info import LoginInfo
from eb_fast_api.snippets.sources import pwdcrypt
from eb_fast_api.domain.schema.sources.schemas import TokenInfo
from eb_fast_api.service.jwt.sources.jwt_service import JWTService


def check_password(
    user_crud: UserCRUD,
    login_info: LoginInfo,
) -> dict:
    user = user_crud.read(email=login_info.email)
    if not user:
        raise Exception("유저정보가 없습니다.")

    if not pwdcrypt.check(
        password=login_info.password,
        hashedPassword=user["hashedPassword"],
    ):
        raise Exception("잘못된 패스워드 입니다.")

    return user


def create_auth_token(
    user: dict,
    jwtService: JWTService,
) -> TokenInfo:
    email = user["email"]
    accessToken = jwtService.createAccessToken(email)
    refreshToken = jwtService.createRefreshToken(email)

    return TokenInfo(
        accessToken=accessToken,
        refreshToken=refreshToken,
    )


def update_tokens(
    user_crud: UserCRUD,
    token_info: TokenInfo,
    login_info: LoginInfo,
):
    user_crud.update(
        key_email=login_info.email,
        refreshToken=token_info.refreshToken,
        fcm_token=login_info.fcm_token,
    )
    user_crud.commit()
