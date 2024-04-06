# idea vomit

at appending a component the sizes and surfaces and shit of all the children are recursively recalculated
    -> working on


- components are nested sequentialy, not recursively -> DONE

- everything in append happens in relation to the component being appended to
    -> recompute position of children DONE

# idea vomit 2 *optimalization*

*readability* -> take a look at output of pylint in github actions <https://github.com/MisustinIvan/ParticleSimulator/actions>

call to c functions to calculate shit <https://www.digitalocean.com/community/tutorials/calling-c-functions-from-python>

use mojo <https://docs.modular.com/mojo>

send events only to components who want them
    -> working on


# cache surfaces of components that dont have to be redrawn

- static components -> labels for now -> DONE

- dynamic components -> buttons -> dont redraw if mouse not moved -> DONE