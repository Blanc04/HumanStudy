/*
    ============================================================
    15_event 복습 핵심
    ============================================================
    1. HTML 요소를 찾는 시점과 window.onload의 관계
    2. onclick과 addEventListener()의 차이
    3. removeEventListener()가 동작하기 위한 조건
    4. 입력값 검사와 배열을 이용한 경고문 만들기
    5. keyup 이벤트와 event 객체
    6. 스크롤 이벤트와 키보드로 요소 이동시키기

    이 파일은 원본 실행 코드를 변경하지 않고
    공부용 설명 주석만 추가한 버전이다.
*/
console.log('hello js')


/*
    현재 스크립트가 실행되는 즉시 #btn1을 찾는다.

    스크립트가 HTML의 #btn1보다 먼저 실행되면 아직 요소가 만들어지지 않아
    btn1에는 null이 들어갈 수 있다. 이 차이를 아래 window.onload 예제와 비교한다.
*/
const btn1 = document.querySelector('#btn1')
console.log(1, 'btn1', btn1)

// window는 현재 브라우저 창을 나타내는 최상위 객체이다.
console.log(window)

// 페이지 로딩 이벤트가 발생하면~

// window.onload = function(){
//     const btn1 = document.querySelector('#btn1')
//     console.log(2, 'btn1', btn1)
// }
/*
    init 함수는 페이지의 모든 자원이 로드된 뒤 실행할 초기화 함수이다.
    이 시점에는 일반적으로 HTML 요소 생성이 완료되어 querySelector가 안전하다.
*/
function init(){
    const btn1 = document.querySelector('#btn1')
    console.log(2, 'btn1', btn1)
    /*
        element.style은 HTML 태그의 style 속성에 직접 적힌 인라인 스타일만 읽는다.
        CSS 파일이나 <style>에서 지정된 최종값까지 읽으려면 getComputedStyle()을 사용한다.
    */
    const game = document.querySelector('#game')
    console.log(game.style.left)
    // 실제 이벤트 연결 작업을 bind 함수에 맡긴다.
    bind()
}
/*
    onload 프로퍼티에 init 함수 자체를 저장한다.
    init()처럼 괄호를 붙이면 지금 즉시 실행한 결과를 저장하게 되므로 의미가 달라진다.

    window.onload 방식은 나중에 다른 함수를 다시 대입하면 기존 함수가 덮어써진다.
*/
window.onload = init

/*
    addEventListener('load', init)은 load 이벤트에 함수를 추가하는 방식이다.
    같은 load 이벤트에 여러 리스너를 등록할 수 있다는 점이 onload와 다르다.
*/
// window.addEventListener('load', init)

// 페이지에서 사용할 여러 이벤트를 한곳에서 연결하는 함수이다.
function bind(){
    // load 이후이므로 여기서는 #btn1 요소를 다시 안전하게 가져온다.
    const btn1 = document.querySelector('#btn1')
    /*
        onclick 프로퍼티에는 클릭 함수 하나만 저장할 수 있다.
        아래에서 onclick에 다시 함수를 대입하므로 이 첫 번째 함수는 덮어써진다.
    */
    btn1.onclick = function(){
        console.log('btn1 클릭')
    }
    /*
        같은 onclick 프로퍼티에 새 함수를 대입한다.
        따라서 btn1 클릭 시 'btn1 클릭'은 나오지 않고 'btn1 click'만 출력된다.
    */
    btn1.onclick = function(){
        console.log('btn1 click')
    }
    // addEventListener : 동일한 이벤트에 여러 함수 추가 가능
    /*
        addEventListener()는 동일한 이벤트에 여러 리스너를 누적해서 등록할 수 있다.
        btn2를 한 번 클릭하면 아래 두 함수가 등록된 순서대로 모두 실행된다.
    */
    const btn2 = document.querySelector('#btn2')
    btn2.addEventListener('click', function(){
        console.log('btn2 클릭')
    })
    btn2.addEventListener('click', function(){
        console.log('btn2 click')
    })

    // btn4 요소에 연결할 함수는 아래에 선언된 btn4click이다.
    const btn4 = document.querySelector('#btn4')
    /*
    함수 호출 결과가 아니라 함수 자체를 전달한다.
    btn4click()이 아니라 btn4click이라고 적는 것이 핵심이다.
    */
    btn4.addEventListener('click', btn4click)
    // removeEventListener
    // 이벤트 제거
    // 단, 익명함수는 제거 못함
    /*
        방금 등록한 것과 동일한 이벤트 종류('click')와
        동일한 함수 참조(btn4click)를 전달했으므로 이벤트가 제거된다.

        이 줄이 즉시 실행되기 때문에 결과적으로 btn4를 클릭해도 아무 일도 일어나지 않는다.
        익명 함수는 제거가 절대 불가능한 것이 아니라,
        등록할 때 사용한 동일한 함수 참조를 다시 전달하기 어려운 것이 문제다.
    */
    btn4.removeEventListener('click', btn4click)

    // 로그인 버튼을 클릭했을 때 아이디와 비밀번호의 빈칸을 검사한다.
    const login = document.querySelector('#login')
    login.addEventListener('click', function(){
        // 클릭 시점의 입력 요소와 경고 출력 요소를 가져온다.
        const id = document.querySelector('#id')
        const pw = document.querySelector('#pw')
        const warning = document.querySelector('.warning')
        // input의 value 프로퍼티에는 사용자가 입력한 문자열이 들어 있다.
        console.log(id.value)
        console.log(pw.value)

        // id를 적었는지 판단
        // if(id.value.trim() == ''){
        //     console.log('아이디는 필수입니다')
        //     warning.innerText = '아이디는 필수입니다'
        // }
        // 비밀번호를 적었는지 판단
        // else if(pw.value.trim() == ''){
        //     console.log('비밀번호는 필수입니다')
        //     warning.innerText = '비밀번호는 필수입니다'
        // }
        /*
            비어 있는 항목의 이름을 모아둘 배열이다.
            아이디와 비밀번호가 둘 다 비었을 때 두 항목을 한 문장으로 출력할 수 있다.
        */
        const blankList = []
        // trim()으로 앞뒤 공백을 제거한 뒤 빈 문자열인지 검사한다.
        if(id.value.trim() == ''){
        // 아이디가 비어 있으면 배열 끝에 '아이디'를 추가한다.
            blankList.push('아이디')
        }
        // 비밀번호도 별도로 검사하므로 두 입력칸을 동시에 안내할 수 있다.
        if(pw.value.trim() == ''){
            blankList.push('비밀번호')
        }
        // 배열에 하나라도 항목이 들어 있으면 입력하지 않은 값이 있다는 뜻이다.
        if(blankList.length > 0){
        /*
            join(', ')은 배열 요소를 ', '로 연결한다.
            예: ['아이디', '비밀번호'] → '아이디, 비밀번호'
        */
            const message = `${blankList.join(', ')}는 필수입니다`
            console.log(message)
            warning.innerText = message
        // 빈칸이 하나도 없으면 이전에 표시했던 경고 문구를 지운다.
        } else {
            warning.innerText = ''
        }
    })
    /*
        id 입력칸에서 키를 눌렀다가 뗄 때 keyup 이벤트가 발생한다.
        event에는 어떤 키가 눌렸는지와 Ctrl/Shift/Alt 상태 등이 들어 있다.
    */
    document.querySelector('#id').addEventListener('keyup', function(event){
        // log('keyup발생')
        // console.log(event)
        // log('key:'+ event.key)
        /*
            keyCode는 키의 숫자 코드를 제공하지만 현재는 권장되지 않는 방식이다.
            최신 코드에서는 event.key === 'Enter' 또는 event.code를 주로 사용한다.
            다만 이 수업 코드는 keyCode 동작을 공부하기 위한 예제이다.
        */
        log('keyCode:'+ event.keyCode)
        // log('shiftKey:'+ event.shiftKey)
        // log('ctrlKey:'+ event.ctrlKey)
        // log('altKey:'+ event.altKey)
        // keyCode 13은 Enter 키이다.
        if(event.keyCode == 13){
            log('엔터 빵')
        // focus()를 호출하면 입력 커서가 비밀번호 칸으로 이동한다.
            const pw = document.querySelector('#pw')
            pw.focus()
        }
        // Ctrl 키가 눌린 상태이고 keyCode가 67(C)이면 Ctrl+C 조합이다.
        if(event.ctrlKey && event.keyCode == 67){ // ctrl + c
            alert('어딜 복사하려고?')
        }
    })
    // document.querySelector('#id').addEventListener('keydown', function(event){
    //     log('keydown 발생')
    //     console.log(event)
    // })
    // 비밀번호 입력칸에서도 키를 뗄 때마다 아래 함수가 실행된다.
    document.querySelector('#pw').addEventListener('keyup', function(event){
        // 비밀번호 칸에서 Enter를 누르면 로그인 버튼 클릭을 코드로 발생시킨다.
        if(event.keyCode == 13){
            log('로그인 시도')
            const login = document.querySelector('#login')
        // click()은 사용자가 실제로 클릭한 것처럼 login의 click 이벤트를 실행한다.
            login.click()
        }
        if(event.ctrlKey && event.keyCode == 67){ // ctrl + c
            alert('어딜 복사하려고?')
        }
    })
    // #top 요소를 클릭하면 문서 맨 위로 부드럽게 이동한다.
    document.querySelector('#top').addEventListener('click', function(event){
        // documentElement.scrollTop은 문서가 세로로 얼마나 스크롤됐는지 나타낸다.
        console.log(document.documentElement.scrollTop)
        // document.documentElement.scrollTop = 0
        //부드럽게 스크롤 올리기
        /*
            window.scrollTo()로 스크롤 위치를 변경한다.
            top: 0은 문서 최상단, behavior: 'smooth'는 부드러운 이동을 뜻한다.
        */
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        })
    })
    // 창을 스크롤할 때마다 현재 세로 스크롤 위치를 출력한다.
    window.addEventListener('scroll', function(){
        console.log('window.scrollY', window.scrollY)
    })
    /*
        body에서 발생하거나 body까지 버블링된 keydown 이벤트를 처리한다.
        키를 누르고 있는 동안 브라우저의 키 반복에 따라 여러 번 실행될 수 있다.
    */
    document.querySelector('body').addEventListener('keydown', function(event){
        log(event.keyCode)
        // 움직일 #game 요소를 찾는다.
        const game = document.querySelector('#game')
        /*
            getComputedStyle(game)은 최종 계산된 CSS 스타일 객체를 반환한다.
            현재 left 변수는 이후 코드에서 사용되지 않는 실습용 변수이다.
        */
        const left = getComputedStyle(game)
        // keyCode 39는 오른쪽 방향키이다.
        if(event.keyCode == 39){  // 오른쪽
            /*
                getComputedStyle(game).left는 '10px' 같은 문자열이므로 parseInt로 숫자만 얻는다.
                left 값이 'auto'라면 parseInt 결과가 NaN이 될 수 있어 CSS 초기 위치가 필요하다.
            */
            const currentLeft = parseInt(getComputedStyle(game).left)
            // 현재 위치에 5를 더한 뒤 다시 'px' 단위를 붙여 인라인 스타일로 저장한다.
            game.style.left = (currentLeft + 5) + 'px'
        }
    })
}

// HTML의 onclick 속성 등에서 사용할 수 있는 일반 함수 예제이다.
function btn3click(){
    console.log('btn3 click')
}

// btn4에 등록했다가 바로 제거한 클릭 함수이다.
function btn4click(){
    console.log('btn4 click')
}

/*
    전달받은 내용을 #view 영역의 맨 위에 로그로 추가하는 공통 함수이다.
    prepend()를 사용하므로 최신 로그가 위에 표시된다.
*/
function log(message){
    // 메모리에 새로운 div 요소를 만든다. 아직 화면에는 붙지 않은 상태이다.
    const div = document.createElement('div')
    // 생성한 div에 log 클래스를 추가한다.
    div.classList.add('log')
    /*
        innerHTML은 문자열을 HTML로 해석한다.
        외부에서 받은 값을 그대로 넣을 때는 보안 문제가 생길 수 있으므로
        단순 글자 출력만 필요하면 textContent가 더 안전하다.
    */
    div.innerHTML = message
    // 로그가 들어갈 부모 요소 #view를 찾는다.
    const view = document.querySelector('#view')
    // 새 로그 div를 #view의 첫 번째 자식 위치에 삽입한다.
    view.prepend(div)
}
