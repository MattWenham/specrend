# Colour Rendering of Spectra

This is a fairly direct port of the C code to be found on [John Walker](https://www.fourmilab.ch/)'s webpage titled [Colour Rendering of Spectra](https://www.fourmilab.ch/documents/specrend/). I've used named tuples to substitute for C `struct`s, and the black body radiation example code has been taken into a separate source file. I've also eliminated the *z* CIE component from the exposed data structure, as this can always be derived from the *x* and *y* components: 

<a href="https://www.codecogs.com/eqnedit.php?latex=$$&space;z=1-(x&plus;y)&space;$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$&space;z=1-(x&plus;y)&space;$$" title="$$ z=1-(x+y) $$" /></a>

The black body radiation test code produces the same output as Walker's C code, but I have not yet tested it further.