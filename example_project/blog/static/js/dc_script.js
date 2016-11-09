function drawCircles(data, width, height){

  var colors = ["#e24b4b", "#e1874b", "#e1a44c"];

  //Create the SVG Viewport
  var svgContainer = d3.select("#blog_bubbles").append("svg")
                                       .attr("width",width+300)
                                       .attr("height",height+150);

  //Add circles to the svgContainer
  var circles = svgContainer.selectAll("circle")
                             .data(data)
                             .enter()
                             .append("circle");

  //Add the circle attributes
  var circleAttributes = circles
                         .attr("cx", function (d) { return d.coordinates[0]; })
                         .attr("cy", function (d) { return d.coordinates[1]; })
                         .attr("r", "8" )
                         .attr("fill", "#e24b4b")
                         .on("mouseover", function(d){
                            increaseCircl(this);
                         })
                         .on("mouseout", function(d){
                            restoreCircl(this);
                         })
                         .on("click", function(d){
                            window.open(d.url, '_blank');
                         });

  //Add the SVG Text Element to the svgContainer
  var text = svgContainer.selectAll("text")
                          .data(data)
                          .enter()
                          .append("text");

  //Add SVG Text Element Attributes
  var textLabels = text
                   .attr("x", function(d) { return d.coordinates[0] + 17; })
                   .attr("y", function(d) { return d.coordinates[1] + 4; })
                   .text( function (d) { return d.title; })
                   .attr("fill", "red");

}


function increaseCircl(d3_) {
  d3.select(d3_)
  .transition()
  .duration(500)
  .attr("r", "18");
}

function restoreCircl(d3_){
  d3.select(d3_)
  .transition()
  .duration(500)
  .attr("r", "8");
}