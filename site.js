const frame = document.querySelector('#demo');
const pause = document.querySelector('#pause');
let userPaused = matchMedia('(prefers-reduced-motion: reduce)').matches;
let visible = true;
function update() {
  pause.textContent = userPaused ? '再生' : '一時停止';
  pause.setAttribute('aria-pressed', String(userPaused));
  frame.contentWindow.postMessage({type: 'demo-pause', paused: userPaused || !visible || document.hidden}, location.origin);
}
pause.addEventListener('click', () => {userPaused = !userPaused; update();});
frame.addEventListener('load', update);
document.addEventListener('visibilitychange', update);
new IntersectionObserver(([entry]) => {visible = entry.isIntersecting; update();}, {threshold: 0.05}).observe(frame);
update();
document.querySelector('#copy').addEventListener('click', async () => {
  const status = document.querySelector('#copy-status');
  try {
    await navigator.clipboard.writeText(document.querySelector('#prompt').textContent);
    status.textContent = 'コピーしました';
  } catch {
    status.textContent = 'テキストを選択してコピーしてください';
  }
});
