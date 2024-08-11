from abc import ABC, abstractmethod

class ABSJWTEncoder(ABC):
    """
    JWT 인코더 추상클래스
    encode 메소드를 구현
 
    :param data: JWT에 담을 데이터
    :param expires_delta: JWT 만료 시간
    :param secret_key: JWT 암호화 키
    :param algorithm: JWT 암호화 알고리즘
    """
 
    @abstractmethod
    def encode(
        self, data: dict, expireDelta: int, secretKey: str, algorithm: str
    ) -> str:
        pass


class ABSJWTDecoder(ABC):
    """
    JWT 디코더 추상클래스
    decode 메소드를 구현
 
    :param token: JWT 토큰
    :param secret_key: JWT 암호화 키
    :param algorithm: JWT 암호화 알고리즘
    """
 
    @abstractmethod
    def decode(self, token: str, secretKey: str, algorithm: str) -> dict | None:
        pass