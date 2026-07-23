/*
    ============================================================
    16_event_mouse 복습 핵심
    ============================================================
    1. 우클릭·드래그 선택·복사 이벤트 제어
    2. 마우스 클릭 관련 이벤트의 발생 순서
    3. offset/page/client/screen 좌표의 차이
    4. mouseover/out과 mouseenter/leave의 차이
    5. 마우스를 따라다니는 요소와 직접 드래그 구현
    6. resize 이벤트로 브라우저 내부 크기 확인

    이 파일은 원본 실행 코드를 변경하지 않고
    공부용 설명 주석만 추가한 버전이다.

    아래 세 변수는 드래그 기능에서 여러 이벤트가 함께 사용하는 상태값이다.
*/
let _isDrag = false
// 이미지 안에서 누른 지점과 이미지 왼쪽 사이의 가로 거리이다.
let _offsetX = 0
// 이미지 안에서 누른 지점과 이미지 위쪽 사이의 세로 거리이다.
let _offsetY = 0

// 로그 내용을 #view의 맨 위에 추가하는 공통 함수이다.
function log(message){
    const div = document.createElement('div')
    div.classList.add('log')
    /*
        innerHTML은 문자열을 HTML로 해석한다.
        message가 DOM 객체라면 문자열 변환 결과가 표시될 수 있다.
    */
    div.innerHTML = message
    const view = document.querySelector('#view')
    view.prepend(div)
}

// 페이지 로드가 끝나면 이벤트 연결 함수 bind를 실행한다.
window.onload = function(){
    bind()
}

// 이 페이지에서 사용할 마우스 관련 이벤트를 한곳에서 등록한다.
function bind(){
    // 우클릭과 선택을 막을 첫 번째 영역을 가져온다.
    const area = document.querySelector('#area')
    /*
        contextmenu 이벤트는 보통 마우스 오른쪽 버튼 메뉴가 열리기 직전에 발생한다.
        oncontextmenu에 화살표 함수를 저장한다.
    */
    area.oncontextmenu = () =>{
        alert('오른쪽 버튼 금지입니다')
    /*
        이벤트 핸들러 프로퍼티 방식에서 false를 반환하면
        기본 컨텍스트 메뉴가 열리는 동작을 취소한다.
    */
        return false
    }

    // selectstart는 사용자가 글자 선택을 시작할 때 발생한다.
    area.onselectstart = function(){
        // false를 반환해 해당 영역의 기본 글자 선택 동작을 막는다.
        return false
    }
    // area DOM 객체를 log에 전달한다. 보통 문자열로 변환되어 표시된다.
    log(area)

    // 복사와 여러 마우스 이벤트를 실습할 두 번째 영역이다.
    const area2 = document.querySelector('#area2')
    // area2 안에서 복사 동작이 발생하면 실행된다.
    area2.addEventListener('copy', function(event){
        // 브라우저가 선택 내용을 그대로 복사하는 기본 동작을 취소한다.
        event.preventDefault()

        // 현재 문서에서 사용자가 드래그해 선택한 글자를 문자열로 얻는다.
        const selection = window.getSelection().toString()
        console.log(selection)
        // 선택한 글자가 없다면 더 처리하지 않고 함수를 끝낸다.
        if(selection.length == 0){
            return
        }
        // 선택한 글자 뒤에 붙일 출처 문자열이다.
        const str = '[출처] www.naver.com'
        // 실제 클립보드에 저장할 최종 문자열을 만든다.
        const result = selection + str
        
        // 클립보드의 text/plain 형식에 직접 만든 문자열을 저장한다.
        event.clipboardData.setData('text/plain', result)
    })

    // dblclick은 짧은 시간 안에 같은 위치를 두 번 클릭했을 때 발생한다.
    area2.addEventListener('dblclick', function(){
        log('더블클릭 발생')
    })
    /*
        일반적인 마우스 클릭 순서:
        mousedown → mouseup → click
        빠르게 두 번 클릭하면 마지막에 dblclick도 추가로 발생한다.
    */
    area2.addEventListener('mousedown', function(){
        log('mousedown')
    })
    area2.addEventListener('mouseup', function(){
        log('mouseup')
    })
    // click 이벤트 객체의 여러 Y 좌표를 비교한다.
    area2.addEventListener('click', function(evt){
        log('click')

    /*
        좌표 기준을 정확히 정리하면 다음과 같다.

        offsetY : 이벤트 대상 요소의 내부 좌표 기준
        pageY   : 스크롤을 포함한 전체 문서 좌상단 기준
        clientY : 현재 보이는 브라우저 화면(viewport) 좌상단 기준
        screenY : 실제 모니터 화면 좌상단 기준

        따라서 원본의 'offset: DOM 최상단 기준' 설명보다는
        '이벤트 대상 요소 내부 기준'이라고 이해하는 편이 정확하다.
    */
        /* 
            offset : DOM 최상단 기준
            page : 스크롤에 관계없이 문서 좌상단 기준

            client : 지금 딱 보이는 브라우저 좌상단 기준
            screen : 실제 모니터 좌상단 기준
        */
        log('offsetY :'+ evt.offsetY)
        log('pageY :'+ evt.pageY)
        log('clientY :'+ evt.clientY)
        log('screenY :'+ evt.screenY)
    })

    /*
        mouseenter는 자식 요소로 이동할 때 다시 발생하지 않고 버블링하지 않는다.
        mouseover는 자식 요소 위로 들어갈 때도 발생할 수 있으며 버블링한다.
    */
    // area2.addEventListener('mouseenter', function(evt){
    // 현재 코드는 mouseover를 사용하므로 자식 요소 때문에 여러 번 발생할 수 있다.
    area2.addEventListener('mouseover', function(evt){
        // log('mouseover')
        // 마우스가 들어오면 area2의 배경색을 salmon으로 바꾼다.
        area2.style.backgroundColor = 'salmon'
    })
    /*
        mouseleave는 영역 전체에서 완전히 나갈 때 발생하고 버블링하지 않는다.
        mouseout은 자식 요소로 이동할 때도 발생할 수 있으며 버블링한다.
    */
    // area2.addEventListener('mouseleave', function(evt){
    // 현재 코드는 mouseout을 사용하므로 자식 요소 이동에도 반응할 수 있다.
    area2.addEventListener('mouseout', function(evt){
        // log('mouseout')
        area2.style.backgroundColor = 'white'
    })
    // mousemove는 영역 안에서 마우스가 움직일 때 매우 자주 발생한다.
    area2.addEventListener('mousemove', function(evt){
        // log('mousemove')
        // log(`offsetX: ${evt.offsetX}, offsetY: ${evt.offsetY}`)
    })

/*
    body 위에서 마우스가 움직일 때마다 #game 요소를 마우스 위치로 이동시킨다.
    아래쪽에도 body의 mousemove 리스너가 하나 더 있으므로 두 함수가 모두 실행된다.
*/
    document.querySelector('body').addEventListener('mousemove', function(evt){
        const game = document.querySelector('#game')

        // pageX/pageY를 사용하므로 문서 전체 좌표를 기준으로 배치한다.
        game.style.left = evt.pageX+1 + 'px'
        game.style.top = evt.pageY+1 + 'px'

        // log(`X:${evt.offsetX}, Y:${evt.offsetY}`)
    })

/*
    이미지에서 마우스 버튼을 누르면 드래그 시작 상태로 바꾼다.
    눌렀던 지점의 offset을 기억해야 이미지가 갑자기 모서리에 붙지 않는다.
*/
    document.querySelector('#img').addEventListener('mousedown', function(evt){
        // true이면 현재 드래그 중이라는 뜻이다.
        _isDrag = true
        // 이미지 내부에서 클릭한 가로 위치를 저장한다.
        _offsetX = evt.offsetX
        // 이미지 내부에서 클릭한 세로 위치를 저장한다.
        _offsetY = evt.offsetY
    })
/*
    이미지 위에서 마우스 버튼을 놓으면 드래그를 끝낸다.

    주의: 현재 코드는 mouseup이 #img에만 등록되어 있다.
    이미지 밖에서 버튼을 놓으면 mouseup이 잡히지 않아 _isDrag가 true로 남을 수 있다.
    원본 동작은 유지하고 위험 지점만 주석으로 표시했다.
*/
    document.querySelector('#img').addEventListener('mouseup', function(evt){
        _isDrag = false
    })
    // 드래그 중인 이미지가 body 전체의 마우스 이동을 따라가게 한다.
    document.querySelector('body').addEventListener('mousemove', function(evt){
        const img = document.querySelector('#img')
        // 마우스를 누른 상태일 때만 이미지 위치를 갱신한다.
        if(_isDrag){
    /*
        마우스의 문서 좌표에서 처음 누른 이미지 내부 좌표를 뺀다.
        이 계산 덕분에 처음 잡은 지점이 마우스 아래에 계속 유지된다.
    */
        img.style.left = (evt.pageX-_offsetX) + 'px'
        img.style.top = (evt.pageY-_offsetY) + 'px'
        }
    })

    // 브라우저 창 크기가 바뀔 때 resize 이벤트가 발생한다.
    window.addEventListener('resize', function(evt){
    // innerWidth는 스크롤바 등을 제외한 브라우저 콘텐츠 영역의 너비이다.
        const w = window.innerWidth
    // innerHeight는 브라우저 콘텐츠 영역의 높이이다.
        const h = window.innerHeight

        log(`w:${w}, h:${h}`)
    })
}
