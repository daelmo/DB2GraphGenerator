#Using Graph Similarity Measures on Converted Relational Database

## Step 1: create graph with graphgenerator
build graph out of sakila db: \
\
`python3 1_create_graph.py `

## Step 2 : Data Translation to .bcsr
for data conversion from edge list to bcsr format: \
\
`python ./verse/python/convert.py data/1_edge_list/graph.edgelist data/2_bcsr_file/graph.bcsr --format edgelist --directed
`
## Step 3 : Execute Verse

`./verse/src/verse -input data/2_bcsr_file/graph.bcsr -output data/3_vectors/vectors.bin -dim 128 -alpha 0.85 -threads 4 -nsamples 3
`

## Step 4 : calculate graph and vector similarity + compare
`python3 4_calc_similarities.py`