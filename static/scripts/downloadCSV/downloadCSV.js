function converteArrayParaCsv(dados)
{
    const titulos = Object.keys(dados[0]).join(',');
    const linhas = dados.map(obj => Object.values(obj).join(','));
    return [titulos, ...linhas].join('\n');
}

function downloadCSV( dados, nomeArquivo )
{
    const filename = nomeArquivo + '.csv';

    const csv = converteArrayParaCsv(dados);
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.style.display = 'none';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}