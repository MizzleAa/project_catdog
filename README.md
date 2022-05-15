# :cat: :dog: PROJECT_CATDOG_PREDICT

## Information

```
MMDetection 의 마스크 모델 샘플본을 사용하여 back-end 및 front-end 를 구현
```
---
## AI

### Tech/AI Used

- MMDetection 2.10.0

### Setting

1. *.py Download
    ```
    https://github.com/open-mmlab/mmdetection/tree/master/configs/cascade_rcnn 
    ```

2. *.pth Download
    - *.py와 동일한 모델의 pth 파일을 다운로드 수행
    ```
    https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
    ```

3. checkpoints 저장
    - pth 파일을 backend/catdog/ai/checkpoints 하위에 저장

### MMDetection 참고자료
    - https://mmdetection.readthedocs.io/en/latest/api.html  
---

## Back-end
### Tech/Framework Used

- Python 3.7.4

**built with**

- VSCODE

### Setting

1. _VSCODE_ 에서 `PROJECT_CATDOG_PREDICT` 프로젝트 폴더 열고 `Terminal - New Terminal` 메뉴로 터미널 접속

   - `{workspace}\PROJECT_CATDOG_PREDICT` 프로젝트 폴더 생성 후 진행

2. python 가상환경 생성

   - 생성 경로는 AIDM 프로젝트 폴더 내에 생성

   - `python -m venv {venv_name}`

3. python 가상환경 실행

   - `{venv_name}\Scripts\activate`
   - `python -m pip install --upgrade pip`  


4. python 라이브러리 설치

   - 인공지능 라이브러리
       - `pip install torch==1.8.1+cu102 torchvision==0.9.1+cu102 torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html`
       - `pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu102/torch1.8.0/index.html`
       - `pip install mmdet==2.14.0`
   - Django 라이브러리
       - `pip install django==3.2.2`
       - `pip install django-allauth==0.44.0`



    ### requirement.txt

    ```
    asgiref==3.5.1
    certifi==2021.10.8
    cffi==1.15.0
    charset-normalizer==2.0.12
    cryptography==37.0.2
    cycler==0.11.0
    Cython==0.29.28
    defusedxml==0.7.1
    Django==3.2.2
    django-allauth==0.44.0
    django-cors-headers==3.7.0
    django-rest-auth==0.9.5
    django-sslserver==0.22
    djangorestframework==3.13.1
    djangorestframework-simplejwt==4.6.0
    fonttools==4.33.3
    idna==3.3
    kiwisolver==1.4.2
    matplotlib==3.5.2
    mmdet==2.14.0
    numpy==1.21.6
    oauthlib==3.2.0
    packaging==21.3
    Pillow==9.1.0
    pycocotools-windows==2.0.0.2
    pycparser==2.21
    PyJWT==2.4.0
    pyparsing==3.0.9
    python-dateutil==2.8.2
    python3-openid==3.2.0
    pytz==2022.1
    requests==2.27.1
    requests-oauthlib==1.3.1
    six==1.16.0
    sqlparse==0.4.2
    terminaltables==3.1.10
    torch==1.8.1+cu102
    torchaudio==0.8.1
    torchvision==0.9.1+cu102
    typing_extensions==4.2.0
    urllib3==1.26.9
    ```

5. 실행 방법
- console 접속
    ```bash
    ${classPath}/venv/Script/activate

    cd backend

    py manage.py runserver
    ```


---
## Front-end

### Tech/Framework Used

- React 17.0.2

**built with**

- VSCODE

### Setting

1. package 설치
    ```bash
    npm install
    ```

2. 실행 방법
    ```bash
    npm start
    ```

---
## Made

© [mizzleaa](https://github.com/mizzleaa)