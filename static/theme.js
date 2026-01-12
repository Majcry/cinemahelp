const toggle = document.getElementById('themeToggle');
const title = document.getElementById('title');

function setTheme(isDark) {
    if (isDark) {
        document.body.classList.add('dark');
        title.src = logoDark;
        localStorage.setItem('theme', 'dark');
    } else {
        document.body.classList.remove('dark');
        title.src = logoLight;
        localStorage.setItem('theme', 'light');
    }
}

if (localStorage.getItem('theme') === 'dark') {
    setTheme(true);
}else{
    setTheme(false);
}

toggle.addEventListener('click', () => {
    const isDark = document.body.classList.contains('dark');
    setTheme(!isDark);
});