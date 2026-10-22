const details = [...document.querySelectorAll('details')];
document.querySelector('#expand-all').addEventListener('click', () => details.forEach(d => {d.open = true;}));
document.querySelector('#collapse-all').addEventListener('click', () => details.forEach(d => {d.open = false;}));
function revealTarget() {
  const target = document.getElementById(location.hash.slice(1));
  if (!target) return;
  for (let node = target; node; node = node.parentElement) {
    if (node.tagName === 'DETAILS') node.open = true;
  }
  requestAnimationFrame(() => target.scrollIntoView({block: 'start'}));
}
addEventListener('hashchange', revealTarget);
revealTarget();
