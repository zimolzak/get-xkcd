library(ggplot2)
X = read.csv("C:/Users/vhabhszimola/Documents/local/get-xkcd/out.txt", header=TRUE, stringsAsFactors=FALSE, colClasses = "numeric")
p = ggplot(X, aes(panels, words)) + geom_point()
ggsave("scatter.png", plot = p, dpi = 100)
