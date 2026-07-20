console.log('hello js')


const btn1 = document.querySelector('#btn1')
console.log(1, 'btn1', btn1)

console.log(window)

// 페이지 로딩 이벤트가 발생하면~

// window.onload = function(){
//     const btn1 = document.querySelector('#btn1')
//     console.log(2, 'btn1', btn1)
// }
function init(){
    const btn1 = document.querySelector('#btn1')
    console.log(2, 'btn1', btn1)
    const game = document.querySelector('#game')
    console.log(game.style.left)
    bind()
}
window.onload = init

// window.addEventListener('load', init)

function bind(){
    const btn1 = document.querySelector('#btn1')
    btn1.onclick = function(){
        console.log('btn1 클릭')
    }
    btn1.onclick = function(){
        console.log('btn1 click')
    }
    // addEventListener : 동일한 이벤트에 여러 함수 추가 가능
    const btn2 = document.querySelector('#btn2')
    btn2.addEventListener('click', function(){
        console.log('btn2 클릭')
    })
    btn2.addEventListener('click', function(){
        console.log('btn2 click')
    })

    const btn4 = document.querySelector('#btn4')
    btn4.addEventListener('click', btn4click)
    // removeEventListener
    // 이벤트 제거
    // 단, 익명함수는 제거 못함
    btn4.removeEventListener('click', btn4click)

    const login = document.querySelector('#login')
    login.addEventListener('click', function(){
        const id = document.querySelector('#id')
        const pw = document.querySelector('#pw')
        const warning = document.querySelector('.warning')
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
        const blankList = []
        if(id.value.trim() == ''){
            blankList.push('아이디')
        }
        if(pw.value.trim() == ''){
            blankList.push('비밀번호')
        }
        if(blankList.length > 0){
            const message = `${blankList.join(', ')}는 필수입니다`
            console.log(message)
            warning.innerText = message
        } else {
            warning.innerText = ''
        }
    })
    document.querySelector('#id').addEventListener('keyup', function(event){
        // log('keyup발생')
        // console.log(event)
        // log('key:'+ event.key)
        log('keyCode:'+ event.keyCode)
        // log('shiftKey:'+ event.shiftKey)
        // log('ctrlKey:'+ event.ctrlKey)
        // log('altKey:'+ event.altKey)
        if(event.keyCode == 13){
            log('엔터 빵')
            const pw = document.querySelector('#pw')
            pw.focus()
        }
        if(event.ctrlKey && event.keyCode == 67){ // ctrl + c
            alert('어딜 복사하려고?')
        }
    })
    // document.querySelector('#id').addEventListener('keydown', function(event){
    //     log('keydown 발생')
    //     console.log(event)
    // })
    document.querySelector('#pw').addEventListener('keyup', function(event){
        if(event.keyCode == 13){
            log('로그인 시도')
            const login = document.querySelector('#login')
            login.click()
        }
        if(event.ctrlKey && event.keyCode == 67){ // ctrl + c
            alert('어딜 복사하려고?')
        }
    })
    document.querySelector('#top').addEventListener('click', function(event){
        console.log(document.documentElement.scrollTop)
        // document.documentElement.scrollTop = 0
        //부드럽게 스크롤 올리기
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        })
    })
    window.addEventListener('scroll', function(){
        console.log('window.scrollY', window.scrollY)
    })
    document.querySelector('body').addEventListener('keydown', function(event){
        log(event.keyCode)
        const game = document.querySelector('#game')
        const left = getComputedStyle(game)
        if(event.keyCode == 39){  // 오른쪽
            const currentLeft = parseInt(getComputedStyle(game).left)
            game.style.left = (currentLeft + 5) + 'px'
        }
    })
}

function btn3click(){
    console.log('btn3 click')
}

function btn4click(){
    console.log('btn4 click')
}

function log(message){
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message
    const view = document.querySelector('#view')
    view.prepend(div)
}
