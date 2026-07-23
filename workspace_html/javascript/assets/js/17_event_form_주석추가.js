/*
    ============================================================
    17_event_form 복습 핵심
    ============================================================
    1. focus / blur / input / submit 이벤트
    2. event.target, event.currentTarget, this
    3. 이벤트 버블링과 stopPropagation()
    4. 부모 하나로 여러 자식을 처리하는 이벤트 위임
    5. 주문·로그인·피자·메뉴·Todo 실습
    6. querySelector(All), classList, 속성, DOM 생성과 삭제

    이 파일은 원본 실행 코드를 변경하지 않고
    공부용 설명 주석만 추가한 버전이다.
*/

/*
    전달받은 내용을 새 div로 만들어 #view의 맨 위에 표시하는 공통 함수이다.
*/
function log(message){
// 아직 문서에 붙지 않은 새로운 div 요소를 생성한다.
    const div = document.createElement('div')
// CSS 적용을 위해 log 클래스를 추가한다.
    div.classList.add('log')
// innerHTML은 문자열을 HTML로 해석한다. 단순 글자라면 textContent가 더 안전하다.
    div.innerHTML = message
    const view = document.querySelector('#view')
// prepend()이므로 가장 최근 로그가 기존 로그보다 위에 들어간다.
    view.prepend(div)
}

/*
    addEventListener 방식으로 window의 load 이벤트를 등록한다.
    아래의 window.onload = function(){ bind() }와 함께 존재해도 둘 다 실행된다.
*/
window.addEventListener('load', function(){
// 검색어를 입력할 #query 요소를 가져온다.
    const query = document.querySelector("#query")
// focus는 입력칸이 클릭되거나 키보드 이동으로 활성화될 때 발생한다.
    query.addEventListener('focus', function(){
// 활성화된 입력칸의 배경을 salmon으로 바꾼다.
        query.style.background = 'salmon'
    })
// blur는 입력칸이 포커스를 잃을 때 발생한다.
    query.addEventListener('blur', function(){
// 포커스를 잃으면 배경을 흰색으로 되돌린다.
        query.style.background = 'white'
    })
    // input : 값이 변경될 때
/*
    input 이벤트는 타이핑, 붙여넣기, 삭제 등으로 값이 실제 변경될 때 발생한다.
    keyup과 달리 마우스로 붙여넣거나 모바일 입력을 해도 값 변경을 잡을 수 있다.
*/
    query.addEventListener('input', function(){
// 입력할 때마다 현재 검색어를 화면 로그에 추가한다.
        log(query.value)

        // 0 이상 255 이하의 빨강 성분을 무작위로 만든다.
        const r = parseInt(Math.random() * 256)
        // 0 이상 255 이하의 초록 성분을 무작위로 만든다.
        const g = parseInt(Math.random() * 256)
        // 0 이상 255 이하의 파랑 성분을 무작위로 만든다.
        const b = parseInt(Math.random() * 256)
        // 투명도는 0 이상 1 미만의 실수로 만든다.
        const a = Math.random()

        // 입력할 때마다 무작위 RGBA 배경색을 적용한다.
        query.style.backgroundColor = `rgba(${r},${g},${b},${a})`
    })

    // 제출 동작을 검사할 form 요소를 가져온다.
    const form = document.querySelector('#form')
/*
    submit 이벤트는 제출 버튼 클릭뿐 아니라
    입력칸에서 Enter를 눌러 폼이 제출될 때도 발생한다.
*/
    form.addEventListener('submit', function(event){
        // 태그의 기본(고유) 기능을 막음
        // 폼이 바로 서버로 전송되거나 페이지가 이동하는 기본 동작을 우선 막는다.
        event.preventDefault()
        // 앞뒤 공백을 뺀 검색어 길이가 2보다 작은지 검사한다.
        if(query.value.trim().length<2){
            alert('검색어는 2글자 이상입니다')
        } else {
    /*
        조건을 통과하면 form.submit()으로 실제 제출한다.
        form.submit()은 submit 이벤트를 다시 발생시키지 않으므로 무한 반복되지 않는다.
        또한 브라우저의 일반 submit 이벤트 검사를 우회하는 특성이 있다.
    */
            form.submit()
        }
    })

// 이벤트 버블링과 target/currentTarget을 비교할 부모 요소이다.
    const parent = document.querySelector('#parent')
// 일반 function 문법을 사용한 클릭 리스너이다.
    parent.addEventListener('click', function(event){
        log('부모 클릭')

// target은 사용자가 실제로 클릭한 가장 안쪽 요소이다.
        // target : 실제 이벤트가 발생한 DOM
        console.log('event.target', event.target)

// currentTarget은 현재 이 리스너가 등록되어 실행 중인 요소이다. 여기서는 parent이다.
        // currentTarget : 이벤트가 적용되어 있는 DOM
        console.log('event.currentTarget', event.currentTarget)

    /*
        this를 정확히 정리하면:
        - addEventListener의 일반 function 안에서는 this === event.currentTarget
        - 화살표 함수는 자신의 this를 만들지 않고 바깥 스코프의 this를 사용한다.
        - 브라우저의 일반 script 최상위에서 화살표 함수가 바깥 this를 받으면
          결과가 window일 수 있지만, 모듈 등 실행 환경에 따라 달라질 수 있다.

        따라서 원본의 '대부분 window' 설명은 일반 function 리스너에는 맞지 않는다.
        바로 아래 비교 결과는 true가 된다.
    */
        // this
        //  addEventListener 안에서는 event.currentTarget을 의미
        //  대부분의 경우 window를 가지고 있음
        //  그래서 현재 this에 어떤 값이 있는지 알고 있을 때만 쓰기
        //  arrow 함수의 경우 this === window
        console.log('this', this)
        console.log(this === event.currentTarget)
    })

// parent 안의 자식 요소 #child1에 별도 클릭 이벤트를 등록한다.
    const child1 = document.querySelector('#child1')
    child1.addEventListener('click', function(event){

        // 전달 방지
        // 부모로 전달되는 이벤트 중지
    /*
        이벤트가 child1에서 부모 방향으로 버블링되는 것을 중지한다.
        따라서 child1을 클릭해도 위 parent의 클릭 리스너는 실행되지 않는다.
    */
        event.stopPropagation()

        log('자식 1 클릭')
    })


    // 1. click된 dom 출력
    // 5. 작성자를 클릭했을 때 속성 writer 값 출력
/*
    board 하나에 클릭 이벤트를 등록해 내부의 여러 요소를 처리한다.
    이것이 이벤트 위임(event delegation) 방식이다.
*/
    const board = document.querySelector('#board')
    board.addEventListener('click', function(event){
// board 바깥 부모로 이벤트가 더 올라가는 것은 막지만 board 내부의 이전 단계까지 되돌리지는 않는다.
        event.stopPropagation()
// 실제 클릭된 요소를 확인한다.
        console.log(event.target)
    // 2. 지금 클릭 요소에 클래스 chk가 있는지 출력
    // 3. 만약 체크박스일 때만 value 출력
// 실제 클릭 요소에 chk 클래스가 있을 때만 체크박스 값으로 처리한다.
        if(event.target.classList.contains('chk')){
            log(event.target.value)
        }
    // 4. 제목을 클릭했을 때 제목 글씨 출력
// title 클래스를 클릭했다면 해당 요소의 글자를 출력한다.
        if(event.target.classList.contains('title')){
            log(event.target.textContent)
        }
// writer라는 사용자 정의 속성이 있는 요소를 클릭했는지 검사한다.
        if(event.target.hasAttribute('writer')){
// getAttribute('writer')로 속성에 저장된 작성자 값을 읽는다.
            log(event.target.getAttribute('writer'))
        }
    })
/*
    이번에는 board 안의 모든 tr을 찾아 각각 이벤트를 등록한다.
    위 이벤트 위임 방식과 비교하기 위한 코드이다.

    제목 등을 클릭하면 tr 리스너와 board 리스너가 모두 실행되어
    같은 내용이 두 번 출력될 수 있다.
*/
    const trs = document.querySelectorAll('#board tr')
// for...of로 NodeList의 각 행(tr)을 하나씩 꺼낸다.
    for(let tr of trs){
// 현재 반복 중인 행마다 별도의 클릭 리스너를 등록한다.
        tr.addEventListener('click', function(event){
            console.log(event.target)

            if(event.target.classList.contains('chk')){
                log(event.target.value)
            }
            if(event.target.classList.contains('title')){
                log(event.target.textContent)
            }
            if(event.target.hasAttribute('writer')){
                log(event.target.getAttribute('writer'))
            }
        })
// 각 행 안의 체크박스에도 별도 클릭 리스너를 등록한다.
        tr.querySelector('input.chk').addEventListener('click', function(event){
    /*
        체크박스 클릭 이벤트가 tr과 board로 버블링되는 것을 막는다.
        따라서 체크박스 클릭 시 이 함수만 실행된다.
    */
            event.stopPropagation()

            // console.log(this.parentNode)
            
    /*
        this는 클릭된 체크박스이다.
        parentNode를 두 번 올라가 행을 찾은 뒤,
        그 행 내부의 .title 글자를 출력한다.
    */
            console.log(this.parentNode.parentNode.querySelector('.title').innerText)
        })
    }
})

/*
    일반 script의 최상위 this는 보통 window이다.
    단, <script type="module">에서는 최상위 this가 undefined이다.
*/
console.log(this)

/*
    onload 프로퍼티 방식으로 bind를 호출한다.
    위 addEventListener('load', ...) 리스너를 지우지는 않으므로 load 때 둘 다 실행된다.
*/
window.onload = function(){
    bind()
}

// 문제 1~5의 이벤트와 DOM 작업을 연결하는 함수이다.
function bind(){
    // 문제 1 : 주문과 배송
    // 주문 정보 : input으로 이름, 주소
    // ㅁ 주문 정보와 배송 정보가 같습니다
    // 배송 정보 : input으로 이름, 주소
    // + 체크하면 주문 정보가 배송 정보로 복사
    // + 체크 풀면 배송 정보 글씨 지우기
    /*
        주문 영역과 배송 영역을 각각 가져온다.
        q1Order는 아래 주석 처리된 대안 코드에서 사용되며 현재 실행 코드에서는 직접 쓰이지 않는다.
    */
    const q1Order = document.querySelector('#q1Order')
    const q1Delivery = document.querySelector('#q1Delivery')
    /*
        querySelectorAll은 해당 클래스를 가진 모든 요소를 NodeList로 반환한다.
        여기서는 [0]을 주문 정보, [1]을 배송 정보라고 가정한다.
    */
    const q1Name = document.querySelectorAll('.q1Name')
    const q1Address = document.querySelectorAll('.q1Address')
// 주문 정보와 배송 정보가 같다는 체크박스이다.
    const same = document.querySelector('#q1Same')
// 체크 상태가 바뀌도록 사용자가 클릭할 때 실행된다.
    same.addEventListener('click', function(event){
// checked 프로퍼티가 true이면 현재 체크된 상태이다.
        if(same.checked == true){
// 주문자 이름의 값을 배송자 이름에 복사한다.
            q1Name[1].value = q1Name[0].value
// 주문 주소의 값을 배송 주소에 복사한다.
            q1Address[1].value = q1Address[0].value
            // q1Delivery.querySelector('.q1Name').value = q1Order.querySelector('.q1Name').value
            // q1Delivery.querySelector('.q1Address').value = q1Order.querySelector('.q1Address').value
// 체크를 해제하면 배송 정보 입력칸을 빈 문자열로 초기화한다.
        } else {
            q1Delivery.querySelector('.q1Name').value = ''
            q1Delivery.querySelector('.q1Address').value = ''
        }
    })


    // 문제 2 : 로그인창
    // 로그인 버튼 눌렀을 때
    // 아이디 / 비밀번호 없으면 빨간 글씨 나오게
    // 단, 아이디/비밀번호를 쓰고 로그인을 누르면 빨간 글씨 지우기
// 로그인 버튼 클릭 시 입력값의 빈칸을 순서대로 검사한다.
    const login = document.querySelector('#login')
    login.addEventListener('click', function(){
// 아이디 입력 요소를 가져온다.
        const id = document.querySelector('#id')
// 비밀번호 입력 요소를 가져온다.
        const pw = document.querySelector('#pw')
// 경고 문구를 표시할 요소를 가져온다.
        const warning = document.querySelector('.warning')
        console.log(id.value)
        console.log(pw.value)

        // id를 적었는지 판단
// 아이디가 비어 있으면 첫 번째 경고를 표시한다.
        if(id.value.trim() == ''){
            console.log('아이디는 필수입니다')
            warning.innerText = '아이디는 필수입니다'
        }
        // 비밀번호를 적었는지 판단
    /*
        else if이므로 아이디가 비어 있지 않을 때만 비밀번호를 검사한다.
        둘 다 비어 있으면 아이디 경고만 표시되는 구조이다.
    */
        else if(pw.value.trim() == ''){
            console.log('비밀번호는 필수입니다')
            warning.innerText = '비밀번호는 필수입니다'
// 두 입력값이 모두 있으면 이전 경고 문구를 지운다.
        } else {
            warning.innerText = ''
        }
    })


    // 문제 3 : 피자 주문
    // 1. 피자 종류 선택 : select
    // - 불고기, 페퍼로니, 포테이토, 치즈, 파인애플, 고르곤졸라
    // 2. 사이즈 선택 : radio
    // - small(18000), medium(20000), large(22000)
    // 3. 도우 선택 : radio
    // - 씬, 고구마, 치즈, 소보로
    // 4. 토핑 : checkbox
    // - 감자(2000), 고구마(2000), 치즈(2500), 베이컨(3000), 옥수수(500), 페페론치노(2500)
    // [확인]
    // + 문제3-1 : 선택 내역 모두 출력
    // 피자 종류를 선택하는 select
// name이 q3Pizza인 select 요소 하나를 가져온다.
    const q3Pizza = document.querySelector('select[name="q3Pizza"]')
    // 선택 결과를 출력하는 버튼
// 주문 내역을 계산하고 출력할 확인 버튼이다.
    const q3Button = document.querySelector('#q3Button')

    // 각각의 결과를 출력할 div
    // 클래스가 2개인 요소는 클래스 사이를 띄우지 않고 붙여서 선택
    // 예: class="q3Result pizza" → '.q3Result.pizza'
    
    /*
        '.q3Result.size'는 q3Result와 size 클래스를 동시에 가진 하나의 요소를 뜻한다.
        '.q3Result .size'처럼 띄우면 자손 요소를 찾는 다른 선택자가 된다.
    */
    const resultSize = document.querySelector('.q3Result.size')
    const resultPizza = document.querySelector('.q3Result.pizza')
    const resultTopping = document.querySelector('.q3Result.topping')
    const resultPrice = document.querySelector('.q3Result.price')

    // 출력 버튼을 클릭했을 때 주문 내역을 확인
// 확인 버튼을 클릭하면 현재 선택 상태를 읽어 주문 결과를 만든다.
    q3Button.addEventListener('click', function(event) {

    // 1. 피자 종류 출력
// select.value에는 현재 선택한 option의 value가 들어 있다.
    resultPizza.innerText = `피자: ${q3Pizza.value}`

    // 2. 사이즈 (단일 선택)
    // :checked를 사용하면 같은 name을 가진 라디오 버튼 중
    // 현재 선택된 요소 하나만 가져올 수 있음
    /*
        :checked 가상 클래스는 현재 선택된 radio 하나를 찾는다.
        아무 사이즈도 선택하지 않았다면 checkedSize는 null이 되어
        아래 parentElement 접근에서 오류가 날 수 있다.
    */
    const checkedSize = document.querySelector('input[name="q3Size"]:checked')
    // 사이즈 가격을 저장할 변수
// 사이즈 가격을 누적 계산에 사용할 숫자 변수로 준비한다.
    let sizePrice = 0
    
    // 라디오 버튼을 감싸는 부모 label의 글자를 가져옴
    // trim()은 글자 앞뒤의 불필요한 공백과 줄바꿈을 제거
// 체크된 input의 부모 label 전체 글자를 사이즈 표시로 사용한다.
    resultSize.innerText = `사이즈: ${checkedSize.parentElement.innerText.trim()}`
    // input의 value는 문자열이므로 가격 계산을 위해 숫자로 변환
// input.value는 문자열이므로 parseInt로 정수 가격으로 변환한다.
    sizePrice = parseInt(checkedSize.value) // value에 있는 가격을 숫자로 변환 (총액 계산용)

    // 3. 도우 (단일 선택)
    // 사이즈와 마찬가지로 :checked를 사용해서
    // 선택된 도우 라디오 버튼 하나만 가져옴
    /*
        선택된 도우 radio를 찾는다.
        도우도 아무것도 선택하지 않았다면 checkedDow가 null일 수 있다.
    */
    const checkedDow = document.querySelector('input[name="q3Dow"]:checked')
    const resultDow = document.querySelector('.q3Result.dow')
    // 도우는 value에 이름이 들어 있으므로 바로 출력
// 도우 input의 value에 도우 이름이 있다고 가정하고 바로 출력한다.
    resultDow.innerText = `도우: ${checkedDow.value}`

    // 4. 토핑 (다중 선택)
    // 체크박스는 여러 개를 동시에 선택할 수 있으므로
    // querySelectorAll()로 선택된 체크박스를 모두 가져옴
// q3Topping 내부에서 체크된 모든 체크박스를 NodeList로 가져온다.
    const checkedToppings = document.querySelectorAll('.q3Topping input[type="checkbox"]:checked');
    // 선택된 토핑 이름들을 저장할 배열
// 선택된 토핑 이름을 순서대로 담을 배열이다.
    let toppingNames = []
    // 선택된 토핑 가격의 합계를 저장할 변수
// 선택된 토핑 가격을 계속 더할 누적 변수이다.
    let toppingPrice = 0

     // 선택된 토핑 체크박스를 하나씩 반복
// 선택된 체크박스 각각에 대해 같은 작업을 반복한다.
    checkedToppings.forEach(function(checkbox) {
        // 체크박스를 감싸는 label의 글자를 배열에 추가
// label의 표시 글자를 배열에 추가한다.
        toppingNames.push(checkbox.parentElement.innerText.trim()) // 텍스트 추출
        // value의 가격을 숫자로 변환한 뒤 기존 가격에 더함
// 각 checkbox.value 가격을 숫자로 바꿔 합계에 더한다.
        toppingPrice += parseInt(checkbox.value) // 토핑 가격 누적
    })

    // 선택된 토핑이 하나 이상 있으면
    // join(', ')으로 배열의 항목들을 쉼표로 연결
// 선택한 토핑이 하나라도 있는지 배열 길이로 판단한다.
    if (toppingNames.length > 0) {
// join(', ')으로 토핑 이름들을 쉼표와 공백으로 연결한다.
        resultTopping.innerText = `토핑: ${toppingNames.join(', ')}`
    } else {
        resultTopping.innerText = `토핑: 선택안함`
    }

    // + 문제3-2 : 선택 내역과 총액 출력
    // 5. 총액 계산 (문제 3-2)
// 총액은 사이즈 가격과 모든 토핑 가격의 합이다. 도우 추가금은 현재 계산에 없다.
    const totalPrice = sizePrice + toppingPrice;
    resultPrice.innerText = `총액: ${totalPrice}원`
    })


    // 문제 4 : 메뉴 선택
    // 인기상품순, 낮은가격순, 높은가격순, 신상품순, 상품평 많은순
    // + 클릭한 것만 굵은 글씨로 유지
// 메뉴 항목 전체를 NodeList로 가져온다.
    const q4Menu = document.querySelectorAll('.q4Menu')
// 각 메뉴에 클릭 이벤트를 하나씩 등록한다.
    q4Menu.forEach(function(menu){
    menu.addEventListener('click', function(){
    /*
        메뉴를 클릭할 때 전체 메뉴를 다시 반복하며 선택 클래스를 모두 제거한다.
        바깥과 안쪽 매개변수 이름이 모두 menu라서 서로 다른 스코프의 변수가 가려진다.
        문법 오류는 아니지만 복습할 때는 이름을 다르게 하면 더 읽기 쉽다.
    */
        q4Menu.forEach(function(menu){
        menu.classList.remove('q4Checked')
        })
// 모든 선택 표시를 지운 뒤 실제 클릭한 바깥쪽 menu에만 클래스를 추가한다.
        menu.classList.add('q4Checked')
        })
    })


    // 문제 5 : Todo List
    // 할일을 적는 input, 추가 버튼
    /*
        Todo 영역 요소를 미리 가져온다.
        q5Custom은 현재 실행 코드에서 사용되지 않는 변수이다.
    */
    const q5Custom = document.getElementById('q5Custom') 
    const q5Area = document.getElementById('q5Area')
    const q5Add = document.getElementById('q5Add')
    const q5Board = document.querySelector('.q5Board')

    // + 5-1 : 추가버튼 누르면 체크박스와 할일이 하단에 추가된다
    // <div>
    //     <input type="checkbox">
    //     <span>입력한 할 일</span>
    //     <button>삭제</button>
    // </div>
// 추가 버튼 클릭 시 Todo 한 줄을 구성할 DOM 요소들을 새로 만든다.
    q5Add.addEventListener('click', function(event) {
// 체크박스, 내용, 삭제 버튼을 감쌀 부모 div이다.
        const div = document.createElement('div')
// 새 input 요소를 만든다.
        const input = document.createElement('input')
// input의 type 속성을 checkbox로 지정한다.
        input.setAttribute('type', 'checkbox')
// 새 체크박스에 checked라는 CSS 클래스를 지정한다. checked 상태 자체를 뜻하지는 않는다.
        input.setAttribute('class', 'checked')
// 할 일 글자를 표시할 span을 만든다.
        const span = document.createElement('span')
// 사용자가 입력한 q5Area.value를 span의 글자로 복사한다.
        span.innerText = q5Area.value
// 각 Todo 줄에 들어갈 삭제 버튼을 만든다.
        const button = document.createElement('button')
    /*
        모든 삭제 버튼에 같은 id를 부여한다.
        HTML의 id는 문서에서 고유해야 하므로 여러 줄이 생기면 중복 id가 된다.
        현재 삭제는 event.target을 사용하므로 실행은 가능하지만 구조상 class가 더 적절하다.
    */
        button.setAttribute('id', 'q5Delete')
    // + 5-2 : 개별 삭제 버튼이 있고, 클릭 시 그 줄이 지워진다 (dom.remove())
// 버튼에 보일 글자를 '삭제'로 설정한다.
        button.textContent = '삭제'
// 각 버튼에 자신이 속한 Todo 줄을 지우는 클릭 이벤트를 등록한다.
        button.addEventListener('click', function(event) {
    /*
        event.target은 실제 클릭한 삭제 버튼이다.
        parentElement는 그 버튼을 감싼 Todo div이며 remove()로 문서에서 삭제한다.
    */
            event.target.parentElement.remove()
        })
// 만든 input, span, button을 순서대로 새 div의 자식으로 넣는다.
        div.append(input, span, button)
// 완성된 Todo div를 실제 화면의 q5Board 끝에 추가한다.
        q5Board.append(div)
    })

    // + 5-3 : 전체 선택 checkbox가 있고
    //         전체 선택 체크 시 : 모든 checkbox 체크
// 전체 선택 기능에 사용할 체크박스를 가져온다. 아직 이벤트 코드는 작성되지 않았다.
    const q5AllCheck = document.getElementById('q5AllCheck')
// 선택 삭제 버튼을 가져온다. 이 역시 현재는 변수만 준비된 상태이다.
    const q5SelectDelete = document.getElementById('q5SelectDelete')
    //         해제 시 : 모든 checkbox 체크 해제
    // + 5-4 : 전체 선택 후 하나라도 개별 해제가 되면 전체 선택도 해제
    //         개별로 모두 체크한 경우 전체 선택도 체크된다
    // + 5-5 : 선택 삭제 버튼 클릭 시 선택된 내용만 삭제
/*
    현재 문제 5는 Todo 추가와 개별 삭제까지만 구현되어 있다.
    전체 선택, 개별 체크와 전체 선택 동기화, 선택 삭제는 아직 미구현 상태이다.
*/
}
