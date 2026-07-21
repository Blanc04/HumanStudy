function log(message){
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message
    const view = document.querySelector('#view')
    view.prepend(div)
}

window.addEventListener('load', function(){
    const query = document.querySelector("#query")
    query.addEventListener('focus', function(){
        query.style.background = 'salmon'
    })
    query.addEventListener('blur', function(){
        query.style.background = 'white'
    })
    // input : 값이 변경될 때
    query.addEventListener('input', function(){
        log(query.value)

        const r = parseInt(Math.random() * 256)
        const g = parseInt(Math.random() * 256)
        const b = parseInt(Math.random() * 256)
        const a = Math.random()

        query.style.backgroundColor = `rgba(${r},${g},${b},${a})`
    })

    const form = document.querySelector('#form')
    form.addEventListener('submit', function(event){
        // 태그의 기본(고유) 기능을 막음
        event.preventDefault()
        if(query.value.trim().length<2){
            alert('검색어는 2글자 이상입니다')
        } else {
            form.submit()
        }
    })

    const parent = document.querySelector('#parent')
    parent.addEventListener('click', function(event){
        log('부모 클릭')

        // target : 실제 이벤트가 발생한 DOM
        console.log('event.target', event.target)

        // currentTarget : 이벤트가 적용되어 있는 DOM
        console.log('event.currentTarget', event.currentTarget)

        // this
        //  addEventListener 안에서는 event.currentTarget을 의미
        //  대부분의 경우 window를 가지고 있음
        //  그래서 현재 this에 어떤 값이 있는지 알고 있을 때만 쓰기
        //  arrow 함수의 경우 this === window
        console.log('this', this)
        console.log(this === event.currentTarget)
    })

    const child1 = document.querySelector('#child1')
    child1.addEventListener('click', function(event){

        // 전달 방지
        // 부모로 전달되는 이벤트 중지
        event.stopPropagation()

        log('자식 1 클릭')
    })


    // 1. click된 dom 출력
    // 5. 작성자를 클릭했을 때 속성 writer 값 출력
    const board = document.querySelector('#board')
    board.addEventListener('click', function(event){
        event.stopPropagation()
        console.log(event.target)
    // 2. 지금 클릭 요소에 클래스 chk가 있는지 출력
    // 3. 만약 체크박스일 때만 value 출력
        if(event.target.classList.contains('chk')){
            log(event.target.value)
        }
    // 4. 제목을 클릭했을 때 제목 글씨 출력
        if(event.target.classList.contains('title')){
            log(event.target.textContent)
        }
        if(event.target.hasAttribute('writer')){
            log(event.target.getAttribute('writer'))
        }
    })
    const trs = document.querySelectorAll('#board tr')
    for(let tr of trs){
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
        tr.querySelector('input.chk').addEventListener('click', function(event){
            event.stopPropagation()

            // console.log(this.parentNode)
            
            console.log(this.parentNode.parentNode.querySelector('.title').innerText)
        })
    }
})

console.log(this)

window.onload = function(){
    bind()
}

function bind(){
    // 문제 1 : 주문과 배송
    // 주문 정보 : input으로 이름, 주소
    // ㅁ 주문 정보와 배송 정보가 같습니다
    // 배송 정보 : input으로 이름, 주소
    // + 체크하면 주문 정보가 배송 정보로 복사
    // + 체크 풀면 배송 정보 글씨 지우기
    const q1Order = document.querySelector('#q1Order')
    const q1Delivery = document.querySelector('#q1Delivery')
    const q1Name = document.querySelectorAll('.q1Name')
    const q1Address = document.querySelectorAll('.q1Address')
    const same = document.querySelector('#q1Same')
    same.addEventListener('click', function(event){
    if(same.checked == true){
        q1Name[1].value = q1Name[0].value
        q1Address[1].value = q1Address[0].value
        // q1Delivery.querySelector('.q1Name').value = q1Order.querySelector('.q1Name').value
        // q1Delivery.querySelector('.q1Address').value = q1Order.querySelector('.q1Address').value
        } else {
            q1Delivery.querySelector('.q1Name').value = ''
            q1Delivery.querySelector('.q1Address').value = ''
        }
    })
    // 문제 2 : 로그인창
    // 로그인 버튼 눌렀을 때
    // 아이디 / 비밀번호 없으면 빨간 글씨 나오게
    // 단, 아이디/비밀번호를 쓰고 로그인을 누르면 빨간 글씨 지우기
    const login = document.querySelector('#login')
    login.addEventListener('click', function(){
        const id = document.querySelector('#id')
        const pw = document.querySelector('#pw')
        const warning = document.querySelector('.warning')
        console.log(id.value)
        console.log(pw.value)

        // id를 적었는지 판단
        if(id.value.trim() == ''){
            console.log('아이디는 필수입니다')
            warning.innerText = '아이디는 필수입니다'
        }
        // 비밀번호를 적었는지 판단
        else if(pw.value.trim() == ''){
            console.log('비밀번호는 필수입니다')
            warning.innerText = '비밀번호는 필수입니다'
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
    const q3Pizza = document.querySelector('select[name="q3Pizza"]')
    // 선택 결과를 출력하는 버튼
    const q3Button = document.querySelector('#q3Button')

    // 각각의 결과를 출력할 div
    // 클래스가 2개인 요소는 클래스 사이를 띄우지 않고 붙여서 선택
    // 예: class="q3Result pizza" → '.q3Result.pizza'
    const resultPizza = document.querySelector('.q3Result.pizza')
    const resultSize = document.querySelector('.q3Result.size')
    const resultDow = document.querySelector('.q3Result.dow')
    const resultTopping = document.querySelector('.q3Result.topping')
    const resultPrice = document.querySelector('.q3Result.price')

    // 출력 버튼을 클릭했을 때 주문 내역을 확인
    q3Button.addEventListener('click', function(event) {

    // 1. 피자 종류 출력
    resultPizza.innerText = `피자: ${q3Pizza.value}`

    // 2. 사이즈 (단일 선택)
    // :checked를 사용하면 같은 name을 가진 라디오 버튼 중
    // 현재 선택된 요소 하나만 가져올 수 있음
    const checkedSize = document.querySelector('input[name="q3Size"]:checked')
    // 사이즈 가격을 저장할 변수
    let sizePrice = 0
    
    // 라디오 버튼을 감싸는 부모 label의 글자를 가져옴
    // trim()은 글자 앞뒤의 불필요한 공백과 줄바꿈을 제거
    resultSize.innerText = `사이즈: ${checkedSize.parentElement.innerText.trim()}`
    // input의 value는 문자열이므로 가격 계산을 위해 숫자로 변환
    sizePrice = parseInt(checkedSize.value) // value에 있는 가격을 숫자로 변환 (총액 계산용)

    // 3. 도우 (단일 선택)
    // 사이즈와 마찬가지로 :checked를 사용해서
    // 선택된 도우 라디오 버튼 하나만 가져옴
    const checkedDow = document.querySelector('input[name="q3Dow"]:checked')
    // 도우는 value에 이름이 들어 있으므로 바로 출력
    resultDow.innerText = `도우: ${checkedDow.value}`

    // 4. 토핑 (다중 선택)
    // 체크박스는 여러 개를 동시에 선택할 수 있으므로
    // querySelectorAll()로 선택된 체크박스를 모두 가져옴
    const checkedToppings = document.querySelectorAll('.q3Topping input[type="checkbox"]:checked');
    // 선택된 토핑 이름들을 저장할 배열
    let toppingNames = []
    // 선택된 토핑 가격의 합계를 저장할 변수
    let toppingPrice = 0

     // 선택된 토핑 체크박스를 하나씩 반복
    checkedToppings.forEach(function(checkbox) {
        // 체크박스를 감싸는 label의 글자를 배열에 추가
        toppingNames.push(checkbox.parentElement.innerText.trim()) // 텍스트 추출
        // value의 가격을 숫자로 변환한 뒤 기존 가격에 더함
        toppingPrice += parseInt(checkbox.value) // 토핑 가격 누적
    })

    // 선택된 토핑이 하나 이상 있으면
    // join(', ')으로 배열의 항목들을 쉼표로 연결
    if (toppingNames.length > 0) {
        resultTopping.innerText = `토핑: ${toppingNames.join(', ')}`
    } else {
        resultTopping.innerText = `토핑: 선택안함`
    }

    // + 문제3-2 : 선택 내역과 총액 출력
    // 5. 총액 계산 (문제 3-2)
    const totalPrice = sizePrice + toppingPrice;
    resultPrice.innerText = `총액: ${totalPrice}원`
    })



    // 문제 4 : 메뉴 선택
    // 인기상품순, 낮은가격순, 높은가격순, 신상품순, 상품평 많은순
    // + 클릭한 것만 굵은 글씨로 유지


    // 문제 5 : Todo List
    // 할일을 적는 input, 추가 버튼

    // + 5-1 : 추가버튼 누르면 체크박스와 할일이 하단에 추가된다
    // + 5-2 : 개별 삭제 버튼이 있고, 클릭 시 그 줄이 지워진다 (dom.remove())
    // + 5-3 : 전체 선택 checkbox가 있고
    //         전체 선택 체크 시 : 모든 checkbox 체크
    //         해제 시 : 모든 checkbox 체크 해제
    // + 5-4 : 전체 선택 후 하나라도 개별 해제가 되면 전체 선택도 해제
    //         개별로 모두 체크한 경우 전체 선택도 체크된다
    // + 5-5 : 선택 삭제 버튼 클릭 시 선택된 내용만 삭제
}