<br />
<div align="center">

  <h3 align="center">abalyzer</h3>

  <p align="center">
    Parses ABA (American Bankers Association) codes

   <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

Parsing out information from ABA numbers can be tricky without the use of online lookup tools. This project aims to create an offline and open-source alternative. When used, the package can be used to validate ABA numbers and if valid, return information about the number including:
 - Bank Name
 - Bank Address
 - Bank State
 - Bank Phone Number

#### ABA Number Validation:
> Check digit\
> The ninth, check digit provides a checksum test using a position-weighted sum of each of the digits. High-speed check-sorting equipment will typically verify the checksum and if it fails, route the item to a reject pocket for manual examination, repair, and re-sorting. Mis-routings to an incorrect bank are thus greatly reduced.
>
> The following condition must hold: \
> (3(d1 + d4 + d7) + 7(d2 + d5 + d8) + (d3 + d6 + d9)) mod 10 = 0


-----------
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

