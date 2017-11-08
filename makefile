scatter.png : out.txt plot.R
	Rscript plot.R

out.txt : get-xkcd.py
	python3 get-xkcd.py 1 1600 > out.txt

clean :
	rm -f out.txt scatter.png

test :
	python3 get-xkcd.py > out.txt
	Rscript plot.R
