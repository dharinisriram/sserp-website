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

  /* ---------- live-chat panel placeholder (widget embeds at go-live) ---------- */
  var chatBtn = document.querySelector(".float-btn.chat");
  var chatPanel = document.querySelector(".chat-panel");
  if (chatBtn && chatPanel) {
    chatBtn.addEventListener("click", function () {
      chatPanel.classList.toggle("open");
    });
  }

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
    if (!seen) cookieBar.classList.add("show");
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
      var ok = form.querySelector(".form-success");
      if (ok) { ok.style.display = "block"; }
      form.reset();
    });
  });
})();
