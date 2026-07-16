'use strict';

const dropdowns = document.querySelectorAll('.nav-dropdown');

function closeAllDropdowns(exceptDropdown = null) {
    dropdowns.forEach((dropdown) => {
        if (dropdown !== exceptDropdown) {
            dropdown.classList.remove('is-open');
            dropdown.querySelector('.nav-dropdown-button')?.setAttribute('aria-expanded', 'false');
        }
    });
}

dropdowns.forEach((dropdown) => {
    const button = dropdown.querySelector('.nav-dropdown-button');

    if (!button) {
        return;
    }

    button.addEventListener('click', () => {
        const willOpen = !dropdown.classList.contains('is-open');
        closeAllDropdowns(dropdown);
        dropdown.classList.toggle('is-open', willOpen);
        button.setAttribute('aria-expanded', String(willOpen));
    });
});

document.addEventListener('click', (event) => {
    if (!(event.target instanceof Element) || !event.target.closest('.nav-dropdown')) {
        closeAllDropdowns();
    }
});

document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        closeAllDropdowns();
        document.activeElement?.blur();
    }
});


const loginForm = document.querySelector('.login-form');

if (loginForm) {
    loginForm.addEventListener('submit', (event) => {
        event.preventDefault();
    });
}
