# Git Flow

## 기본원칙

- master branch는 반드시 배포 가능한 상태여야 함
- feature branch는 각 기능의 의도를 알 수 있도록 작성
- commit message는 **매우** 중요하며, 명확하게 작성
- pull request를 통해 협업 진행
- 변경 사항을 반영하고 싶다면 master branch에 병합



## Branch 종류

- main
  - **master** : **배포 가능한 상태**의 코드
  - **develop** : 버그 수정 등 개발 진행
- supporting
  - **feature branches** : 기능 별로 개발 진행, 기능이 반영되거나 드랍되면 삭제
  - **release branches** : 개발 완료 이후 QA/Test 등을 통해 얻어진 다음 배포 전 마이너 버그 픽스 등 반영
  - **hotfixes** : 현재 버전에 긴급하게 반영해야 하는 버그 픽스





## Branch 명령어

- ```
  (master) $ git branch 'branch name'
  # 브랜치 생성
  ```

- ```
  (master) $ git checkout 'branch name'
  # 브랜치 이동
  ```

- ```
  (master) $ git checkout -b 'branch name'
  # 브랜치 생성 및 이동
  ```

- ```
  (master) $ git branch
  # 브랜치 목록
  ```

- ```
  (master) $ git branch -d '브랜치이름'
  # 브랜치 삭제
  ```

- ```
  (master) $ git merge '브랜치이름'
  # {branch name} 브랜치를 master 브랜치에 병합
  # 충돌이 발생하여 자동으로 병합되지 않으면 직접 수정하고 다시 add, commit을 해야 함
  ```





## Branch Merge

### Fast-forward

기존 master 브랜치에 변경사항이 없어 단순한 앞으로의 이동

1. feature/home branch 생성 및 이동

   ```bash
   $ git checkout -b 'feature'
   ```

   

2. 작업 완료 후 commit

   ```bash
   (feature/home) $ touch home.txt
   (feature/home) $ git add .
   (feature/home) $ git commit -m 'Add home.txt'
   ```


3. master 이동

   ```bash
   $ git checkout 'master'
   ```

   


4. master에 병합

   ```bash
   $ git merge 'feature'
   ```

   


5. 결과 : fast-foward

   

6. branch 삭제

   ```bash
   $ git branch -d 'feature'
   ```

   



### Merge commit 

기존 마스터 브랜치에 변경사항이 있어 병합 커밋 발생 (중복되는 파일 X)

1. feature/about branch 생성 및 이동

   ```bash
   git checkout -b 'feature/about'
   ```

   

2. 작업 완료 후 commit

   ```bash
   (feature/about) $ touch about.txt
   (feature/about) $ git add .
   (feature/about) $ git commit -m 'Add about.txt'
   ```

   

3. master 이동

   ```bash
   $ git checkout master
   ```

   

4. *master에 추가 commit 이 발생시키기!!*

   * **다른 파일을 수정 혹은 생성하세요!**

   ```bash
   (master) $ touch master.txt
   (master) $ git add .
   (master) $ git commit -m 'Add master.txt'
   ```

   

5. master에 병합

   ```bash
   $ git merge 'feature/about'
   ```

   

6. 결과 -> 자동으로 *merge commit 발생*

   * vim 편집기 화면이 나타납니다. 

     * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
       * `w` : write
       * `q` : quit

     

7. 커밋 및 그래프 확인하기

   ```bash
   $ git log --onelie --graph
   ```

8. branch 삭제

   ```bash
   $ git branch -d 'feature'
   ```

   

### Merge commit (충돌)

기존 마스터 브랜치에 변경사항이 있는데 수정된 파일이 중복된다

1. feature/test branch 생성 및 이동

   ```bash
   $ git checkout -b 'feature/test'
   ```

   

2. 작업 완료 후 commit

   ```bash
   # README.md 파일 열어서 수정
   (feature/test) $ touch test.txt
   (feature/test) $ git add .
   (feature/test) $ git commit -m 'Add test.txt'
   ```


3. master 이동

   ```bash
   $ git checkout 'master'
   ```

   


4. *master에 추가 commit 이 발생시키기!!*

   * **동일 파일을 수정 혹은 생성하세요!**

   ```bash
   # README.md 파일 열어서 수정
   (master) $ git add README.md
   (master) $ git commit -m 'Update README.md'
   ```

   

5. master에 병합

   ```bash
   $ git merge 'feature/test'
   ```

   


6. 결과 -> *merge conflict발생*

   > git status 명령어로 충돌 파일을 확인할 수 있음.

   


7. 충돌 확인 및 해결

   


8. merge commit 진행

   ```bash
   $ git commit
   ```

   * vim 편집기 화면이 나타납니다.

     * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.

     * `w` : write

     * `q` : quit

       

9. 커밋 및 확인하기

   ```bash
   $ git log --oneline --graph
   ```


10. branch 삭제

    ```bash
    $ git branch -d 'feature/test'
    ```






## Branch workflow

### Feature Branch workflow

저장소의 소유권이 있는 경우

1. clone을 통해 원격 저장소를 로컬로 복제
2. 각 사용자는 기능 추가를 위해 로컬에 branch를 생성하고 기능을 구현
3. 기능 구현 후 원격 저장소에 각 branch를 push하여 원격 저장소에 반영
4. 원격 저장소에 쌓인 branch를 pull request로 병합
5. 병합 완료된 원격 저장소의 branch는 삭제
6. 각 사용자는 master branch로 checkout
7. 병합된 원격 저장소의 master branch 내용을 pull하여 가져옴
8. 원격 master의 내용이 로컬 master에 반영되면 로컬 branch는 삭제



### Forking workflow

1. 소유권이 없는 원격 저장소를 fork를 통해 자신의 원격 저장소로 복제

2. 본인의 계정에 있는 fork한 원격 저장소를 clone한다

3. 기능 추가를 위해 로컬에 branch를 생성하고 기능을 구현

4. 기능 구현 후 **본인** 계정의 원격 저장소에 push하여 반영

   (git push **origin** feature)

5. 원본 소유자에게 pull request를 보냄

6. 원본에 병합이 완료되면 자신의 원격 저장소에 push된 branch 삭제

7. 로컬 저장소에서 master branch로 checkout

8. 원본 원격 저장소와 연결

   (git remote add **upstream** [원본 URL])

9. 병합된 원본 원격 저장소의 master 내용을 pull

   (git pull **upstream** master)

10. 원격 master의 내용이 로컬 master에 반영되면 로컬 branch는 삭제

