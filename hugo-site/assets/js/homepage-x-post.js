(() => {
  const posts = document.querySelectorAll('[data-x-post-id]');
  if (!posts.length) return;

  let widgetsPromise;
  function loadWidgets() {
    if (window.twttr?.widgets?.createTweet) return Promise.resolve(window.twttr);
    if (widgetsPromise) return widgetsPromise;
    widgetsPromise = new Promise((resolve, reject) => {
      let script = document.getElementById('twitter-wjs');
      const ready = () => {
        if (window.twttr?.widgets?.createTweet) resolve(window.twttr);
        else if (window.twttr?.ready) window.twttr.ready(resolve);
        else reject(new Error('X widgets unavailable'));
      };
      const isNew = !script;
      if (isNew) {
        script = document.createElement('script');
        script.id = 'twitter-wjs';
        script.async = true;
        script.src = 'https://platform.x.com/widgets.js';
      }
      script.addEventListener('load', ready, { once: true });
      script.addEventListener('error', () => reject(new Error('X widgets blocked')), { once: true });
      if (isNew) document.head.appendChild(script);
    });
    return widgetsPromise;
  }

  async function render(post) {
    if (post.dataset.xPostState) return;
    post.dataset.xPostState = 'loading';
    const target = post.querySelector('.home-x-post-widget');
    const fallback = post.querySelector('.home-x-post-fallback');
    try {
      const twttr = await loadWidgets();
      const widget = await twttr.widgets.createTweet(post.dataset.xPostId, target, {
        conversation: 'none',
        dnt: true,
        theme: 'dark',
        lang: 'en',
        width: Math.min(550, Math.max(250, Math.floor(post.getBoundingClientRect().width))),
      });
      if (!widget) throw new Error('X post unavailable');
      fallback.hidden = true;
      post.dataset.xPostState = 'rendered';
    } catch {
      target.replaceChildren();
      fallback.hidden = false;
      post.dataset.xPostState = 'fallback';
    }
  }

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        observer.unobserve(entry.target);
        render(entry.target);
      });
    }, { rootMargin: '400px 0px' });
    posts.forEach((post) => observer.observe(post));
  } else {
    posts.forEach(render);
  }
})();
