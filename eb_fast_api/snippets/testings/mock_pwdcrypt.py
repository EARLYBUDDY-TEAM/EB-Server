from unittest.mock import patch


def patch_pwdcrypt_check_FAIL():
    def mock_def_pwdcrypt_check_FAIL(
        password: str,
        hashedPassword: str,
    ) -> bool:
        return False

    patcher = patch(
        "eb_fast_api.snippets.sources.pwdcrypt.check",
        new=mock_def_pwdcrypt_check_FAIL,
    )

    return patcher


def patch_pwdcrypt_check_SUCCESS():
    def mock_def_pwdcrypt_check_SUCCESS(
        password: str,
        hashedPassword: str,
    ) -> bool:
        return True

    patcher = patch(
        "eb_fast_api.snippets.sources.pwdcrypt.check",
        new=mock_def_pwdcrypt_check_SUCCESS,
    )

    return patcher
