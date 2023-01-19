# 마스크 재고 앱 Mock Data

http://104.198.248.76:3000/docs

# docker 이미지 빌드 및 업로드 순서
m1 맥에서 x86에서 실행되도록 빌드 --platform 명시
```
docker build -t mask --platform linux/amd64 .  
```

태깅
```shell
docker tag mask junsuk5/mask:latest           
```

업로드
```shell
docker push junsuk5/mask:latest           
```

# GCP 에서 실행 순서
실행중인 docker container 확인
```shell
sudo docker ps -a
```

스톱
```shell
sudo docker stop [id 3자리]
```

컨테이너 삭제
```shell
sudo docker rm [id 3자리]
```

이미지 다시 받기
```shell
sudo docker pull junsuk5/mask
```

GCP 용량 모자르면 도커 다 날림
```shell
sudo docker system prune
```

실행
```shell
sudo docker run -d --name mock-json -p 3000:80 junsuk5/mask 
```


# 로컬 docker 컨테이너 실행

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
