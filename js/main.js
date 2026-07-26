/* SS ERP Solutions — shared interactions (PRD v1.2 §8)
   Particle-wave hero, counters, scroll reveals, FAQ accordion,
   mobile nav, chat panel. All motion respects prefers-reduced-motion. */

(function () {
  "use strict";

  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- dark / light theme toggle (client request, interview 2026-07-25) ----------
     Default is dark per PRD §7; choice persists in localStorage.
     A tiny inline script in <head> applies the saved theme before paint. */
  var root = document.documentElement;
  var themeBtn = document.querySelector(".theme-toggle");
  var setThemeIcon = function () {
    if (themeBtn) themeBtn.textContent = root.getAttribute("data-theme") === "light" ? "🌙" : "☀";
  };
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("sserp-theme", next); } catch (e) {}
      setThemeIcon();
    });
    setThemeIcon();
  }

  /* ---------- message delivery (no direct WhatsApp links, client rule) ----------
     Messages are relayed from the page itself: email via the FormSubmit
     relay (activate once by clicking the confirmation mail it sends to
     support@), and optionally pushed to the team's WhatsApp via CallMeBot
     when WA_RELAY_KEY is configured. The number is never rendered. */
  var RELAY_EMAIL = "support@sserpsolutions.net";
  var WA_RELAY_KEY = ""; // CallMeBot apikey — set to enable WhatsApp push
  var deliver = function (subject, text) {
    var jobs = [];
    jobs.push(fetch("https://formsubmit.co/ajax/" + RELAY_EMAIL, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify({ _subject: subject, message: text, page: location.href })
    }).then(function (r) { if (!r.ok) throw new Error("relay " + r.status); return r.json(); }));
    if (WA_RELAY_KEY) {
      var n = atob("OTE4OTM5MTI2MjMy");
      jobs.push(fetch("https://api.callmebot.com/whatsapp.php?phone=" + n +
        "&apikey=" + encodeURIComponent(WA_RELAY_KEY) +
        "&text=" + encodeURIComponent(subject + "\n" + text), { mode: "no-cors" }).catch(function () {}));
    }
    return jobs[0];
  };

  /* ---------- on-site chat window ---------- */
  var waPanel = document.querySelector(".wa-panel");
  if (waPanel) {
    var waThread = waPanel.querySelector("[data-wa-thread]");
    var waInput = waPanel.querySelector("[data-wa-input]");
    var waBubble = function (cls, text) {
      var d = document.createElement("div");
      d.className = "wa-msg " + cls;
      d.textContent = text;
      var t = document.createElement("span");
      t.className = "wa-time";
      t.textContent = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
      d.appendChild(t);
      waThread.appendChild(d);
      waThread.scrollTop = waThread.scrollHeight;
    };
    var waGreeted = false;
    var waGreet = function () {
      if (waGreeted) return;
      waGreeted = true;
      var h = new Date().getHours();
      var hello = h < 12 ? "Good morning" : (h < 17 ? "Good afternoon" : "Good evening");
      var name = null;
      try { name = localStorage.getItem("sserp-user-name"); } catch (e) {}
      var first = waThread.querySelector(".wa-msg");
      var g = document.createElement("div");
      g.className = "wa-msg in";
      g.textContent = hello + (name ? ", " + name : "") + " 👋 Welcome to SS ERP Solutions.";
      waThread.insertBefore(g, first);
    };
    document.querySelectorAll("[data-wa-open]").forEach(function (el) {
      el.addEventListener("click", function (e) {
        e.preventDefault();
        waPanel.classList.toggle("open");
        if (waPanel.classList.contains("open")) {
          waGreet();
          if (waInput) waInput.focus();
        }
      });
    });
    var waSendBtn = waPanel.querySelector("[data-wa-send]");
    var waSending = false;
    var waSend = function () {
      var text = (waInput.value || "").trim();
      if (!text || waSending) return;
      waSending = true;
      waBubble("out", text);
      waInput.value = "";
      deliver("Chat message from sserpsolutions.net", text).then(function () {
        waBubble("in", "Delivered ✓ We usually reply within a few hours — make sure your message includes an email or phone number.");
      }).catch(function () {
        waBubble("in", "Hmm, that didn't go through from the browser. Please email us at " + RELAY_EMAIL + " — sorry about that.");
      }).then(function () { waSending = false; });
    };
    if (waSendBtn) waSendBtn.addEventListener("click", waSend);
    if (waInput) waInput.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); waSend(); }
    });
  }

  /* ---------- sticky header state ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("scrolled", window.scrollY > 10);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------- mobile nav ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") links.classList.remove("open");
    });
  }

  /* ---------- particle-wave hero (PRD §6.2.2) ---------- */
  var canvas = document.getElementById("particle-canvas");
  if (canvas && !reducedMotion) {
    var ctx = canvas.getContext("2d");
    var particles = [];
    var W, H, t = 0;

    var resize = function () {
      W = canvas.width = canvas.offsetWidth;
      H = canvas.height = canvas.offsetHeight;
      particles = [];
      var cols = Math.floor(W / 34);
      var rows = Math.floor(H / 34);
      for (var i = 0; i <= cols; i++) {
        for (var j = 0; j <= rows; j++) {
          particles.push({ x: i * 34, y: j * 34, baseY: j * 34, phase: (i * 0.35 + j * 0.2) });
        }
      }
    };

    var draw = function () {
      ctx.clearRect(0, 0, W, H);
      t += 0.012;
      for (var k = 0; k < particles.length; k++) {
        var p = particles[k];
        var wave = Math.sin(t + p.phase) * 9 + Math.sin(t * 0.6 + p.x * 0.008) * 7;
        var y = p.baseY + wave;
        var glow = (Math.sin(t + p.phase) + 1) / 2;
        var goldMix = glow > 0.82;
        var light = root.getAttribute("data-theme") === "light";
        ctx.beginPath();
        ctx.arc(p.x, y, goldMix ? 1.6 : 1.1, 0, Math.PI * 2);
        ctx.fillStyle = goldMix
          ? "rgba(178,140,55," + (0.3 + glow * 0.4) + ")"
          : (light
            ? "rgba(60,80,130," + (0.1 + glow * 0.16) + ")"
            : "rgba(120,140,180," + (0.06 + glow * 0.12) + ")");
        ctx.fill();
      }
      requestAnimationFrame(draw);
    };

    resize();
    window.addEventListener("resize", resize);
    requestAnimationFrame(draw);
  }

  /* ---------- animated counters, trigger in view (PRD §8) ---------- */
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length) {
    var animate = function (el) {
      var target = parseFloat(el.getAttribute("data-count"));
      if (reducedMotion) { el.textContent = target; return; }
      var dur = 1600, start = null;
      var step = function (ts) {
        if (!start) start = ts;
        var p = Math.min((ts - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased);
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    var cObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { animate(en.target); cObs.unobserve(en.target); }
      });
    }, { threshold: 0.4 });
    counters.forEach(function (c) { cObs.observe(c); });
  }

  /* ---------- scroll reveals ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if (reveals.length) {
    if (reducedMotion) {
      reveals.forEach(function (r) { r.classList.add("visible"); });
    } else {
      var rObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add("visible"); rObs.unobserve(en.target); }
        });
      }, { threshold: 0.12 });
      reveals.forEach(function (r) { rObs.observe(r); });
    }
  }

  /* ---------- FAQ accordion (PRD §6.2.11) ---------- */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var q = item.querySelector(".faq-q");
    var a = item.querySelector(".faq-a");
    if (!q || !a) return;
    q.addEventListener("click", function () {
      var isOpen = item.classList.contains("open");
      document.querySelectorAll(".faq-item.open").forEach(function (o) {
        o.classList.remove("open");
        o.querySelector(".faq-a").style.maxHeight = null;
        o.querySelector(".faq-q").setAttribute("aria-expanded", "false");
      });
      if (!isOpen) {
        item.classList.add("open");
        a.style.maxHeight = a.scrollHeight + "px";
        q.setAttribute("aria-expanded", "true");
      }
    });
  });

  /* ---------- "How can we help?" guided assistant ----------
     Deterministic quick-reply menu (it introduces itself as a guide, not a
     human). Remembers the visitor's name from the portal sign-in and greets
     returning visitors. A third-party live-chat widget can replace or sit
     beside this at go-live. */
  var chatBtn = document.querySelector(".float-btn.chat");
  var chatPanel = document.querySelector(".chat-panel");
  if (chatBtn && chatPanel) {
    var thread = chatPanel.querySelector("[data-chat-thread]");
    var croot = chatPanel.getAttribute("data-root") || "";
    var started = false;
    var savedName = null;
    try { savedName = localStorage.getItem("sserp-user-name"); } catch (e) {}
    var safeName = savedName ? savedName.replace(/[<>&"]/g, "") : null;

    var bot = function (html) {
      var d = document.createElement("div");
      d.className = "chat-msg bot";
      d.innerHTML = html;
      thread.appendChild(d);
      thread.scrollTop = thread.scrollHeight;
    };
    var opts = function (list) {
      var w = document.createElement("div");
      w.className = "chat-opts";
      list.forEach(function (o) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "chat-opt";
        b.textContent = o[0];
        b.addEventListener("click", function () {
          var u = document.createElement("div");
          u.className = "chat-msg user";
          u.textContent = o[0];
          thread.appendChild(u);
          w.remove();
          o[1]();
        });
        w.appendChild(b);
      });
      thread.appendChild(w);
      thread.scrollTop = thread.scrollHeight;
    };
    var again = function () { opts([["Something else", menu]]); };
    var menu = function () {
      opts([
        ["Request an SAP health check", function () {
          bot('Smart place to start. A senior consultant reviews your system and gives you an honest findings report. <a href="' + croot + 'health-check.html">See what the health check covers →</a>');
          again();
        }],
        ["Discuss a new project", function () {
          bot('Great — tell us about your landscape and goals and a senior consultant will come back within one business day. <a href="' + croot + 'contact/index.html">Open the contact form →</a>');
          again();
        }],
        ["Support for a running system", function () {
          bot('Our AMS desk covers SAP, Oracle and mixed estates. Email <a href="mailto:support@sserpsolutions.net">support@sserpsolutions.net</a> or use the <a href="' + croot + 'contact/index.html">contact form</a> and choose “AMS / production support”.');
          again();
        }],
        ["Training & internships", function () {
          bot('Growing Together runs practitioner-led SAP training, internships and mentoring. <a href="' + croot + 'growing-together/index.html">Explore the programmes →</a>');
          again();
        }],
        ["Careers", function () {
          bot('We hire consultants who care how the work is done. <a href="' + croot + 'careers/index.html">See open roles →</a>');
          again();
        }],
        ["Talk to a person", function () {
          bot('Two quick routes: the green message button below (goes straight to our team) or <a href="mailto:support@sserpsolutions.net">support@sserpsolutions.net</a>. We reply promptly during business hours (IST).');
          again();
        }]
      ]);
    };
    chatBtn.addEventListener("click", function () {
      chatPanel.classList.toggle("open");
      if (chatPanel.classList.contains("open") && !started) {
        started = true;
        bot(safeName
          ? "Welcome back, <strong>" + safeName + "</strong> 👋 How can we help today?"
          : "Hello 👋 I'm the SS ERP Solutions guide — a quick menu, not a person. How can we help?");
        menu();
      }
    });
  }

  /* ---------- Google sign-in (portal) ----------
     Uses Google Identity Services when a client ID is configured on the
     [data-google-config] element; until then, shows an honest note. */
  var gbtn = document.querySelector("[data-google-signin]");
  if (gbtn) {
    gbtn.addEventListener("click", function () {
      var cfg = document.querySelector("[data-google-config]");
      var cid = cfg ? cfg.getAttribute("data-client-id") : "";
      var note = document.querySelector(".google-note");
      if (!cid) {
        if (note) { note.textContent = "Google sign-in activates once the Google OAuth client ID is configured for this domain — use email sign-in meanwhile."; note.style.display = "block"; }
        return;
      }
      if (window.google && google.accounts && google.accounts.id) {
        google.accounts.id.initialize({
          client_id: cid,
          callback: function (resp) {
            try {
              var payload = JSON.parse(atob(resp.credential.split(".")[1].replace(/-/g, "+").replace(/_/g, "/")));
              if (payload.name) localStorage.setItem("sserp-user-name", payload.name.split(" ")[0]);
              if (payload.email) localStorage.setItem("sserp-user-email", payload.email);
            } catch (e) {}
            window.location.href = "dashboard.html";
          }
        });
        google.accounts.id.prompt();
      } else if (note) {
        note.textContent = "Google sign-in script did not load — use email sign-in meanwhile.";
        note.style.display = "block";
      }
    });
  }

  /* ---------- requirement relay: compose once, deliver via email AND WhatsApp ---------- */
  document.querySelectorAll("form[data-relay-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var hp = form.querySelector(".honeypot input");
      if (hp && hp.value) return;
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var lines = ["New requirement via sserpsolutions.net"];
      form.querySelectorAll("input[id], select[id], textarea[id]").forEach(function (f) {
        if (!f.value) return;
        var label = form.querySelector('label[for="' + f.id + '"]');
        var name = label ? label.textContent.replace("*", "").trim() : f.id;
        lines.push(name + ": " + f.value);
      });
      var text = lines.join("\n");
      var company = form.querySelector("#rq-company");
      var subject = "New requirement — " + (company && company.value ? company.value : "website enquiry");
      var mail = form.querySelector("[data-relay-mail]");
      if (mail) mail.href = "mailto:" + RELAY_EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(text);
      var btn = form.querySelector("button[type=submit]");
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      deliver(subject, text).then(function () {
        var ok = form.querySelector(".form-success");
        if (ok) ok.style.display = "block";
        if (btn) btn.textContent = "Sent ✓";
      }).catch(function () {
        var actions = form.querySelector(".relay-actions");
        if (actions) actions.style.display = "flex";
        if (btn) { btn.disabled = false; btn.textContent = "Try again"; }
      });
      var nm = form.querySelector("#rq-name");
      if (nm && nm.value) { try { localStorage.setItem("sserp-user-name", nm.value.split(" ")[0]); } catch (er) {} }
    });
  });

  /* ---------- greet signed-in portal visitors ---------- */
  document.querySelectorAll("[data-user-greet]").forEach(function (el) {
    var n = null;
    try { n = localStorage.getItem("sserp-user-name"); } catch (e) {}
    if (n) el.textContent = "Welcome back, " + n + " — ";
  });

  /* ---------- back to top ---------- */
  var backTop = document.querySelector(".back-top");
  if (backTop) {
    window.addEventListener("scroll", function () {
      backTop.classList.toggle("show", window.scrollY > 600);
    }, { passive: true });
    backTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: reducedMotion ? "auto" : "smooth" });
    });
  }

  /* ---------- cookie / privacy notice ---------- */
  var cookieBar = document.querySelector(".cookie-bar");
  if (cookieBar) {
    var seen = null;
    try { seen = localStorage.getItem("sserp-cookie-ok"); } catch (e) {}
    if (!seen) {
      // wait for webfonts so the banner never reflows once visible (CLS)
      var fontsReady = (document.fonts && document.fonts.ready) ? document.fonts.ready : Promise.resolve();
      fontsReady.then(function () {
        setTimeout(function () { cookieBar.classList.add("show"); }, 400);
      });
    }
    var okBtn = cookieBar.querySelector("[data-cookie-ok]");
    if (okBtn) okBtn.addEventListener("click", function () {
      try { localStorage.setItem("sserp-cookie-ok", "1"); } catch (e) {}
      cookieBar.classList.remove("show");
    });
  }

  /* ---------- forms: client-side validation + honeypot spam trap ----------
     On Webflow these become native forms with server-side spam protection
     and delivery to the official mailbox; this mirrors the UX for review. */
  document.querySelectorAll("form[data-demo-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var hp = form.querySelector(".honeypot input");
      if (hp && hp.value) return; // silent drop: bot filled the trap
      if (!form.checkValidity()) { form.reportValidity(); return; }
      if (form.hasAttribute("data-portal-login")) {
        var em = form.querySelector("input[type=email]");
        if (em && em.value) {
          var nm = em.value.split("@")[0].replace(/[._-]+/g, " ").trim();
          nm = nm.charAt(0).toUpperCase() + nm.slice(1);
          try { localStorage.setItem("sserp-user-name", nm); } catch (e) {}
        }
      }
      var ok = form.querySelector(".form-success");
      if (ok) { ok.style.display = "block"; }
      form.reset();
    });
  });
})();
