---
title: Game Dashboard
---

# Level Up: Uma Jornada Visual pela Indústria dos Jogos 🎮

<!-- Cards with big numbers -->

<!-- TreeMap + node-link -->
<div id="observablehq-viewof-TreemapChart-b532cd5f"></div>
<div id="observablehq-viewof-includeAllYears-b532cd5f"></div>
<div id="observablehq-viewof-selectedYearFilter-b532cd5f"></div>
<div id="observablehq-viewof-selectedGenreFilter-b532cd5f"></div>
<div id="observablehq-viewof-NodeLinkChart-b532cd5f"></div>
<div id="observablehq-legend1-b532cd5f"></div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@5/dist/inspector.css">
<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@5/dist/runtime.js";
import define from "https://api.observablehq.com/d/dab8c2e1d07fb1a3@794.js?v=4";
new Runtime().module(define, name => {
  if (name === "viewof TreemapChart") return new Inspector(document.querySelector("#observablehq-viewof-TreemapChart-b532cd5f"));
  if (name === "viewof includeAllYears") return new Inspector(document.querySelector("#observablehq-viewof-includeAllYears-b532cd5f"));
  if (name === "viewof selectedYearFilter") return new Inspector(document.querySelector("#observablehq-viewof-selectedYearFilter-b532cd5f"));
  if (name === "viewof selectedGenreFilter") return new Inspector(document.querySelector("#observablehq-viewof-selectedGenreFilter-b532cd5f"));
  if (name === "viewof NodeLinkChart") return new Inspector(document.querySelector("#observablehq-viewof-NodeLinkChart-b532cd5f"));
  if (name === "legend1") return new Inspector(document.querySelector("#observablehq-legend1-b532cd5f"));
  return ["filteredData","degreesMap","degreeScale"].includes(name);
});
</script>
  
<!-- Plot -->

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

<!-- Plot da tabela -->

<div id="observablehq-viewof-table-16efeadf"></div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@5/dist/inspector.css">
<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@5/dist/runtime.js";
import define from "https://api.observablehq.com/d/dab8c2e1d07fb1a3@825.js?v=4";
new Runtime().module(define, name => {
  if (name === "viewof table") return new Inspector(document.querySelector("#observablehq-viewof-table-16efeadf"));
});
</script>