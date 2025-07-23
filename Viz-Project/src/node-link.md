# Top 1000 best games

<div id="observablehq-viewof-includeAllYears-b3c99ca9"></div>
<div id="observablehq-viewof-selectedYearFilter-b3c99ca9"></div>
<div id="observablehq-viewof-selectedGenreFilter-b3c99ca9"></div>
<div id="observablehq-viewof-NodeLinkChart-b3c99ca9"></div>
<div id="observablehq-legend1-b3c99ca9"></div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@5/dist/inspector.css">
<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@5/dist/runtime.js";
import define from "https://api.observablehq.com/d/dab8c2e1d07fb1a3@794.js?v=4";
new Runtime().module(define, name => {
  if (name === "viewof includeAllYears") return new Inspector(document.querySelector("#observablehq-viewof-includeAllYears-b3c99ca9"));
  if (name === "viewof selectedYearFilter") return new Inspector(document.querySelector("#observablehq-viewof-selectedYearFilter-b3c99ca9"));
  if (name === "viewof selectedGenreFilter") return new Inspector(document.querySelector("#observablehq-viewof-selectedGenreFilter-b3c99ca9"));
  if (name === "viewof NodeLinkChart") return new Inspector(document.querySelector("#observablehq-viewof-NodeLinkChart-b3c99ca9"));
  if (name === "legend1") return new Inspector(document.querySelector("#observablehq-legend1-b3c99ca9"));
  return ["filteredData","viewof TreemapChart","degreesMap","degreeScale"].includes(name);
});
</script>