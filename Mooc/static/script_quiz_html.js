document.getElementById("validateBtn").addEventListener("click", checkReponses);

  function checkReponses() {
    let score = 0;

    const correctAnswers = {
      q1: "2",
      q2: "4",
      q3: ["1", "4", "5"],
      q4: ["1", "2"],
      q5: ["1", "4"],
      q6: "2",
      q7: "1"
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

    Object.keys(correctAnswers).forEach((q) => {
        const inputs = Array.from(document.querySelectorAll(`input[name="${q}"]`));
        if (inputs.length === 0) return;

        const selected = inputs.filter(i => i.checked).map(i => i.value);
        const correctRaw = correctAnswers[q];
        const correct = Array.isArray(correctRaw) ? correctRaw : [correctRaw];
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
}
