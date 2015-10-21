Recurring Event analysis
----------------------------

An attempt at a Bayesian re-analysis of Rampino&Caldeira 2015

* Article: Rampino&Caldeira 2015 http://mnras.oxfordjournals.org/content/454/4/3480.abstract
* Discussion thread: https://www.facebook.com/groups/astro.r/permalink/889900187772654/

Model for the event probability
---------------------------------

Code: extinction.py

A flat distribution plus a Gaussian which is repeated.

Parameters:

* s Strength of the Gaussian (0-1, remainder is in the flat distribution)
* w Width/Duration [in Myrs]
* p Period [in Myrs]
* phase Phase [0-1]

Interpretation
----------------

1. If a significant recurring signal is in the data, s should by > 0 and p should be constrained.
2. If the data is uniformly random (not periodic), s should be 0 and all signal parameters (s, w, p) should be unconstrained.

Analysis of Mock data
-----------------------

* Data: extinction_testdata.txt

  * generated events at [ 15,  35,  55,  75,  95, 115, 135, 155, 175, 195, 215, 235] Myrs 
  *   and 5 randomly placed events
  * with uncertainty of 0.1 Myrs

* Data and posterior of the model: extinction_testdata.txt_gauss_predict.png
* Parameter posterior distributions: See file extinction_testdata.txt_gaussmarg.png

Conclusion: Signal detected/recovered.

Analysis of Real data
------------------------

* Data: extinction.txt

  * from the article

* Data and posterior of the model: extinction.txt_gauss_predict.png
* Parameter posterior distributions: See file extinction.txt_gaussmarg.png

Conclusion: No signal detected. In particular the period posterior distribution is flat.


