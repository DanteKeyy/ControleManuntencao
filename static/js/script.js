document.addEventListener('DOMContentLoaded', () => {
    const cardData = [
        { title: "Card 1", content: "Conteúdo do card 1.", status: "finished" },
        { title: "Card 2", content: "Conteúdo do card 2.", status: "most-urgent" },
        { title: "Card 3", content: "Conteúdo do card 3.", status: "urgent" },
        { title: "Card 4", content: "Conteúdo do card 4.", status: "common" },
        { title: "Card 5", content: "Conteúdo do card 5.", status: "no-status" },
        { title: "Card 6", content: "Conteúdo do card 6.", status: "finished" },
        { title: "Card 7", content: "Conteúdo do card 7.", status: "most-urgent" },
        { title: "Card 8", content: "Conteúdo do card 8.", status: "urgent" },
        { title: "Card 9", content: "Conteúdo do card 9.", status: "common" },
        { title: "Card 10", content: "Conteúdo do card 10.", status: "no-status" },
        { title: "Card 11", content: "Conteúdo do card 11.", status: "finished" },
        { title: "Card 12", content: "Conteúdo do card 12.", status: "most-urgent" },
        { title: "Card 13", content: "Conteúdo do card 13.", status: "urgent" },
        { title: "Card 14", content: "Conteúdo do card 14.", status: "common" },
        { title: "Card 15", content: "Conteúdo do card 15.", status: "no-status" }
    ];

    const container = document.getElementById('card-container');

    // Define a ordem dos status
    const statusPriority = {
        'most-urgent': 1,
        'urgent': 2,
        'common': 3,
        'finished': 4,
        'no-status': 5
    };

    // Define a cor de fundo para cada status
    const statusColors = {
        'finished': '#28a745',
        'most-urgent': '#dc3545',
        'urgent': '#ffc107',
        'common': '#007bff',
        'no-status': '#6c757d'
    };

    // Ordena os dados dos cards com base na prioridade do status
    cardData.sort((a, b) => statusPriority[a.status] - statusPriority[b.status]);

    // Adiciona todos os cards ao contêiner
    cardData.forEach(cardInfo => {
        const card = document.createElement('div');
        card.className = 'card';

        const cardTitle = document.createElement('h2');
        cardTitle.textContent = cardInfo.title;

        const cardContent = document.createElement('p');
        cardContent.textContent = cardInfo.content;

        const cardStatus = document.createElement('div');
        cardStatus.className = `status ${cardInfo.status}`;
        cardStatus.textContent = cardInfo.status.replace(/-/g, ' ').toUpperCase(); // Exibe o status com palavras em maiúsculas e substitui hífens por espaços

        const statusSelect = document.createElement('div');
        statusSelect.className = 'status-select';
        
        const select = document.createElement('select');
        const statuses = [
            { value: 'finished', label: 'Finalizado' },
            { value: 'most-urgent', label: 'Muito Urgente' },
            { value: 'urgent', label: 'Urgente' },
            { value: 'common', label: 'Comum' },
            { value: 'no-status', label: 'Sem Status' }
        ];
        
        statuses.forEach(status => {
            const option = document.createElement('option');
            option.value = status.value;
            option.textContent = status.label;
            select.appendChild(option);
        });

        select.value = cardInfo.status;
        select.style.backgroundColor = statusColors[cardInfo.status]; // Define a cor de fundo com base no status atual

        select.addEventListener('change', (event) => {
            const newStatus = event.target.value;
            cardStatus.className = `status ${newStatus}`;
            cardStatus.textContent = newStatus.replace(/-/g, ' ').toUpperCase(); // Atualiza o texto do status

            // Atualiza a cor de fundo do seletor
            select.style.backgroundColor = statusColors[newStatus];

            // Atualiza o status no cardData
            cardInfo.status = newStatus;

            // Reordena os cards após a atualização
            const cards = Array.from(container.children);
            cards.sort((a, b) => statusPriority[a.querySelector('.status').className.split(' ')[1]] - statusPriority[b.querySelector('.status').className.split(' ')[1]]);
            cards.forEach(card => container.appendChild(card)); // Reanexa os cards ordenados
        });

        statusSelect.appendChild(select);
        
        card.appendChild(cardTitle);
        card.appendChild(cardContent);
        card.appendChild(cardStatus);
        card.appendChild(statusSelect);

        container.appendChild(card);
    });
});
