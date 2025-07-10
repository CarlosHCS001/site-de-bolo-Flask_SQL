function adicionarCarrinho(produto) {
  fetch('/adicionar-carrinho', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ produto })
  })
  .then(res => res.json())
  .then(data => alert(data.mensagem))
  .catch(err => console.error('Erro:', err));
}
