// 滚动动画
window.addEventListener('scroll', function () {
    const cards = document.querySelectorAll('.command-card');
    cards.forEach(card => {
        const rect = card.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom >= 0) {
            card.classList.add('visible');
        } else {
            card.classList.remove('visible');
        }
    });
});

// 鼠标交互动画
const cards = document.querySelectorAll('.command-card');
cards.forEach(card => {
    card.addEventListener('mouseenter', function () {
        this.style.transform = 'translateY(-5px) scale(1.05)';
    });
    card.addEventListener('mouseleave', function () {
        this.style.transform = 'translateY(0) scale(1)';
    });
});

// 为每个卡片添加动画延迟
document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.command-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.2}s`;
    });
});
    