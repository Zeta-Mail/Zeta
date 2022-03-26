function showContetn() {
  const emailRow = document.getElementById('emailR'),
    from1 = document.getElementById('from')

  if (from1) {
    from1.addEventListener('click', () => {
      emailRow.classList.add('hide-content')
    })
  }
}
