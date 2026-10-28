// ============================================================================
// LongoUZ — AI repetitor chat oynasi
// ============================================================================

(function () {
  const form = document.getElementById("chat-form");
  const input = document.getElementById("chat-input");
  const messages = document.getElementById("chat-messages");
  const sendBtn = document.getElementById("chat-send-btn");

  if (!form) return;

  function clearEmptyState() {
    const empty = messages.querySelector(".chat-msg-empty");
    if (empty) empty.remove();
  }

  function addMessage(text, role) {
    clearEmptyState();
    const bubble = document.createElement("div");
    bubble.className = "chat-msg " + (role === "user" ? "chat-msg-user" : "chat-msg-ai");
    bubble.textContent = text;
    messages.appendChild(bubble);
    messages.scrollTop = messages.scrollHeight;
    return bubble;
  }

  function showTyping() {
    clearEmptyState();
    const typing = document.createElement("div");
    typing.className = "chat-typing";
    typing.id = "chat-typing-indicator";
    typing.innerHTML = "<span></span><span></span><span></span>";
    messages.appendChild(typing);
    messages.scrollTop = messages.scrollHeight;
  }

  function removeTyping() {
    const typing = document.getElementById("chat-typing-indicator");
    if (typing) typing.remove();
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const question = input.value.trim();
    if (!question) return;

    addMessage(question, "user");
    input.value = "";
    sendBtn.disabled = true;
    showTyping();

    try {
      const res = await fetch("/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      removeTyping();

      if (!res.ok) {
        addMessage("Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.", "ai");
        return;
      }

      const data = await res.json();
      addMessage(data.answer, "ai");
    } catch (err) {
      removeTyping();
      addMessage("Internet aloqasida muammo bo'ldi. Qayta urinib ko'ring.", "ai");
    } finally {
      sendBtn.disabled = false;
      input.focus();
    }
  });
})();
