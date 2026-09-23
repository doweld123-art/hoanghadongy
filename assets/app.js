(function () {
  var cfg = window.SITE_CONFIG || {};
  var params = new URLSearchParams(location.search);

  // Ghi nhớ nguồn traffic (UTM + ttclid) để gắn vào lead.
  var source = {};
  ["utm_source", "utm_medium", "utm_campaign", "utm_content", "ttclid"].forEach(function (k) {
    if (params.get(k)) source[k] = params.get(k);
  });
  try {
    if (Object.keys(source).length) sessionStorage.setItem("src", JSON.stringify(source));
    else source = JSON.parse(sessionStorage.getItem("src") || "{}");
  } catch (e) {}

  var fromTikTok = source.ttclid || /tiktok/i.test(source.utm_source || "") || /tiktok/i.test(document.referrer);
  if (fromTikTok) document.getElementById("welcome").hidden = false;

  // TikTok Pixel
  if (cfg.tiktokPixelId) {
    !function (w, d, t) {
      w.TiktokAnalyticsObject = t; var ttq = w[t] = w[t] || [];
      ttq.methods = ["page", "track", "identify", "instances", "debug", "on", "off", "once", "ready", "alias", "group", "enableCookie", "disableCookie"];
      ttq.setAndDefer = function (t, e) { t[e] = function () { t.push([e].concat(Array.prototype.slice.call(arguments, 0))); }; };
      for (var i = 0; i < ttq.methods.length; i++) ttq.setAndDefer(ttq, ttq.methods[i]);
      ttq.load = function (e) {
        var s = d.createElement("script"); s.async = true;
        s.src = "https://analytics.tiktok.com/i18n/pixel/events.js?sdkid=" + e + "&lib=" + t;
        d.head.appendChild(s);
      };
      ttq.load(cfg.tiktokPixelId); ttq.page();
    }(window, document, "ttq");
  }
  function track(event, props) {
    if (window.ttq) window.ttq.track(event, props || {});
  }

  // Gắn link CTA
  var zalo = /^https?:/.test(cfg.zalo || "") ? cfg.zalo : "https://zalo.me/" + (cfg.zalo || "");
  var links = {
    "cta-zalo": zalo,
    "cta-call": "tel:" + (cfg.phone || ""),
    "cta-messenger": cfg.messenger,
    "cta-map": cfg.map,
    "tiktok-link": cfg.tiktok
  };
  Object.keys(links).forEach(function (id) {
    var el = document.getElementById(id);
    if (el && links[id]) el.href = links[id];
  });
  document.querySelectorAll("[data-cta]").forEach(function (el) {
    el.addEventListener("click", function () {
      track("Contact", { content_name: el.dataset.cta });
    });
  });

  // Form lead
  var form = document.getElementById("lead-form");
  var msg = document.getElementById("form-msg");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var data = Object.fromEntries(new FormData(form));
    data.phone = (data.phone || "").replace(/[\s.-]/g, "");
    if (!data.name.trim() || !/^(0|\+84)[0-9]{9}$/.test(data.phone)) {
      msg.textContent = "Vui lòng nhập họ tên và số điện thoại hợp lệ.";
      return;
    }
    data.source = source;
    data.time = new Date().toISOString();

    var done = function () {
      track("SubmitForm", { content_name: data.topic });
      form.reset();
      msg.textContent = "Cảm ơn bạn! Chúng tôi sẽ liên hệ lại sớm.";
    };
    if (cfg.leadEndpoint) {
      fetch(cfg.leadEndpoint, { method: "POST", mode: "no-cors", body: JSON.stringify(data) })
        .then(done)
        .catch(function () { msg.textContent = "Gửi thất bại, vui lòng nhắn Zalo giúp chúng tôi."; });
    } else {
      try {
        var leads = JSON.parse(localStorage.getItem("leads") || "[]");
        leads.push(data);
        localStorage.setItem("leads", JSON.stringify(leads));
      } catch (err) {}
      done();
    }
  });
})();
