// HTML 문서와 이미지 등의 로딩이 모두 끝나면 bind 함수를 실행한다.
window.addEventListener('load', bind)

// 버튼들의 클릭 이벤트를 연결하는 함수
function bind(){
    // HTML에서 id가 btn1인 요소를 가져온다.
    const btn1 = document.querySelector('#btn1')
    // btn1을 클릭했을 때 내부 함수를 실행한다.
    btn1.addEventListener('click', function(){

        // 1. ajax 객체 생성
        // 서버에 데이터를 요청하고 응답을 받을 수 있는 XMLHttpRequest 객체를 만든다.
        const xhr = new XMLHttpRequest()

        // 2. 보낼 준비
        // GET 방식으로 해당 주소에 데이터를 요청하도록 설정한다.
        // GET은 서버에서 데이터를 가져올 때 주로 사용하는 방식이다.
        // 방식 method, 주소
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')

        // 3. 보내기
        // 위에서 준비한 요청을 실제 서버로 보낸다.
        xhr.send()

        // 4. 결과 활용
        // 서버의 응답이 모두 도착하면 실행되는 함수
        xhr.onload = function(){
            // 서버 요청이 끝났는지 확인하기 위한 출력
            console.log('다녀왔어')
            // 서버가 보내준 원본 응답 내용을 출력한다.
            // responseText는 아직 문자열 형태이다.
            console.log(xhr.responseText)

            // 깜짝 퀴즈

            // JSON 형태의 문자열을 자바스크립트 배열 또는 객체로 변환한다.
            // 변환해야 배열 번호나 객체 속성을 이용할 수 있다.
            const Quiz = JSON.parse(xhr.responseText)

            // 두 번째 사람의 이름을 출력
            // 배열 번호는 0부터 시작하므로 두 번째 사람은 Quiz[1]이다.
            // Quiz[1]의 name 속성에 접근한다.
            // Ervin Howell
            console.log(Quiz[1].name)

            // 세 번째 사람의 lat을 출력
            // 세 번째 사람은 Quiz[2]이다.
            // address 안의 geo 안에 들어 있는 lat 속성까지 순서대로 접근한다.
            // -68.6102
            console.log(Quiz[2].address.geo.lat)
        }
        
    })

    // HTML에서 id가 btn2인 요소를 가져온다.
    const btn2 = document.querySelector('#btn2')
        // btn2를 클릭했을 때 내부 함수를 실행한다.
        btn2.addEventListener('click', function(){
        // 1. ajax 객체 생성
        // 서버 또는 파일에 데이터를 요청할 XMLHttpRequest 객체를 만든다.
        const xhr = new XMLHttpRequest()
        // 2. 보낼 준비
        // 현재 프로젝트에 있는 19_json.html 파일을 GET 방식으로 요청한다.
        // 방식 method, 주소
        xhr.open('GET', '19_json.html')
        // 3. 보내기
        // 준비한 요청을 실제로 보낸다.
        xhr.send()
        // 4. 결과 활용
        // 요청한 파일의 응답이 모두 도착하면 실행된다.
        xhr.onload = function(){
            // 요청이 끝났다는 것을 확인하기 위한 출력
            console.log('다녀왔어')
            // 19_json.html에서 받아온 원본 문자열을 출력한다.
            console.log(xhr.responseText)
        }
    })

    // HTML에서 id가 btn3인 요소를 가져온다.
    const btn3 = document.querySelector('#btn3')
        // btn3을 클릭했을 때 기상청 API에 날씨 데이터를 요청한다.
        btn3.addEventListener('click', function(){
        const now = new Date()
        const today = now.toISOString().split('T')[0].replace(/-/g, '')
        let hour = now.getHours() - 1
        if(hour < 10){
            hour = '0'+hour + '00'
        } else {
            hour = hour + '00'
        }
        // 기상청 API를 사용하기 위한 인증키
        const key= 'qVTaW2lslPLGXY2uHKVY3Vuc66ZQmC950RmMKYEg4Grvfz%2FeYbsd%2Fp4F0CzdQQwC26aBf2fTEHW76VU0OA04RQ%3D%3D'
        // 기상청 초단기예보 API의 기본 주소
        let url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
        // 기본 주소 뒤에 요청 조건을 붙이기 시작한다.
        url += '?'
        // 인증키를 주소에 추가한다.
        url += 'serviceKey='+key
        // 한 번에 최대 1000개의 데이터를 요청한다.
        url += '&numOfRows=1000'
        // 여러 페이지 중 첫 번째 페이지를 요청한다.
        url += '&pageNo=1'
        // 응답 데이터를 JSON 형식으로 받는다.
        url += '&dataType=JSON'
        // 예보를 발표한 기준 날짜
        url += '&base_date=20260722'
        // 예보를 발표한 기준 시간
        url += '&base_time=1530'
        // 날씨를 확인할 지역의 X 격자 좌표
        url += '&nx=63'
        // 날씨를 확인할 지역의 Y 격자 좌표
        url += '&ny=110'
        // 1. ajax 객체 생성
        // 기상청 API에 요청을 보낼 XMLHttpRequest 객체를 만든다.
        const xhr = new XMLHttpRequest()
        // 2. 보낼 준비
        // 위에서 완성한 url 주소에 GET 방식으로 요청하도록 설정한다.
        // 방식 method, 주소
        xhr.open('GET', url)
        // 3. 보내기
        // 기상청 API로 요청을 실제 전송한다.
        xhr.send()
        // 4. 결과 활용
        // 기상청에서 응답이 모두 도착하면 실행된다.
        xhr.onload = function(){
            // 요청 완료 확인용 출력
            console.log('다녀왔어')
            console.log('상태 코드:', xhr.status)
            // 200번대가 아니면 정상 응답이 아니므로 실행 중단
            if(xhr.status < 200 || xhr.status >= 300){
                console.error('API 요청 실패')
                console.error(xhr.responseText)
                return
            }
            // 기상청에서 받은 JSON 문자열을 자바스크립트 객체로 변환한다.
            const data = JSON.parse(xhr.responseText)
            // 변환된 전체 날씨 데이터의 구조를 확인한다.
            console.log(data)
            // 전체 예보 데이터 중 첫 번째 데이터의 카테고리를 출력한다.
            console.log(data.response.body.items.item[0].category)
            // 전체 예보 데이터 중 첫 번째 데이터의 예측값을 출력한다.
            console.log(data.response.body.items.item[0].fcstValue)
            // 전체 예보 데이터 중 첫 번째 데이터의 예측시간을 출력한다.
            console.log(data.response.body.items.item[0].fcstTime)
            // 전체 응답 구조에서 실제 예보 데이터 배열만 꺼내 itemData에 저장한다.
            let itemData = data.response.body.items.item
            // itemData 배열의 처음부터 마지막까지 모든 데이터를 반복한다.
            for(let i=0; i<itemData.length; i++){
                // 현재 데이터의 카테고리가 T1H이면 출력한다.
                // T1H는 1시간 기온을 의미한다.
                if(itemData[i].category == 'T1H'){
                    console.log(itemData[i])
                // 현재 데이터의 카테고리가 RN1이면 출력한다.
                // RN1은 1시간 강수량을 의미한다.
                } else if(itemData[i].category == 'RN1') {
                    console.log(itemData[i])
                // 현재 데이터의 카테고리가 REH이면 출력한다.
                // REH는 습도를 의미한다.
                } else if(itemData[i].category == 'REH') {
                    console.log(itemData[i])
                }
            }
            // itemData에서 T1H, RN1, REH 카테고리만 골라 새로운 배열을 만든다.
            let filtered = itemData.filter(function(data){
                // 현재 데이터가 기온, 강수량, 습도 중 하나인지 확인한다.
                if(data.category == 'T1H' 
                    || data.category == 'RN1' 
                    || data.category == 'REH'){
                    // true를 반환한 데이터는 filtered 배열에 포함된다.
                    return true
                }
            })
            // 필요한 카테고리만 남은 filtered 배열 전체를 출력한다.
            console.log(filtered)

            // 문제 1
            // 예측카테고리 | 예측시간 | 값
            // filtered 배열에 들어 있는 모든 데이터를 하나씩 반복한다.
            const q1 = document.querySelector('#q1')
            q1.innerHTML = ''
            for(let i=0; i<filtered.length; i++){
                // 현재 데이터의 예측 카테고리를 출력한다.
                console.log('예측 카테고리', filtered[i].category)
                // 현재 데이터의 예측 시간을 출력한다.
                console.log('예측 시간', filtered[i].fcstTime)
                // 현재 데이터의 예측값을 출력한다.
                console.log('예측값', filtered[i].fcstValue)
            }
            filtered.forEach(function(predic){
                // 현재 데이터의 예측 카테고리를 출력한다.
                console.log('예측 카테고리', predic.category)
                // 현재 데이터의 예측 시간을 출력한다.
                console.log('예측 시간', predic.fcstTime)
                // 현재 데이터의 예측값을 출력한다.
                console.log('예측값', predic.fcstValue)
            })
            // 문제 2
            // 시간 | 온도 | 습도 | 강수량
            const q2 = {}
            for(let i=0; i<filtered.length; i++){
                // 현재 데이터의 예측시간을 time에 저장
                const time = filtered[i].fcstTime
                // 틀 생성
                if(q2[time] == undefined){
                    q2[time] = {
                        'T1H' : '',
                        'REH' : '',
                        'RN1' : ''
                    }
                }
                if(filtered[i].category == 'T1H'){
                    // 카테고리 온도
                    q2[time]['T1H'] = filtered[i].fcstValue
                } else if(filtered[i].category == 'REH'){
                    // 카테고리 습도
                    q2[time]['REH'] = filtered[i].fcstValue
                } else if(filtered[i].category == 'RN1'){
                    // 카테고리 강수량
                    q2[time]['RN1'] = filtered[i].fcstValue
                }
                // 테스트 출력
                console.log(time, q2[time])
            }
            // 최종 출력
            const q2Table = document.querySelector('#q2')
            console.log('q2Table:', q2Table)
            for(let time in q2){
                console.log(
                    `시간: ${time} | 온도: ${q2[time]['T1H']} | 습도: ${q2[time]['REH']} | 강수량: ${q2[time]['RN1']}`
                )
                // 회원 한 명당 행 하나 생성
                const tr = document.createElement('tr')
                // 각 칸을 직접 생성
                const timeTd = document.createElement('td')
                const t1hTd = document.createElement('td')
                const rehTd = document.createElement('td')
                const rn1Td = document.createElement('td')
                timeTd.textContent = time
                t1hTd.textContent = q2[time]['T1H']
                rehTd.textContent = q2[time]['REH']
                rn1Td.textContent = q2[time]['RN1']
                // tr 안에 td 4개 넣기
                tr.append(timeTd)
                tr.append(t1hTd)
                tr.append(rehTd)
                tr.append(rn1Td)
                // tbody 안에 완성된 tr 넣기
                q2Table.append(tr)
            }
        }
    })

    // btn4를 클릭 시
    // https://jsonplaceholder.typicode.com/users
    // 10명의 정보 중 id, name, zipcode, 회사이름을 html로 표시
    const btn4 = document.querySelector('#btn4')
    // btn4를 클릭했을 때 내부 함수를 실행한다.
    btn4.addEventListener('click', function(){
        // 1. ajax 객체 생성
        // 서버 또는 파일에 데이터를 요청할 XMLHttpRequest 객체를 만든다.
        const xhr = new XMLHttpRequest()
        // 2. 보낼 준비
        // 방식 method, 주소
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')
        // 3. 보내기
        // 준비한 요청을 실제로 보낸다.
        xhr.send()
        // 4. 결과 활용
        // 요청한 파일의 응답이 모두 도착하면 실행된다.
        xhr.onload = function(){
            // 요청이 끝났다는 것을 확인하기 위한 출력
            console.log('다녀왔어')
            // https://jsonplaceholder.typicode.com/users 에서 받아온 원본 문자열을 출력한다.
            console.log(xhr.responseText)

            const btn4Quiz = JSON.parse(xhr.responseText)
            // btn4Quiz.forEach(function(data){
            //     console.log(btn4Quiz[data].name)
            // })
            const memberInfo = document.querySelector('#memberInfo')
            // for(let i=0; i<btn4Quiz.length; i++){
            //     console.log(btn4Quiz[i].id)
            //     console.log(btn4Quiz[i].name)
            //     console.log(btn4Quiz[i].address.zipcode)
            //     console.log(btn4Quiz[i].company.name)
            //     const member = [
            //         btn4Quiz[i].id,
            //         btn4Quiz[i].name,
            //         btn4Quiz[i].address.zipcode,
            //         btn4Quiz[i].company.name
            //     ]
            //     // 현재 행을 담을 tr 생성
            //     const tr = document.createElement('tr')
            //     // td는 현재 행에 들어 있는 값의 개수만큼 반복문 돌리기
            //     for(let j=0;j<member.length;j++){
            //         // 반복 수 만큼 td 생성
            //         const td = document.createElement('td')
            //         // i = 몇 번째 행, j = 행 안의 몇 번째 칸
            //         td.textContent = member[j]
            //         // 현재 tr 안에 td를 자식으로 넣기
            //         tr.append(td)
            //     }
            //     // memberInfo 안에 완성된 현재 tr을 자식으로 넣기
            //     memberInfo.append(tr)
            // }
            for(let i=0; i<btn4Quiz.length; i++){
                // 회원 한 명당 행 하나 생성
                const tr = document.createElement('tr')
                // 각 칸을 직접 생성
                const idTd = document.createElement('td')
                const nameTd = document.createElement('td')
                const zipcodeTd = document.createElement('td')
                const companyTd = document.createElement('td')
                // 각 칸에 값 넣기
                idTd.textContent = btn4Quiz[i].id
                nameTd.textContent = btn4Quiz[i].name
                zipcodeTd.textContent = btn4Quiz[i].address.zipcode
                companyTd.textContent = btn4Quiz[i].company.name
                // tr 안에 td 4개 넣기
                tr.append(idTd)
                tr.append(nameTd)
                tr.append(zipcodeTd)
                tr.append(companyTd)
                // tbody 안에 완성된 tr 넣기
                memberInfo.append(tr)
            }
        }
    })
    const btn5 = document.querySelector('#btn5')
    btn5.addEventListener('click', function(){
        let a= undefined
        try{
            a.push(1)
        }catch(e){
            console.log(e)
        }
        const url = 'https://jsonplaceholder.typicode.com/users'
        fetch(url, {
            method: 'GET'
        }).then(function(response){
            return response.json()
        }).then(function(data){
            console.log(data)
        }).catch(function(error){
            console.error(error)
        })
    })
}