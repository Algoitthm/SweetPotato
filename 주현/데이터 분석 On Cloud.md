## 데이터 분석 On Cloud

클라우드 환경에서의 데이터 탐색 및 분석(AWS 환경에서의 데이터 탐색, 기초통계분석, 모델링 방법, DataBricks 활용 방법 등등)



### 1. on AWS

0. Amazon Kinesis 를 활용한 실시간 스트리밍 데이터 수집,처리 및 분석.

   - 서버리스 서비스로 관리할 서버가 존재하지 않음

   - kinesis 에서 제공하는 편집기를 통해 sql 쿼리를 구축 할 수 있음.

   - IDE 를 AWS 에 연결하여 java 라이브러리를 설치가능. 확장 가능한 라이브러리에는 스트리밍 데이터 분석에 필요한 기능들이 들어있음

     <사용사례>

     1. java 어플리케이션을 활용한 iot 스트리밍 ETL

        Java 애플리케이션을 작성하고 Amazon Kinesis Data Analytics를 사용하여 가전 제품, 내장 센서, TV 셋톱박스 등과 같은 IoT 디바이스에서 전송되는 스트리밍 데이터를 변환, 집계 및 필터링할 수 있습니다. 그런 다음, 센서가 특정 운영 임계값을 초과하는 경우 데이터를 사용하여 실시간 알림을 전송할 수 있습니다.

     2. sql 을 통한 실시간 로그 분석

        

1. Amazon SageMaker 를 활용한 머신러닝 모델 생성

   - 개발자 및 데이터 분석가가 머신러닝 모델을 빠르게 구축, 학습 및 배포할 수 있도록 하는 완전 관리형 서비스.
   - 머신 러닝에 사용되는 모든 구성 요소를 단일 도구 세트로 제공하여 반복적인 머신러닝 프로세스를 더 빠르게, 더 적은 노력으로 처리 할 수 있음.



​	**상세 기능**

 - SageMaker Studio

   -> 별도의 어플리케이션 설치 없이 주요 기능(notebook, debugger,autopilot, model monitor)을 사용가능

 - SageMaker Notebooks

   -> 'snapshot' 기능을 통해 본인이 작업한 노트북을 깃텁에 올리거나 공유가능한  URL로 저장 할 수 있음.  다른 사용자는 해당 url을 활용하여 조회하거나 편집 가능함.

- SageMaker Experiment

  1. 머신러닝 모델에 대한 반복학습 구성/축적 가능

     -> 입력 매개 변수, 구성 및 결과를 자동으로 캡쳐하고 이를 experiment로 저장하여 반복을 관리.

     -> sagemaker에서 코드로 작업하거나, 오토파일럿 연동 역시 가능하며 pandas 형태로 결과를 제공함

  2.  studio 리더보드를 통한 experiment의 결과 조회 및 비교 가능, 

     -> studio 내 결과를 제공하며 사용성이 뛰어남

  3. 다중 job(하이퍼파라미터 조정)  시행 가능

     -> 파이썬 코드형태로 사용 가능하여 유연성이 뛰어남.

- SageMaker Debugger  ==MLDL 이나 데이터브릭스에는 없는 기능==

  -> 하이퍼파라미터 튜닝에러를 잡아줌.

  파이썬 코드로 사용하며, 디버거의 통계를 스튜디오에서 시각화하여 쉽게 이해할 수 있도록 해줌. 

  일반적인 훈련 문제가 감지 될 때 경고 및 치료 조언을 생성하며, 모델 설명 방법의 초기 단계를 나타내는 모델 작동 방식을 해석 할 수 있음

- SageMaker Autopilot

  -> 오토머신러닝 기능 제공(파이썬 코드로 사용 및 옵션설정)

  -> 전체 머신러닝 진행과정 및 결과를 파이썬 코드로 별도 제공하여 재사용성이 뛰어남.

  -> 결과 보고서가 ipynb 파일로 자동 생성, 익숙한 노트북의 형태로 제공되어 친숙함.

- SageMaker Model Monitor ==MLDL 이나 데이터브릭스에는 없는 기능==

  -> 기존 모델의 학습에 사용되는 프레임에 맞도록 contraint 를 지속적으로 체크하며, 모델 흐름 모니터링을 진행함(데이터 변화에 따른 concept drift 감지 등등)

  

### 2. On Databricks

통합 데이터 분석 환경을 제공함.

0.  Data Science Workspace

   - Collaborative Notebooks 기능

     -> 파이썬, R, SQL, Scala 문법을 제공하는 노트북 사용가능. 노트북을 통해 작업물을 공유 할 수 있으며  다른 사용자의 결과 조회 및 편집도 가능함.

     -> 잡 스케쥴러 기능(특정시간에 특정작업 시행), 대쉬보드 기능(sparked-dashboards를 통해 인사이트 공유), 로그 관리 및 감독 기능 제공

     -> 데이터브릭스 내부에서 Tableau, Looker, PowerBI, Rstudio, SnowFlake 와 같은 툴을 연결하여 사용할 수 있음.

   - MLR(Machine Learning Runtime) 기능 

     -> 콘다 통합환경에 설치되어 있는 패키지들이 모두 설치되어 있음.

     -> tensorflow, keras, pytorch 등등 머신러닝에 필요한 다양한 패키지들이 설치되어 있음.

   - Augmented 머신러닝 기능 제공 / 모델 관리(Managed ML Flow)

     -> 수백, 수천개의 experiment 들에 대한 트랙킹과 비교분석이 가능해짐

     -> 하나의 experiment 에 대해 모델 학습 과정(입력 매개 변수,구성, 결과 등등...)을 기록하여 관리 가능

     -> 최적의 모델탐색 기능 제공(automated model search), 하이퍼파라미터 자동튜닝 기능 제공

     

1. Unified Data Service

   - databricks delta를 활용하여 저장공간 최적화, 데이터 업데이팅, 쿼리문 실행 등 데이터 전처리에 필요한 기능들을 손쉽게 사용할 수 있음.
   - databricks delta는 아파치 스파크와 100% 연동





