const filters = document.querySelectorAll('[data-filter]');
const cards = document.querySelectorAll('.project-card[data-category]');
const announcement = document.querySelector('#filter-status');
const counts = { all: 'six', analytics: 'one', ai: 'one', research: 'two', engineering: 'two' };

filters.forEach(button => {
  button.addEventListener('click', () => {
    const selected = button.dataset.filter;
    filters.forEach(other => {
      const active = other === button;
      other.classList.toggle('is-active', active);
      other.setAttribute('aria-pressed', String(active));
    });
    cards.forEach(card => {
      card.hidden = selected !== 'all' && card.dataset.category !== selected;
    });
    announcement.textContent = selected === 'all'
      ? 'Showing all six projects.'
      : `Showing ${counts[selected]} ${selected} project${counts[selected] === 'one' ? '' : 's'}.`;
  });
});

const year = document.querySelector('#year');
if (year) year.textContent = String(new Date().getFullYear());
