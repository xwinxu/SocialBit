
<!DOCTYPE html>


<html>
<head>
  <link rel = "stylesheet" href = "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
</head>
<body>
  <div class = "container">
    <h1>SocialBit</h1>
    <div class = "row">
      <br>
    </div>
    <div class = "row">
      <div class = "col-6"><h2>Trial</h2></div>
    </div>
    <div class = "row">
      <div class = "col-6"><h3>Location of Friends</h3></div>
      <div class = "col-6"><h3>Sequence of Friends</h3></div>
    </div>
    <div class = "row">
      <div class = "col-6"><svg class = "locshort" width="500" height="300"></svg></div>
      <div class = "col-6"><svg class = "contain seqshort" width="500" height="300"></svg></div>
    </div>
    <div class = "row">
      <br>
    </div>
    <!-- After Long Use -->
    <div class = "row">
      <div class = "col-6"><h2>After Long Use</h2></div>
    </div>
    <div class = "row">
      <div class = "col-6"><h3>Location of Friends</h3></div>
      <div class = "col-6"><h3>Sequence of Friends</h3></div>
    </div>
    <div class = "row">
      <div class = "col-6"><svg class = "loclong" width="500" height="300"></svg></div>
      <div class = "col-6"><svg class = "contain seqlong" width="500" height="300"></svg></div>
    </div>
  </div>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
  <script src="https://d3js.org/d3.v4.min.js"></script>
  <script
  src="https://code.jquery.com/jquery-3.3.1.min.js"
  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
  crossorigin="anonymous"></script>
</body>
</html>

<style>
.links line {
  stroke: #999;
  stroke-opacity: 0.6;
}
.nodes circle {
  stroke: #fff;
  stroke-width: 1.5px;
}
.contain {
  background-color:rgba(182, 182, 182, 0.29);
}
body{
  padding-top:30px;
}
.loclong {
  background-image: url('manhattan.png');
}
.locshort {
  background-image: url('manhattan.png');
}
.group-tick line {
  stroke: #000;
}
.ribbons {
  fill-opacity: 0;
}
</style>



<script>
var svg2 = d3.select(".loclong"),
    widthh = +svg2.attr("width"),
    heightt = +svg2.attr("height");
var color1 = d3.scaleOrdinal(d3.schemeCategory20);
var simulationn = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.id; }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(widthh / 2, heightt / 2));
d3.json("miserables.json", function(error, graph) {
  if (error) throw error;
  var linkk = svg2.append("g")
      .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
      .attr("stroke-width", function(d) { return Math.sqrt(d.value); });
  var nodee = svg2.append("g")
      .attr("class", "nodes")
    .selectAll("circle")
    .data(graph.nodes)
    .enter().append("circle")
      .attr("r", 5)
      .attr("fill", function(d) { return color(d.group); })
  nodee.append("title")
      .text(function(d) { return d.id; });
  simulationn
      .nodes(graph.nodes)
      .on("tick", ticked);
  simulationn.force("link")
      .links(graph.links);
  function ticked() {
    linkk
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });
    nodee
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  }
});
function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}
function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}
function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
</script>


<script>

var svg = d3.select(".locshort"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var color5 = d3.scaleOrdinal(d3.schemeCategory20);

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.id; }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("addnodes.json", function(error, graph) {
  if (error) throw error;

  var link = svg.append("g")
      .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
      .attr("stroke-width", function(d) { return Math.sqrt(d.value); });

  var node = svg.append("g")
      .attr("class", "nodes")
    .selectAll("circle")
    .data(graph.nodes)
    .enter().append("circle")
      .attr("r", 5)
      .attr("fill", function(d) { return color5(d.group); })
      .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));

  node.append("title")
      .text(function(d) { return d.id; });

  simulation
      .nodes(graph.nodes)
      .on("tick", ticked);

  simulation.force("link")
      .links(graph.links);

  function ticked() {
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  }
});

function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}

</script>


<script>
$('button').click(function() {

 $.ajax({
  type: "POST",
  url: "server.php",
  data: { name: "John" }
}).done(function( msg ) {
  alert( "Data Saved: " + msg );
});

    });
</script>

<script>
var matrix = [
  [11975,  5871, 8916, 2868],
  [ 1951, 10048, 2060, 6171],
  [ 8010, 16145, 8090, 8045],
  [ 1013,   990,  940, 6907]
];
var svg1 = d3.select(".seqlong"),
    width = +svg1.attr("width"),
    height = +svg1.attr("height"),
    outerRadius = Math.min(width, height) * 0.5 - 40,
    innerRadius = outerRadius - 5;
//var formatValue = d3.formatPrefix(",.0", 1e3);
var chord = d3.chord()
    .padAngle(0.05)
    .sortSubgroups(d3.descending);
var arc = d3.arc()
    .innerRadius(innerRadius)
    .outerRadius(outerRadius);
var ribbon = d3.ribbon()
    .radius(innerRadius);
var color = d3.scaleOrdinal()
    .domain(d3.range(4))
    .range(["rgb(201, 85, 158)", "#46e3c2", "#c8de6f", "#F26223", "rgb(173, 14, 115)", "rgb(36, 141, 164)", "rgb(102, 132, 152)"]);
var g = svg1.append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
    .datum(chord(matrix));
var group = g.append("g")
    .attr("class", "groups")
  .selectAll("g")
  .data(function(chords) { return chords.groups; })
  .enter().append("g");
group.append("path")
    .style("fill", function(d) { return color(d.index); })
    .style("stroke", function(d) { return d3.rgb(color(d.index)).darker(); })
    .attr("d", arc);
g.append("g")
    .attr("class", "ribbons")
  .selectAll("path")
  .data(function(chords) { return chords; })
  .enter().append("path")
    .attr("d", ribbon)
    .style("fill", function(d) { return color(d.target.index); })
    .style("stroke", function(d) { return d3.rgb(color(d.target.index)).darker(); });
// Returns an array of tick angles and values for a given group and step.
function groupTicks(d, step) {
  var k = (d.endAngle - d.startAngle) / d.value;
  return d3.range(0, d.value, step).map(function(value) {
    return {value: value, angle: value * k + d.startAngle};
  });
}
</script>

<script>
var matrix = [
  [4,  5871, 0, 2868],
  [ 0, 1048, 0, 6171],
  [ 810, 4, 0, 8045],
  [ 0,   990,  940, 6907]
];
var svg1 = d3.select(".seqshort"),
    width = +svg1.attr("width"),
    height = +svg1.attr("height"),
    outerRadius = Math.min(width, height) * 0.5 - 40,
    innerRadius = outerRadius - 5;
//var formatValue = d3.formatPrefix(",.0", 1e3);
var chord = d3.chord()
    .padAngle(0.05)
    .sortSubgroups(d3.descending);
var arc = d3.arc()
    .innerRadius(innerRadius)
    .outerRadius(outerRadius);
var ribbon = d3.ribbon()
    .radius(innerRadius);
var color5 = d3.scaleOrdinal()
    .domain(d3.range(4))
    .range(["rgb(201, 85, 158)", "#46e3c2"]);
var g = svg1.append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
    .datum(chord(matrix));
var group = g.append("g")
    .attr("class", "groups")
  .selectAll("g")
  .data(function(chords) { return chords.groups; })
  .enter().append("g");
group.append("path")
    .style("fill", function(d) { return color5(d.index); })
    .style("stroke", function(d) { return d3.rgb(color5(d.index)).darker(); })
    .attr("d", arc);
g.append("g")
    .attr("class", "ribbons")
  .selectAll("path")
  .data(function(chords) { return chords; })
  .enter().append("path")
    .attr("d", ribbon)
    .style("fill", function(d) { return color5(d.target.index); })
    .style("stroke", function(d) { return d3.rgb(color5(d.target.index)).darker(); });
// Returns an array of tick angles and values for a given group and step.
function groupTicks(d, step) {
  var k = (d.endAngle - d.startAngle) / d.value;
  return d3.range(0, d.value, step).map(function(value) {
    return {value: value, angle: value * k + d.startAngle};
  });
}
</script>
