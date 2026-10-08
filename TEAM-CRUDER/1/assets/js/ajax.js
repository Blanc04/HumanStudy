// HTML 문서와 이미지 등의 로딩이 모두 끝나면 bind 함수를 실행한다.
window.addEventListener('load', bind)

// 버튼들의 클릭 이벤트를 연결하는 함수
function bind(){
    // HTML에서 id가 btn1인 요소를 가져온다.
    const search = document.querySelector('#search')
    // btn1을 클릭했을 때 내부 함수를 실행한다.
    search.addEventListener('click', function(){

        // debugger

        // 1. ajax 객체 생성
        // 서버에 데이터를 요청하고 응답을 받을 수 있는 XMLHttpRequest 객체를 만든다.
        const xhr = new XMLHttpRequest()

        // 2. 보낼 준비
        // GET 방식으로 해당 주소에 데이터를 요청하도록 설정한다.
        // GET은 서버에서 데이터를 가져올 때 주로 사용하는 방식이다.
        // 방식 method, 주소
        xhr.open('GET', 'http://127.0.0.1:8000/jobs?keyword=개발')

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
        }
    })
}