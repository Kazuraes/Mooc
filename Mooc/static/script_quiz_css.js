document.getElementById("validateBtn").addEventListener("click", function(e) {
    e.preventDefault();

    let score = 0;
    const correctResponses = {
        q1: ["2", "3"],
        q2: ["1", "2", "3"],
        q3: ["1", "2", "4"],
        q4: ["3"],
        q5: ["2", "3"],
        q6: ["1", "3"],
        q7: ["2"]
    };

    function getCommonAncestor(nodes) {
        const paths = nodes.map(n => {
            const p = [];
            let cur = n;
            while (cur) { p.push(cur); cur = cur.parentElement; }
            return p;
        });
        const firstPath = paths[0] || [];
        for (let i = 0; i < firstPath.length; i++) {
            const node = firstPath[i];
            if (paths.every(p => p.includes(node))) return node;
        }
        return document.body;
    }

    Object.keys(correctResponses).forEach((q) => {
        const inputs = Array.from(document.querySelectorAll(`input[name="${q}"]`));
        if (inputs.length === 0) return;

        const selected = inputs.filter(i => i.checked).map(i => i.value);
        const correct = correctResponses[q];
        const isCorrect = selected.length === correct.length && selected.every(v => correct.includes(v));
        if (isCorrect) score++;

        const container = getCommonAncestor(inputs);
        let fb = container.querySelector('.feedback');
        if (!fb) {
            fb = document.createElement('div');
            fb.className = 'feedback';
            fb.style.fontWeight = '600';
            fb.style.marginBottom = '8px';
            container.insertBefore(fb, container.firstChild);
        }
        fb.textContent = isCorrect ? '✅ Correct' : '❌ Incorrect';
        fb.classList.toggle('correct', isCorrect);
        fb.classList.toggle('incorrect', !isCorrect);
    });

    document.getElementById("result").textContent = `✅ Vous avez obtenu ${score} / 7`;
});

