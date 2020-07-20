# Hyperledger Indy

## 01. Basic Concept

### 기존의 Identity

- 속성 : 이름, 나이, 성별 등의 정보
- ID 제시할 때 일부 내용만 보여줄 수 없다.
- 한국의 운전면허증이 미국에서는 사용이 불가
- 복잡한 공증의 문제도 있음
- ID 인증 4가지 요소
  - 식별자(Identifier) : ID 사용자 식별
  - 속성(Atrribute) : ID 사용자 특징
  - 인증 수단(Authentication method) : ID 소유권 확인
  - 발행인(Issuer) : ID 발행인

### SSO (Single Sign On, 통합로그인)

- 각 웹사이트마다 진행해야하는 회원가입 문제 해결
- IdP(Identity Provider) 웹사이트의 회원정보를 이용해서 RP(Relying Party) 웹사이트로 회원가입 혹은 로그인할 수 있는 기능
- 구글 계정(IdP)을 이용해서 깃허브(RP) 가입
- 구현 프로토콜
  - OAuth(Open Authorization)
  - SAML(Security Assertion Markup Langauge)
  - JWT(Json Web Token)
- 실제 사용자 정보는 사용자가 아닌 구글이 깃허브에게 전달, 만일 IdP 중 악의적인 IdP가 사용자 개인정보를 무단으로 사용한다면 막을 방법은?

### 대칭키

- 서로 간의 공유된 대칭키가 있어야 복호화 가능
- 그러나 대칭키를 공유하는 과정에서 탈취될 수도 있음
  - SSL/TLS 방식 등장

### 비대칭키

- 비밀키(Private Key), 공개키(Public Key)

### Hash

- sha256 : 어떠한 길이의 메시지를 입력해도 256비트의 결괏값을 반환
- 해시 함수는 누구에게나 공개된 함수이기 때문에 누가 사용하든지 동일한 결과를 받지만 단방향 함수(one-way function)이기 때문에 원본 내용을 알 수가 없음

### SSL/TLS

- 해커가 naver라고 주장하면서 자기의 공개키를 보내면 해커의 공개키와 naver의 공개키를 어떻게 구분할 수 있을까?
- CA(Certificate Authority, 인증기관)라고 부르는 인증 노드를 활용한 SSL/TLS 프로토콜 사용

### SSI (Self-Sovereign Identity, 자기주권 신원증명)

-
