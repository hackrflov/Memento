## Goals
- Presentation
- Exploration
- Confirmation

## Data Reduction 
- Filtering: Eliminate some items or attributes
- Aggregation: Represent a group of elements by a new derived element  
[Never use 3D plot, use visual attribute instead]

## Type of Chart 
+ Comparisons
    - Bar Chart: For showing categorical data.
    - Line Chart: For extrapolating numerical data(both x and y axises). [Use log scale instead of linear scale to magnify changes]
    - Stacked Bar Chart: Good for observing overall trends.
    - Layered Bar Chart
    - Grouped Bar Chart
    - Stacked Area Chart: Use for showing quantitative data that changes over time
+ Correlations
    - Scatterplots: Use alpha value to avoid overplotting.
+ Compositions
    - Pie Charts: Use it only when proportion is highly focused(In other situation we use bar charts).
+ Distribution
    - Histogram: Choose suitable bins.
    - Density Plots: Smooth curve established upon histogram.
    - Heat Maps: 2d chart with distinct clusters.
    - Box Plots: Use **median** and interquartile range as box and 1.5 x IQR as whisker per side.
    - Violin Plot: A box plot plus the probability density.

## Terms 
- *How to chosse aspect ratios?* Banking to 45 degrees(the curve maximized to 45).

## Two features
- Expressive: showing the data and just the data
- Effective: enable the user to perform the task

## Visual Variables
- Points
- Lines
- Areas
- Position
- Shape
- Size
- Color: bad for quantitative data (use brightness or diverging color instead) [Color Brewer]
- Tilt
- Volume

## Grouping Principles
- Containment
- Connection
- Proximity
- Similarity
- Continuity
- Common Fate

## Design Principles
- Alaways start your bar from zero. Scales are critical!
- Pie chart should always add up to 100.
- Size of the graphic effect should be directly proportional to the numerical quantities.
- 3D plot is bad as it will cause distortion.
- Maximize data-ink ratio.
- Avoid chart junk.

## Mutli-dimension Visualization
+ No/little analytics
    - Scatterplot Matrix: Put every dimension both in columns and rows to form a matrix (N x N in total and N*(N-1)/2 usable).
    - Parallel Coordinates: Axes represent attributes, lines connecting axes represent items. 
        - Limitation 1: It cannot handle large axes and items. [Use opacity, cluster or sampling to solve this] 
        - Limitation 2: Correlations only between adjacent axes. [Add user interaction to drag or drop axes]
        - Limitation 3: Ambiguity. [Use interactive highlighting or use curves]
    - Flexible Linked Axes
    - Radial Axis Techniques: Axes radiate from a common origin. [Most used: Star Plot]
    - Table Lens
    - LineUp
    - Visual Attributes: Glyph as Marks
+ Simple Analytic Component
    - Pixel-based Visualizations / Heat Maps: Each cell is a "pixel", value encoded using color, and meaning derived from ordering, if no ordering inherent, clustering is used.
+ String Analytics Components
    - Dimensionality Reduction (e.g.PCA)

## Map
- Dot Map
- Choropleth Map
- Isarithmic Map: Color coding continuous phenomena
- Cartograms: Size of region scaled to arttibute value
- Flow Maps

## Text Visualization
- Tag Cloud / Word Cloud / Wordle: Change word size/color by frequency
- Spark Clouds: Convey trends between multiple tag clouds over time
- Theme River / Stream Graph: Thematic changes over time. Height = frequncy
- Literature Fingerprinting

## Software
- tableau
- Data-Driven Documents (D3.js)

## Books
1. The Visual Display of Quantitative Information, Edward Tufte
2. Show Me the Numbers, Stephen Few
3. Visualization Analysis and Design, Tamara Munzner

## Reference
CS109

