# 마스크 재고 앱 Mock Data

# docker 이미지 빌드
m1 맥에서 x86에서 실행되도록 빌드 --platform 명시
```
docker build -t --platform linux/amd64 mask .  
```

# docker 컨테이너 실행

```
docker run -d --name mask -p 8080:80 mask
```

## docs

http://localhost:8080/docs

## 실행 예

- http://localhost:8080/mask
- http://localhost:8080/mask?page=0&limit=20

## 로컬 실행
```shell
uvicorn main:app --reload
```

## 서버 실행
```shell
uvicorn main:app --host 0.0.0.0 --port 80
```

## Docker
```shell
docker tag mask junsuk5/mask:latest

docker push junsuk5/mask:latest
```

## 서버
docker ps 확인
```shell
sudo docker ps -a
```

stop 
```shell
sudo docker stop [아이디 앞 3자리]
```

## cgp에서 실행

### docker 이미지 컨테이너 캐시 다 날림
```shell
sudo docker system prune
```

```shell
sudo docker run -d --name mock-json -p 3000:80 junsuk5/mask
```
