---
layout: null
title: "关于太极OS"
permalink: /about/
excerpt: "太极OS是面向智能代理工作流的可靠性运营层：预检、事件流、降级、经验池和复盘闭环。"
lang: zh-CN
---
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="太极OS是面向智能代理工作流的可靠性运营层：预检、事件流、降级、经验池和复盘闭环。">
<meta name="keywords" content="太极OS, TaijiOS, 智能代理, 静默失败, 事件流, 经验池, AI 运营">
<link rel="canonical" href="https://taijios.xyz/about/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://taijios.xyz/about/">
<meta property="og:title" content="关于太极OS · 失败会主动报警">
<meta property="og:description" content="太极OS不是聊天机器人包装, 而是一层智能代理工作流运营系统。">
<meta property="og:image" content="https://taijios.xyz/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="关于太极OS · 失败会主动报警">
<meta name="twitter:description" content="预检、事件流、降级、经验池和复盘闭环。">
<meta name="twitter:image" content="https://taijios.xyz/og.png">
<title>关于太极OS</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Noto+Sans+SC:wght@400;500;700;900&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
:root {
  --paper: #f4efe4;
  --paper-strong: #fff9eb;
  --ink: #15110d;
  --ink-soft: #52483d;
  --muted: #80766a;
  --line: rgba(21, 17, 13, 0.15);
  --charcoal: #13100d;
  --red: #c73422;
  --teal: #116f66;
  --gold: #c4922e;
  --mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --sans: "Space Grotesk", "Noto Sans SC", system-ui, sans-serif;
  --cn: "Noto Sans SC", system-ui, sans-serif;
}

* { box-sizing: border-box; }
body {
  margin: 0;
  color: var(--ink);
  background:
    radial-gradient(circle at 8% 8%, rgba(199, 52, 34, 0.15), transparent 26rem),
    radial-gradient(circle at 90% 18%, rgba(17, 111, 102, 0.18), transparent 30rem),
    linear-gradient(135deg, #f4efe4 0%, #eee4d2 50%, #f9f0dc 100%);
  font-family: var(--cn);
}
a { color: inherit; }
.shell { width: min(1120px, calc(100% - 40px)); margin: 0 auto; }
.nav {
  position: sticky;
  top: 0;
  z-index: 10;
  border-bottom: 1px solid var(--line);
  background: rgba(244, 239, 228, 0.86);
  backdrop-filter: blur(18px);
}
.nav-inner { min-height: 72px; display: flex; align-items: center; justify-content: space-between; gap: 24px; }
.brand { display: flex; align-items: center; gap: 12px; text-decoration: none; font: 700 18px var(--sans); }
.mark { width: 34px; height: 34px; border-radius: 50%; background: conic-gradient(from 180deg, var(--ink) 0 50%, var(--paper-strong) 0 100%); border: 1px solid var(--ink); box-shadow: 0 0 0 5px rgba(199,52,34,.08); }
.links { display: flex; align-items: center; gap: 18px; color: var(--ink-soft); font-weight: 700; }
.links a { text-decoration: none; }
.links a:hover { color: var(--red); }
.hero { padding: 104px 0 74px; }
.hero-grid { display: grid; grid-template-columns: 1.05fr .95fr; gap: 44px; align-items: center; }
.eyebrow { display: inline-flex; padding: 9px 12px; border: 1px solid var(--line); border-radius: 999px; background: rgba(255,255,255,.38); color: var(--red); font: 700 13px var(--mono); text-transform: uppercase; letter-spacing: .08em; }
h1 { margin: 24px 0 18px; font: 900 clamp(46px, 7vw, 86px)/.94 var(--sans); letter-spacing: -0.06em; }
.lead { max-width: 720px; color: var(--ink-soft); font-size: 20px; line-height: 1.8; }
.panel {
  border: 1px solid rgba(255,255,255,.18);
  border-radius: 30px;
  padding: 28px;
  background: linear-gradient(145deg, var(--charcoal), #241b14);
  color: #fff8e9;
  box-shadow: 0 28px 90px rgba(31,26,21,.22);
}
.panel h2 { margin: 0 0 16px; font: 800 28px var(--sans); }
.panel p { color: rgba(255,248,233,.74); line-height: 1.75; }
.status { display: grid; gap: 12px; margin-top: 22px; }
.status div { padding: 14px 16px; border-radius: 16px; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.1); }
.status strong { display: block; color: #f3c35b; margin-bottom: 4px; }
.section { padding: 74px 0; border-top: 1px solid var(--line); }
.section-head { display: flex; justify-content: space-between; gap: 28px; align-items: end; margin-bottom: 28px; }
.kicker { color: var(--red); font: 700 13px var(--mono); text-transform: uppercase; letter-spacing: .08em; }
h2 { margin: 8px 0 0; font: 900 clamp(32px, 4vw, 54px)/1 var(--sans); letter-spacing: -0.045em; }
.section-head p { max-width: 440px; margin: 0; color: var(--ink-soft); line-height: 1.75; }
.cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
.card { min-height: 230px; padding: 24px; border: 1px solid var(--line); border-radius: 26px; background: rgba(255,255,255,.4); }
.card.dark { background: var(--charcoal); color: #fff8e9; }
.card h3 { margin: 0 0 12px; font: 800 24px var(--sans); letter-spacing: -0.02em; }
.card p, .card li { color: var(--ink-soft); line-height: 1.75; }
.card.dark p, .card.dark li { color: rgba(255,248,233,.74); }
.card ul { margin: 0; padding-left: 18px; }
.rulebook { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
.rule { padding: 22px; border-radius: 24px; border: 1px solid var(--line); background: var(--paper-strong); }
.rule strong { display: block; margin-bottom: 10px; font: 800 20px var(--sans); }
.rule p { margin: 0; color: var(--ink-soft); line-height: 1.8; }
.cta { border-radius: 34px; padding: 34px; background: var(--charcoal); color: #fff8e9; display: flex; align-items: center; justify-content: space-between; gap: 24px; }
.cta h2 { color: #fff8e9; }
.cta p { color: rgba(255,248,233,.74); max-width: 620px; line-height: 1.75; }
.button { display: inline-flex; align-items: center; justify-content: center; padding: 13px 18px; border-radius: 999px; background: var(--red); color: #fff8e9; text-decoration: none; font-weight: 800; white-space: nowrap; }
footer { padding: 30px 0 44px; color: var(--muted); font-size: 14px; }
.footer-inner { display: flex; justify-content: space-between; gap: 24px; border-top: 1px solid var(--line); padding-top: 24px; }
.footer-links { display: flex; gap: 14px; flex-wrap: wrap; }
@media (max-width: 900px) {
  .hero-grid, .cards, .rulebook { grid-template-columns: 1fr; }
  .section-head, .cta, .footer-inner { align-items: flex-start; flex-direction: column; }
  .links { display: none; }
}
@media (max-width: 600px) {
  h1 { font-size: 40px; letter-spacing: -0.045em; line-height: 1.02; }
  h2 { font-size: 34px; }
  .hero { padding: 82px 0 56px; }
}
</style>
{% include analytics.html %}
</head>
<body>
<nav class="nav">
  <div class="shell nav-inner">
    <a class="brand" href="/"><span class="mark"></span><span>太极OS</span></a>
    <div class="links">
      <a href="/">首页</a>
      <a href="/crystals/">经验池</a>
      <a href="/pricing/">报价</a>
      <a href="/install/">开始接入</a>
    </div>
  </div>
</nav>

<main>
  <section class="hero">
    <div class="shell hero-grid">
      <div>
        <span class="eyebrow">About TaijiOS</span>
        <h1>太极OS不是聊天包装。它是工作流运营层。</h1>
        <p class="lead">我们处理的核心问题很窄：智能代理看起来在跑, 但关键通道未验证、旧产物冒充最新、学习层失败被当成判断成功。太极OS把这些失败暴露出来, 留下事件流, 并给出可恢复动作。</p>
      </div>
      <aside class="panel">
        <h2>当前定位</h2>
        <p>太极OS服务于已经在运行自动化、量化研究、知识库同步、内容生产或 Agent 工作流的人。它不替你做判断, 它先保证系统状态诚实。</p>
        <div class="status">
          <div><strong>正常</strong>输入、输出、事件流、交付物完整。</div>
          <div><strong>降级</strong>主流程可用, 学习层或复核层失败, 只能 learning_only。</div>
          <div><strong>失败</strong>硬阻塞未解除, 不允许伪装成成功。</div>
        </div>
      </aside>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="section-head">
        <div>
          <div class="kicker">What it does</div>
          <h2>先让系统诚实。</h2>
        </div>
        <p>太极OS不追求更热闹的自动化, 而是追求每条关键链路能被检查、复盘、降级和恢复。</p>
      </div>
      <div class="cards">
        <article class="card">
          <h3>预检</h3>
          <p>运行前检查模型、API、额度、鉴权、DNS、数据源和目标目录。通道坏了就停, 不把坏通道当可用。</p>
        </article>
        <article class="card dark">
          <h3>事件流</h3>
          <p>关键流程记录每一轮输入、输出、失败原因和最终仲裁。没有事件流的成功, 视为未验证成功。</p>
        </article>
        <article class="card">
          <h3>经验池</h3>
          <p>把复盘后的失败模式、修复规则和高质量样本沉淀为候选经验, 再经过晋升规则进入可复用知识。</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell">
      <div class="section-head">
        <div>
          <div class="kicker">Operating rules</div>
          <h2>我们默认不相信表面成功。</h2>
        </div>
        <p>系统状态必须由产物、日志、事件流和验证结果共同支撑。只要证据不足, 就按未验证处理。</p>
      </div>
      <div class="rulebook">
        <div class="rule">
          <strong>不假装成功</strong>
          <p>失败、阻塞、额度不足、旧产物、未同步、未验证 ritual 都必须 loud 报告。</p>
        </div>
        <div class="rule">
          <strong>降级不等于可判断</strong>
          <p>degraded 批次只作 learning_only, 不进入高信任 judgment 链。</p>
        </div>
        <div class="rule">
          <strong>先收口, 再扩张</strong>
          <p>每天优先完成量化交易、学习易经、自我进化三条主循环的最小闭环。</p>
        </div>
        <div class="rule">
          <strong>持续输出才是硬实力</strong>
          <p>系统能力要能在 30 天后复盘, 而不是靠一次 demo 或一句高级概念证明。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shell cta">
      <div>
        <div class="kicker">Start</div>
        <h2>带一条真实链路来。</h2>
        <p>最有效的开始方式: 给出你正在跑的自动化、最近一次失败、你希望它每天稳定产出的结果。</p>
      </div>
      <a class="button" href="/pricing/">看服务报价</a>
    </div>
  </section>
</main>

<footer>
  <div class="shell footer-inner">
    <div>太极OS · 失败会主动报警的人工智能运营层</div>
    <div class="footer-links">
      <a href="/">首页</a>
      <a href="/pricing/">报价</a>
      <a href="/crystals/">经验池</a>
      <a href="/blog.html">笔记</a>
    </div>
  </div>
</footer>
</body>
</html>
