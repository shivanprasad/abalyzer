# abalyzer
Parses ABA (American Bankers Association) codes


### ABA Number Validation:
> Check digit\
> The ninth, check digit provides a checksum test using a position-weighted sum of each of the digits. High-speed check-sorting equipment will typically verify the checksum and if it fails, route the item to a reject pocket for manual examination, repair, and re-sorting. Mis-routings to an incorrect bank are thus greatly reduced.
>
> The following condition must hold: \
> (3(d1 + d4 + d7) + 7(d2 + d5 + d8) + (d3 + d6 + d9)) mod 10 = 0 [^1]


-----------
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)


[^1]: https://en.wikipedia.org/wiki/ABA_routing_transit_number
