---
toc: false
---

<div class="hero">
  <h1>Level Up: Uma Jornada Visual pela Indústria dos Jogos</h1>
</div>

<!-- Treemap + graph -->
<h2> Top 1000 best games (according to Metacritic)</h1>

<div id="observablehq-viewof-includeAllYears-416a10b6"></div>
<div id="observablehq-viewof-selectedYearFilter-416a10b6"></div>
<div id="observablehq-viewof-selectedGenreFilter-416a10b6"></div>
<div id="observablehq-viewof-NodeLinkChart-416a10b6"></div>
<div id="observablehq-legend1-416a10b6"></div>
</br>
<h2>Popular Game Genres by Year</h2>
<div id="observablehq-viewof-TreemapChart-416a10b6"></div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@5/dist/inspector.css">
<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@5/dist/runtime.js";
import define from "https://api.observablehq.com/d/dab8c2e1d07fb1a3@854.js?v=4";
new Runtime().module(define, name => {
  if (name === "viewof includeAllYears") return new Inspector(document.querySelector("#observablehq-viewof-includeAllYears-416a10b6"));
  if (name === "viewof selectedYearFilter") return new Inspector(document.querySelector("#observablehq-viewof-selectedYearFilter-416a10b6"));
  if (name === "viewof selectedGenreFilter") return new Inspector(document.querySelector("#observablehq-viewof-selectedGenreFilter-416a10b6"));
  if (name === "viewof NodeLinkChart") return new Inspector(document.querySelector("#observablehq-viewof-NodeLinkChart-416a10b6"));
  if (name === "legend1") return new Inspector(document.querySelector("#observablehq-legend1-416a10b6"));
  if (name === "viewof TreemapChart") return new Inspector(document.querySelector("#observablehq-viewof-TreemapChart-416a10b6"));
  return ["filteredData","degreesMap","degreeScale"].includes(name);
});
</script>

---

<!-- Remaing graphics -->

<div id="observablehq-viewof-anoSelecionado-c7dc6688"></div>
<div id="observablehq-viewof-view-c7dc6688"></div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@5/dist/inspector.css">
<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@5/dist/runtime.js";
import define from "https://api.observablehq.com/d/dab8c2e1d07fb1a3@819.js?v=4";
new Runtime().module(define, name => {
  if (name === "viewof anoSelecionado") return new Inspector(document.querySelector("#observablehq-viewof-anoSelecionado-c7dc6688"));
  if (name === "viewof view") return new Inspector(document.querySelector("#observablehq-viewof-view-c7dc6688"));
  return ["dadosFiltrados","graficoBarras"].includes(name);
});
</script>

---

<!-- Table -->
<h2> Most selling games</h2>

<div id="observablehq-viewof-table-16efeadf"></div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@5/dist/inspector.css">
<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@5/dist/runtime.js";
import define from "https://api.observablehq.com/d/dab8c2e1d07fb1a3@825.js?v=4";
new Runtime().module(define, name => {
  if (name === "viewof table") return new Inspector(document.querySelector("#observablehq-viewof-table-16efeadf"));
});
</script>

<style>

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: var(--sans-serif);
  margin: 4rem 0 8rem;
  text-wrap: balance;
  text-align: center;
}

.hero h1 {
  margin: 1rem 0;
  padding: 1rem 0;
  max-width: none;
  font-size: 14vw;
  font-weight: 900;
  line-height: 1;
  background: linear-gradient(30deg, var(--theme-foreground-focus), currentColor);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero h2 {
  margin: 0;
  max-width: 34em;
  font-size: 20px;
  font-style: initial;
  font-weight: 500;
  line-height: 1.5;
  color: var(--theme-foreground-muted);
}

@media (min-width: 640px) {
  .hero h1 {
    font-size: 90px;
  }
}
</style>
