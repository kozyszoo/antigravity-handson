/**
 * AI Coffee Shop - メインスクリプト
 * Vibe Coding Demo
 */

// ==================================
// スムーススクロール
// ==================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ==================================
// スクロールアニメーション（フェードイン）
// ==================================
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const fadeInObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            fadeInObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

// 監視対象の要素を登録
document.querySelectorAll('.feature-card, .menu-item').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    fadeInObserver.observe(el);
});

// フェードイン時のスタイル
document.head.insertAdjacentHTML('beforeend', `
    <style>
        .feature-card.visible,
        .menu-item.visible {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    </style>
`);

// ==================================
// 予約ボタンのクリックイベント
// ==================================
document.querySelectorAll('.btn--primary').forEach(btn => {
    btn.addEventListener('click', function (e) {
        // デモ用: 実際の予約機能は未実装
        if (this.textContent.includes('予約')) {
            e.preventDefault();
            alert('🎉 ご予約ありがとうございます！\n（これはデモです）');
        }
    });
});

// ==================================
// コンソールログ（開発者向け）
// ==================================
console.log('%c☕ AI Coffee Shop', 'font-size: 24px; font-weight: bold; color: #6366f1;');
console.log('%cBuilt with ❤️ and Antigravity', 'color: #64748b;');
